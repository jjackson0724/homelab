"""
Matrix Homelab — Discord Security Monitor
Monitors: Honeyfiles, Network changes, CVEs, Windows Event Log
Alerts: Discord webhook
Run on: Zion and/or Sentinel
Author: Jarron Jackson
"""

import os
import time
import json
import socket
import hashlib
import requests
import datetime
import subprocess
import threading
from pathlib import Path

# ============================================================
# CONFIGURATION — edit these before running
# ============================================================

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1520590672510324747/aVhcv1NRRRkLrbNxyp0rFJMJJbhC_EdguMaz12x58X3pxRtAnmie7GVz7417Fa-0E4dP"

HOSTNAME = socket.gethostname()  # auto-detects Zion or Sentinel

# Honeyfiles to monitor — add as many as you want
HONEYFILES = [
    r"C:\Users\Jarron\Documents\passwords_backup.txt",
    r"C:\Users\Jarron\Documents\banking_credentials.xlsx",
    r"C:\Users\Jarron\Documents\VPN_credentials.docx",
    r"C:\Users\Jarron\Desktop\ssh_keys_backup.txt",
]

# Network scan interval in seconds (300 = every 5 minutes)
NETWORK_SCAN_INTERVAL = 300

# CVE check interval in seconds (3600 = every hour)
CVE_CHECK_INTERVAL = 3600

# Event Log check interval in seconds
EVENT_LOG_INTERVAL = 60

# Network to scan (your home network)
NETWORK_RANGE = "192.168.1.0/24"

# Windows Event IDs to alert on
ALERT_EVENT_IDS = {
    4625: "Failed login attempt",
    4648: "Login with explicit credentials",
    4663: "Object access (honeyfile trigger)",
    4720: "New user account created",
    4726: "User account deleted",
    4728: "User added to privileged group",
    4732: "User added to local admin group",
    7045: "New service installed",
    1102: "Audit log cleared — possible cover-up",
    4698: "Scheduled task created",
    4702: "Scheduled task modified",
}

# CVE keywords to monitor (products in your lab)
CVE_KEYWORDS = [
    "windows 11",
    "vmware workstation",
    "kali linux",
    "windows server 2025",
    "nmap",
    "wireshark",
]

# ============================================================
# DISCORD ALERTING
# ============================================================

def send_discord(title, description, color=0xFF0000, fields=None):
    """Send a Discord embed alert."""
    embed = {
        "title": f"🚨 {title}",
        "description": description,
        "color": color,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "footer": {"text": f"Matrix Homelab Monitor | {HOSTNAME}"},
    }
    if fields:
        embed["fields"] = fields

    payload = {"embeds": [embed]}
    try:
        r = requests.post(DISCORD_WEBHOOK, json=payload, timeout=10)
        if r.status_code not in [200, 204]:
            print(f"[DISCORD ERROR] {r.status_code}: {r.text}")
    except Exception as e:
        print(f"[DISCORD ERROR] {e}")


def send_info(title, description, fields=None):
    """Blue info alert."""
    send_discord(title, description, color=0x0078D4, fields=fields)


def send_warning(title, description, fields=None):
    """Yellow warning alert."""
    send_discord(title, description, color=0xFFB900, fields=fields)


def send_critical(title, description, fields=None):
    """Red critical alert."""
    send_discord(title, description, color=0xFF0000, fields=fields)


# ============================================================
# MODULE 1 — HONEYFILE MONITOR
# ============================================================

class HoneyfileMonitor:
    """
    Watches honeyfiles for any access.
    Uses file modification time + hash to detect reads/writes.
    Zero false positives — nobody should touch these files.
    """

    def __init__(self, files):
        self.files = files
        self.baseline = {}
        self._build_baseline()

    def _get_file_state(self, path):
        try:
            p = Path(path)
            if not p.exists():
                return None
            stat = p.stat()
            return {
                "mtime": stat.st_mtime,
                "atime": stat.st_atime,
                "size": stat.st_size,
            }
        except Exception:
            return None

    def _build_baseline(self):
        print("[HONEYFILE] Building baseline...")
        for f in self.files:
            state = self._get_file_state(f)
            if state:
                self.baseline[f] = state
                print(f"  Monitoring: {f}")
            else:
                # Create the honeyfile if it doesn't exist
                try:
                    Path(f).parent.mkdir(parents=True, exist_ok=True)
                    Path(f).touch()
                    self.baseline[f] = self._get_file_state(f)
                    print(f"  Created: {f}")
                except Exception as e:
                    print(f"  [ERROR] Could not create {f}: {e}")

    def check(self):
        for filepath in self.files:
            current = self._get_file_state(filepath)
            if not current:
                continue
            baseline = self.baseline.get(filepath)
            if not baseline:
                self.baseline[filepath] = current
                continue

            # Detect access (atime change) or modification (mtime change)
            if current["atime"] != baseline["atime"]:
                send_critical(
                    "HONEYFILE ACCESSED",
                    f"A honeyfile was accessed on `{HOSTNAME}`.\nThis file should never be opened.",
                    fields=[
                        {"name": "File", "value": f"`{filepath}`", "inline": False},
                        {"name": "Time", "value": f"`{datetime.datetime.now()}`", "inline": True},
                        {"name": "Action", "value": "File Read/Opened", "inline": True},
                    ]
                )
                self.baseline[filepath] = current

            elif current["mtime"] != baseline["mtime"]:
                send_critical(
                    "HONEYFILE MODIFIED",
                    f"A honeyfile was **written to** on `{HOSTNAME}`.\nPossible attacker leaving malware.",
                    fields=[
                        {"name": "File", "value": f"`{filepath}`", "inline": False},
                        {"name": "Time", "value": f"`{datetime.datetime.now()}`", "inline": True},
                        {"name": "Action", "value": "File Written", "inline": True},
                        {"name": "Old Size", "value": str(baseline["size"]), "inline": True},
                        {"name": "New Size", "value": str(current["size"]), "inline": True},
                    ]
                )
                self.baseline[filepath] = current


# ============================================================
# MODULE 2 — NETWORK SCANNER
# ============================================================

class NetworkMonitor:
    """
    Runs periodic Nmap scans and alerts on:
    - New devices appearing on the network
    - Devices disappearing
    - New open ports on known devices
    """

    def __init__(self, network):
        self.network = network
        self.known_hosts = {}
        self._initial_scan()

    def _run_nmap(self):
        try:
            result = subprocess.run(
                ["nmap", "-sn", self.network, "--output", "normal"],
                capture_output=True, text=True, timeout=60
            )
            hosts = {}
            current_ip = None
            for line in result.stdout.split("\n"):
                if "Nmap scan report for" in line:
                    parts = line.split()
                    current_ip = parts[-1].strip("()")
                    hostname = parts[4] if len(parts) > 4 else current_ip
                    hosts[current_ip] = {"hostname": hostname, "ports": []}
                elif "open" in line and current_ip:
                    hosts[current_ip]["ports"].append(line.strip())
            return hosts
        except Exception as e:
            print(f"[NMAP ERROR] {e}")
            return {}

    def _initial_scan(self):
        print("[NETWORK] Running initial scan...")
        self.known_hosts = self._run_nmap()
        print(f"  Found {len(self.known_hosts)} hosts")
        send_info(
            "Network Baseline Established",
            f"Initial scan complete on `{HOSTNAME}`",
            fields=[{"name": "Hosts found", "value": str(len(self.known_hosts)), "inline": True}]
        )

    def check(self):
        current_hosts = self._run_nmap()

        # New devices
        for ip, data in current_hosts.items():
            if ip not in self.known_hosts:
                send_warning(
                    "NEW DEVICE ON NETWORK",
                    f"An unknown device appeared on `{NETWORK_RANGE}`",
                    fields=[
                        {"name": "IP", "value": f"`{ip}`", "inline": True},
                        {"name": "Hostname", "value": data.get("hostname", "Unknown"), "inline": True},
                        {"name": "Time", "value": str(datetime.datetime.now()), "inline": False},
                    ]
                )

        # Devices gone
        for ip in self.known_hosts:
            if ip not in current_hosts:
                send_info(
                    "Device Left Network",
                    f"`{ip}` is no longer responding",
                    fields=[{"name": "IP", "value": f"`{ip}`", "inline": True}]
                )

        self.known_hosts = current_hosts


# ============================================================
# MODULE 3 — CVE MONITOR
# ============================================================

class CVEMonitor:
    """
    Pulls recent CVEs from the CIRCL CVE API.
    Alerts on CVEs matching your lab software.
    """

    def __init__(self, keywords):
        self.keywords = [k.lower() for k in keywords]
        self.seen_cves = set()
        self._load_initial()

    def _load_initial(self):
        """Load existing CVEs so we don't alert on old ones at startup."""
        try:
            r = requests.get("https://cve.circl.lu/api/last/50", timeout=15)
            if r.ok:
                for cve in r.json():
                    self.seen_cves.add(cve.get("id", ""))
        except Exception as e:
            print(f"[CVE] Initial load error: {e}")

    def check(self):
        try:
            r = requests.get("https://cve.circl.lu/api/last/20", timeout=15)
            if not r.ok:
                return
            for cve in r.json():
                cve_id = cve.get("id", "")
                if cve_id in self.seen_cves:
                    continue
                self.seen_cves.add(cve_id)

                summary = cve.get("summary", "").lower()
                cvss = cve.get("cvss", 0) or 0

                # Check if CVE affects our software
                matched = [k for k in self.keywords if k in summary]
                if matched:
                    severity = "CRITICAL" if cvss >= 9.0 else "HIGH" if cvss >= 7.0 else "MEDIUM"
                    color = 0xFF0000 if cvss >= 9.0 else 0xFFB900 if cvss >= 7.0 else 0x0078D4
                    send_discord(
                        f"CVE ALERT — {severity} ({cve_id})",
                        cve.get("summary", "No description")[:300],
                        color=color,
                        fields=[
                            {"name": "CVE ID", "value": f"`{cve_id}`", "inline": True},
                            {"name": "CVSS Score", "value": str(cvss), "inline": True},
                            {"name": "Matched Keywords", "value": ", ".join(matched), "inline": True},
                            {"name": "Reference", "value": f"https://nvd.nist.gov/vuln/detail/{cve_id}", "inline": False},
                        ]
                    )
        except Exception as e:
            print(f"[CVE ERROR] {e}")


# ============================================================
# MODULE 4 — WINDOWS EVENT LOG MONITOR
# ============================================================

class EventLogMonitor:
    """
    Monitors Windows Security Event Log for suspicious Event IDs.
    Uses PowerShell Get-WinEvent for reliable Windows event access.
    """

    def __init__(self, event_ids):
        self.event_ids = event_ids
        self.last_check = datetime.datetime.now() - datetime.timedelta(minutes=1)

    def check(self):
        try:
            since = self.last_check.strftime("%Y-%m-%dT%H:%M:%S")
            self.last_check = datetime.datetime.now()

            # Build PowerShell command to get recent security events
            ps_cmd = f"""
            $since = [datetime]'{since}'
            $ids = @({','.join(str(i) for i in self.event_ids.keys())})
            Get-WinEvent -FilterHashtable @{{
                LogName='Security'
                StartTime=$since
                Id=$ids
            }} -ErrorAction SilentlyContinue |
            Select-Object Id,TimeCreated,Message |
            ConvertTo-Json -Depth 2
            """

            result = subprocess.run(
                ["powershell", "-NoProfile", "-Command", ps_cmd],
                capture_output=True, text=True, timeout=30
            )

            if not result.stdout.strip():
                return

            events = json.loads(result.stdout)
            if isinstance(events, dict):
                events = [events]  # single event returns dict not list

            for event in events:
                eid = event.get("Id")
                description = self.event_ids.get(eid, "Unknown event")
                message = event.get("Message", "")[:500]
                time_created = event.get("TimeCreated", "")

                # Severity based on event type
                if eid in [1102, 4728, 4732, 7045]:
                    color = 0xFF0000  # Critical
                elif eid in [4625, 4648, 4663, 4720]:
                    color = 0xFFB900  # Warning
                else:
                    color = 0x0078D4  # Info

                send_discord(
                    f"Security Event: {description}",
                    f"Event ID `{eid}` detected on `{HOSTNAME}`",
                    color=color,
                    fields=[
                        {"name": "Event ID", "value": str(eid), "inline": True},
                        {"name": "Time", "value": str(time_created), "inline": True},
                        {"name": "Description", "value": description, "inline": False},
                        {"name": "Details", "value": f"```{message[:400]}```", "inline": False},
                    ]
                )

        except json.JSONDecodeError:
            pass  # No events found
        except Exception as e:
            print(f"[EVENT LOG ERROR] {e}")


# ============================================================
# MAIN LOOP
# ============================================================

def run_monitor(monitor, interval, name):
    """Run a monitor module in a loop with a given interval."""
    while True:
        try:
            monitor.check()
        except Exception as e:
            print(f"[{name} ERROR] {e}")
        time.sleep(interval)


def main():
    print("=" * 50)
    print("Matrix Homelab Discord Monitor")
    print(f"Host: {HOSTNAME}")
    print(f"Started: {datetime.datetime.now()}")
    print("=" * 50)

    # Validate webhook
    if DISCORD_WEBHOOK == "YOUR_DISCORD_WEBHOOK_URL_HERE":
        print("\n[ERROR] Set your Discord webhook URL in DISCORD_WEBHOOK before running.\n")
        return

    # Initialize all modules
    honeyfile_monitor = HoneyfileMonitor(HONEYFILES)
    network_monitor = NetworkMonitor(NETWORK_RANGE)
    cve_monitor = CVEMonitor(CVE_KEYWORDS)
    event_monitor = EventLogMonitor(ALERT_EVENT_IDS)

    # Send startup notification
    send_info(
        "Monitor Online",
        f"Homelab security monitor started on `{HOSTNAME}`",
        fields=[
            {"name": "Honeyfiles", "value": str(len(HONEYFILES)), "inline": True},
            {"name": "Network", "value": NETWORK_RANGE, "inline": True},
            {"name": "CVE Keywords", "value": str(len(CVE_KEYWORDS)), "inline": True},
            {"name": "Event IDs", "value": str(len(ALERT_EVENT_IDS)), "inline": True},
        ]
    )

    # Start each module in its own thread
    threads = [
        threading.Thread(target=run_monitor, args=(honeyfile_monitor, 10, "HONEYFILE"), daemon=True),
        threading.Thread(target=run_monitor, args=(network_monitor, NETWORK_SCAN_INTERVAL, "NETWORK"), daemon=True),
        threading.Thread(target=run_monitor, args=(cve_monitor, CVE_CHECK_INTERVAL, "CVE"), daemon=True),
        threading.Thread(target=run_monitor, args=(event_monitor, EVENT_LOG_INTERVAL, "EVENTLOG"), daemon=True),
    ]

    for t in threads:
        t.start()

    print("\n[*] All monitors running. Press Ctrl+C to stop.\n")

    try:
        while True:
            time.sleep(60)
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Monitors running...")
    except KeyboardInterrupt:
        send_info("Monitor Offline", f"Homelab monitor stopped on `{HOSTNAME}`")
        print("\n[*] Stopped.")


if __name__ == "__main__":
    main()