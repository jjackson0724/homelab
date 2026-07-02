# Purple Team Lab Report
## T1049 — System Network Connections Discovery
**Date:** July 1, 2026  
**Author:** Jarron Jackson  
**Lab:** Matrix Homelab  
**Phase:** Phase 1 — Pre-SIEM Baseline  
**ATT&CK Technique:** [T1049](https://attack.mitre.org/techniques/T1049/)  
**MITRE Tactic:** Discovery  

---

## Objective

Execute MITRE ATT&CK technique T1049 (System Network Connections Discovery) using Atomic Red Team on the Trinity attack machine, document the full output from an attacker's perspective, and record the detection outcome in VECTR as part of a Phase 1 purple team baseline engagement.

This is technique #4 and the final Discovery technique executed on Trinity before pivoting to Sentinel for credential dumping and persistence operations.

---

## Attack Chain Context

| Order | Technique | ID | Status |
|---|---|---|---|
| 1 | Local Account Discovery | T1087.001 | ✅ Complete |
| 2 | Process Discovery | T1057 | ✅ Complete |
| 3 | System Information Discovery | T1082 | ✅ Complete |
| 4 | Network Connection Discovery | T1049 | ✅ Complete |
| 5 | Credential Dumping | T1003 | Planned — Sentinel target |
| 6 | Scheduled Task Persistence | T1053.005 | Planned — Sentinel target |
| 7 | Disable Security Tools | T1562.001 | Planned — Sentinel target |

---

## Environment

| Role | Machine | OS | Notes |
|---|---|---|---|
| Attacker | Trinity | Kali Linux 2026.2 | VMware VM on Zion |
| Target | Trinity (local) | Kali Linux 2026.2 | Self-targeted for Phase 1 baseline |
| Documentation | Zion | Windows 11 | VECTR CE 9.12.2 running via Docker |
| Detection | None | N/A | Pre-Seraph. No SIEM active. |

---

## Tools Used

### Execution Layer
| Tool | Purpose |
|---|---|
| Atomic Red Team | Library of 1,000+ MITRE ATT&CK-mapped attack scripts |
| Invoke-AtomicRedTeam (PowerShell module v2.3.0) | Test runner — executes individual Atomics by technique ID |

### Management & Tracking Layer
| Tool | Purpose |
|---|---|
| VECTR Community Edition 9.12.2 | Purple team engagement tracking, outcome documentation, and MITRE ATT&CK heatmap generation |

### Planned (Phase 2)
| Tool | Purpose |
|---|---|
| MITRE CALDERA | Automated adversary emulation — will chain T1087.001 through T1049 in a single adversary profile against Sentinel, watched by Wazuh in real time |

---

## What Is T1049?

After identifying who is on a machine, what is running, and what the system's configuration looks like, an attacker maps the network. T1049 covers System Network Connections Discovery — enumerating all active network connections to identify:

- The machine's IP address and network segment
- What other machines this host is communicating with
- Open ports and listening services
- Logged-in users and active sessions

This information directly enables lateral movement. Once the attacker knows the network segment, a single `nmap` sweep reveals every other host — including Sentinel — without ever touching those machines directly.

---

## Execution

**Command used:**
```powershell
Invoke-AtomicTest T1049 -TestNumbers 4,5 -PathToAtomicsFolder ~/atomic-red-team/atomics
```

Sub-tests selected and rationale:

| Test # | Name | Selected | Reason |
|---|---|---|---|
| T1049-4 | Network Connections via ss | ✅ | Primary tool — maps all TCP/UDP connections |
| T1049-5 | Network Connections via netstat + who -a | ✅ | Confirms connections and active user sessions |
| T1049-6 | sockstat | ❌ | FreeBSD focused — not applicable |

Both selected tests returned **Exit code: 0** (successful execution).

---

## Attack Output Analysis

### Test 4 — ss Output (Most Critical)

**Raw output:**
```
State  Recv-Q  Send-Q  Local Address:Port       Peer Address:Port
ESTAB  0       0       192.168.161.128%eth0:68  192.168.161.254:67
```

**Attacker interpretation:**

| Finding | Value | Attacker Significance |
|---|---|---|
| Trinity IP | `192.168.161.128` | Attacker's own IP on the lab network confirmed |
| Network segment | `192.168.161.0/24` | Full lab network range identified |
| Gateway/DHCP | `192.168.161.254` | VMware virtual network gateway confirmed |
| Active connections | 1 (DHCP only) | No outbound C2, no active sessions to other machines |
| Interface | `eth0` | Single network interface — not multi-homed |

**Critical finding:** Network segment `192.168.161.0/24` is now known. An `nmap -sn 192.168.161.0/24` sweep will reveal every host on this segment including Sentinel. The attacker does not need to guess — they now have the exact range to scan.

---

### Test 5 — netstat + who -a Output

**Key network output:**
```
Proto  Recv-Q  Send-Q  Local Address            Foreign Address          State
udp    0       0       192.168.161.128:bootpc   192.168.161.254:bootps   ESTABLISHED
```

**Confirms:** Same findings as Test 4 — single DHCP connection, no other active network activity.

**who -a output:**
```
kali     seat0    2026-07-01 14:32   (:0)
         system boot  2026-07-01 14:31
```

**Attacker interpretation:**

| Finding | Value | Attacker Significance |
|---|---|---|
| Active user | `kali` | Single user confirmed |
| Session type | `:0` (local X11) | Not an SSH session — user is physically at the machine |
| Login time | 14:32 | User logged in 1 minute after boot |
| Boot time | 14:31 | Machine recently started |

**No SSH sessions active** — the attacker is not being observed by a remote administrator. The machine is running with a single local user session.

---

## Combined Intelligence Picture (After 4 Techniques)

| Category | Finding | Attacker Next Move |
|---|---|---|
| Identity | kali / uid=1000 / sudo group | Privilege escalation via sudo available |
| Defenses | No EDR, no Wazuh, no AV | Proceed without evasion |
| OS | Kali 2026.2 / kernel 6.19.14 / VMware VM | Tools will execute normally |
| Credentials | SSH agent running (from T1082) | SSH agent hijacking path available |
| Network | 192.168.161.0/24 / Trinity at .128 | Scan for Sentinel and other hosts |
| Sessions | Single local X11 session | No remote admin monitoring |
| Monitoring | Zero logging observed | No detection risk |

**The attacker now has everything needed to pivot.** The next step is scanning `192.168.161.0/24` to locate Sentinel, then moving laterally to execute T1003 (Credential Dumping) against it.

---

## VECTR Documentation

| Field | Value |
|---|---|
| Environment | Home_LAB |
| Assessment | Phase 1 - Network Connection Discovery |
| Campaign | T1049 - Network Connection Discovery |
| Defense Tool | Phase 1 Baseline (Manual Observation) |
| Technique | T1049 — System Network Connections Discovery |
| Phase | Discovery |
| Status | Completed |
| Outcome | **None** |
| Defense Success | **Unsuccessful** |
| Attack Source | Trinity (Kali Linux 2026.2) |
| Attack Target | Trinity (local — self) |

No alerts. No logs. No blocks. Full network map retrieved silently including IP, segment, and session information.

---

## Detection Opportunity (Future Wazuh Rule)

**Sigma rule concept:**
```yaml
title: Network Connection Discovery - Linux
status: experimental
description: Detects execution of network enumeration commands in rapid succession
logsource:
  category: process_creation
  product: linux
detection:
  selection:
    CommandLine|contains:
      - 'ss -antp'
      - 'ss -aunp'
      - 'netstat'
      - 'who -a'
  timeframe: 60s
  condition: selection | count() > 2
falsepositives:
  - System administrators performing network diagnostics
level: medium
tags:
  - attack.discovery
  - attack.t1049
```

**Additional detection opportunity:** Alert on `nmap` execution against internal subnets, which is the natural follow-up to T1049 in a real engagement. An attacker who discovers `192.168.161.0/24` will immediately sweep it.

---

## Phase 2 Plan — CALDERA Integration

In Phase 2, the full Discovery chain (T1087.001 → T1057 → T1082 → T1049) will be automated in a single CALDERA adversary profile executed against Sentinel:

1. CALDERA agent deployed on Sentinel
2. Full Discovery chain executes automatically
3. Wazuh on Seraph monitors for the behavioral pattern of all four techniques in sequence
4. Detection goal: alert on the chain, not just individual commands
5. VECTR outcomes updated for all four techniques

The chain detection is more valuable than individual technique detection — a single `netstat` is noise, but `netstat` following `ps aux` following `uname -a` following `cat /etc/passwd` is an attack in progress.

---

## Phase 1 Discovery Chain — Complete Summary

| Technique | Key Finding | Detection Outcome |
|---|---|---|
| T1087.001 | sudo group membership, uid=1000 | None |
| T1057 | No EDR/AV processes running | None |
| T1082 | Kernel 6.19.14, VMware VM, SSH agent active | None |
| T1049 | IP 192.168.161.128, segment /24, single session | None |

**Phase 1 Threat Resilience Score: 0.00%**

This is the documented baseline. All four techniques executed against Trinity with zero detection. Phase 2 will establish Wazuh coverage and retest each technique. The delta between 0% and the Phase 2 score is the measurable improvement.

---

## Next Phase — Pivot to Sentinel

Phase 1 Discovery is complete. The attacker now pivots to Sentinel (`192.168.161.x`) for:

- **T1003** — Credential Dumping (Windows target)
- **T1053.005** — Scheduled Task Persistence (Windows variant)
- **T1562.001** — Disable Security Tools

Sentinel prep required before proceeding:
1. Confirm Sentinel's IP via `ipconfig` on the Windows machine
2. Confirm Trinity can reach Sentinel via `ping`
3. Confirm both machines are on the same VMware network segment

---

## Remediation Notes

- Deploy auditd to capture network enumeration command execution
- Alert on `ss`, `netstat`, and `who` executed in rapid succession
- Alert on subsequent `nmap` scans against internal subnets
- Deploy Wazuh network monitoring rules to detect internal reconnaissance

---

## References

- [MITRE ATT&CK T1049](https://attack.mitre.org/techniques/T1049/)
- [Atomic Red Team T1049](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.md)
- [VECTR Community Edition](https://vectr.io)
- [MITRE CALDERA](https://caldera.mitre.org)
