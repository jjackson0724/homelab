# PCAP Analysis #001 — Home Network Baseline
**Project:** Mad Hat Purple Team Roadmap — Project #16 (PCAP/C2 Analysis)  
**Analyst:** Jarron Jackson  
**Date:** June 27, 2026  
**Tool:** Wireshark 4.x / Scapy (Python) / Nmap 7.99  
**Capture Node:** Sentinel (Lenovo IdeaPad, AMD Ryzen 7 5825U, Windows 11)  
**Capture Interface:** Wi-Fi (home network — 192.168.1.0/24)  
**File:** sentpackets.pcapng (171MB)  
**Packets Analyzed:** 50,000 (sampled from full capture)  

---

## Objective

Establish a network traffic baseline for the home lab environment using passive packet capture on Sentinel. Identify all active hosts, characterize traffic patterns, flag anomalous or unexpected communications, and develop familiarity with real-world PCAP analysis methodology.

---

## Methodology

1. Installed Wireshark and Npcap 1.87 on Sentinel
2. Initiated passive capture on Wi-Fi interface (no traffic injection)
3. Captured live traffic for approximately 20 minutes during normal household activity
4. Exported capture as sentpackets.pcapng
5. Performed automated analysis using Python/Scapy for statistical breakdown
6. Cross-referenced DNS queries against known services and telemetry endpoints
7. Performed active follow-up scanning with Nmap against identified hosts

---

## Protocol Distribution

| Protocol | Packet Count | Percentage | Notes |
|----------|-------------|------------|-------|
| UDP | 45,671 | 91.3% | Dominated by streaming traffic |
| TCP | 131 | 0.26% | HTTPS, Microsoft services |
| Other | ~4,199 | 8.4% | Broadcast, ARP, other |

**Finding:** UDP dominance is consistent with active video streaming on the network during capture window. Netflix on PS5 uses UDP for low-latency delivery — packet drops are acceptable in streaming whereas TCP retransmission latency is not.

---

## Host Inventory

### Internal Hosts Identified

| IP Address | Packets Sent | Packets Received | Identified As |
|------------|-------------|-----------------|---------------|
| 192.168.1.1 | 45,631 | 3 | Spectrum SAX2V1R Router/Gateway |
| 192.168.1.35 | 90 | 45,712 | **PS5** (PlayStation Network streaming ports 12478/12488) |
| 192.168.1.47 | 8 | 0 | **Unknown** — requires follow-up investigation |
| 192.168.1.196 | (Sentinel itself) | — | Sentinel — capture node |

### External Hosts Contacted

| IP Address | Service | Notes |
|------------|---------|-------|
| 34.54.194.141 | Google Cloud | Browser/app traffic |
| 52.168.117.169 | Microsoft Azure | Windows/Office telemetry |
| 52.168.117.171 | Microsoft Azure | Windows/Office telemetry |
| 162.254.192.99 | Steam (Valve) | Steam client background traffic |
| 135.234.174.40 | Microsoft | OneDrive/Skydrive sync |
| 72.153.5.129 | AT&T/ISP Infrastructure | Transit/routing |
| 172.183.7.192 | Microsoft Azure | Background service |
| 239.255.255.250 | Multicast (SSDP/UPnP) | Local network discovery |

---

## PS5 Identification — Traffic Signature Analysis

The dominant traffic pattern (91% of all UDP traffic) was:
- **Source:** 192.168.1.1 (router forwarding inbound internet traffic)
- **Destination:** 192.168.1.35
- **Ports:** 12478 and 12488 (destination)
- **Packet size:** Consistent 60-byte frames, Len=18
- **Frequency:** Near-continuous, high rate

**Analysis:** Ports 12478 and 12488 are Sony PlayStation Network streaming ports used for remote play and media streaming. The consistent packet size and high frequency are characteristic of video stream buffering. This traffic pattern was confirmed to be Netflix streaming on a PS5 during the capture window.

**Key lesson:** Traffic baseline identification — recognizing normal patterns (streaming signatures, consistent packet size, known ports) is a prerequisite for identifying abnormal patterns. A SOC analyst must know what normal looks like before they can define anomalous.

---

## Post-Analysis Correction — DHCP IP Reassignment (June 28, 2026)

**Finding:** Initial host identification of 192.168.1.35 as PS5 was correct at time of capture but required correction after post-capture investigation.

**What changed:** Following the capture session, ipconfig /all on Zion revealed that 192.168.1.35 is currently assigned to Zion's Wi-Fi adapter (MediaTek Wi-Fi 6 MT7921). The PS5 had released its DHCP lease after being powered off, and the router subsequently reassigned 192.168.1.35 to Zion during a lease renewal.

**Critical lesson:** IP addresses on home networks are not reliable long-term device identifiers. MAC addresses are the correct identifier for persistent device attribution. The monitor bot should be updated to track MAC + IP pairs and alert on unexpected mapping changes.

**Remediation:** Assign static DHCP leases to all known devices via router — PS5, Zion, Sentinel all get permanent IP assignments tied to their MAC addresses.

---

## DNS Query Analysis

DNS queries reveal application behavior even when payload traffic is encrypted. The following domains were resolved during the capture:

### Expected / Benign
| Domain | Service | Classification |
|--------|---------|----------------|
| claude.ai | Anthropic Claude | Analyst activity during capture |
| a-api.anthropic.com | Anthropic API backend | Analyst activity |
| s-cdn.anthropic.com | Anthropic CDN | Analyst activity |
| assets-proxy.anthropic.com | Anthropic assets | Analyst activity |
| spclient.wg.spotify.com | Spotify | Background music app |
| p2p-iad1.discovery.steamserver.net | Steam P2P | Steam client background |
| login.microsoftonline.com | Microsoft SSO | Windows account auth |
| skydrive.wns.windows.com | OneDrive | Cloud sync |
| cdn-dynmedia-1.microsoft.com | Microsoft CDN | Windows Update/telemetry |
| accounts.google.com | Google auth | Browser background |
| clientservices.googleapis.com | Google services | Chrome/browser |
| images-eds-ssl.xboxlive.com | Xbox Live | Game Pass / Xbox app |

### Requires Investigation
| Domain | Service | Finding |
|--------|---------|---------|
| browser-intake-us5-datadoghq.com | DataDog telemetry | Unknown application sending usage telemetry to DataDog monitoring platform — source app not yet identified |
| o1158394.ingest.us.sentry.io | Sentry error reporting | Application on Sentinel sending crash/error telemetry to Sentry — source app not yet identified |
| wpad.lan | WPAD proxy discovery | Windows attempting Web Proxy Auto-Discovery on local network — no server responding, but represents attack surface (WPAD poisoning attack vector) |
| www.bing.com | Microsoft/Bing | Windows background telemetry query — consistent with Windows Search indexing behavior |
| array508.prod.do.dsp.mp.microsoft.com | Microsoft DSP | Advertising/telemetry pipeline — Windows telemetry that should be disabled |

---

## Findings & Risk Assessment

### Finding 1 — Unidentified Host 192.168.1.47
**Severity:** Medium  
**Description:** An internal host at 192.168.1.47 generated 8 packets during the capture window. The host was not identified via Nmap (ping-blocked, all ports filtered). MAC address not yet resolved via ARP table.  
**Risk:** Unknown device on network represents uncontrolled attack surface. If compromised or rogue, it has full LAN access.  
**Remediation:** Identify via router DHCP table, MAC lookup, and passive traffic analysis. Consider network segmentation via VLAN to isolate IoT/unknown devices.  
**Status:** Open — follow-up required.

### Finding 2 — WPAD Broadcast Exposure
**Severity:** Low-Medium  
**Description:** Sentinel is broadcasting WPAD (Web Proxy Auto-Discovery) queries to wpad.lan. No server is responding, but the queries are visible on the network.  
**Risk:** An attacker on the local network could respond to WPAD queries and redirect all HTTP/HTTPS traffic through a malicious proxy — enabling MITM attacks.  
**Remediation:** Disable WPAD in Windows registry:  
```
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp
DisableWpad = 1
```
**Status:** Open — remediation pending.

### Finding 3 — DataDog and Sentry Telemetry
**Severity:** Low  
**Description:** An unidentified application on Sentinel is sending telemetry data to DataDog (browser-intake-us5-datadoghq.com) and Sentry (sentry.io). These are legitimate monitoring platforms but the source application has not been identified.  
**Risk:** Application telemetry may include system information, usage patterns, or error details being transmitted to third-party platforms.  
**Remediation:** Identify source application via process monitoring correlated with DNS query timing. Review what data is being transmitted.  
**Status:** Open — investigation pending.

### Finding 4 — Windows Telemetry Active
**Severity:** Low  
**Description:** Multiple Microsoft telemetry endpoints observed (array508.prod.do.dsp.mp.microsoft.com, cdn-dynmedia-1.microsoft.com). Windows telemetry cleanup is on the Zion hardening roadmap but has not been applied to Sentinel.  
**Remediation:** Apply Windows telemetry hardening to Sentinel — disable DiagTrack service, configure telemetry registry keys, apply hosts file blocks.  
**Status:** Open — scheduled for future hardening session.

---

## TCP Port Analysis

| Destination Port | Count | Service | Notes |
|-----------------|-------|---------|-------|
| 443 | 68 | HTTPS/TLS | Encrypted web traffic — expected |
| 55002 | 16 | Unknown | High ephemeral port — likely P2P or game traffic |
| 62291 | 14 | Unknown | Ephemeral — likely Steam P2P |
| 60839 | 9 | Unknown | Ephemeral |
| 65343/65344 | 9/7 | Unknown | High ephemeral ports — investigation warranted |

---

## MITRE ATT&CK Mapping

This analysis exercise covers detection relevant to the following ATT&CK techniques:

| Technique | ID | Relevance |
|-----------|-----|-----------|
| Network Service Discovery | T1046 | Nmap scanning performed against discovered hosts |
| System Network Connections Discovery | T1049 | Netstat/traffic analysis of active connections |
| DNS | T1071.004 | DNS query analysis for C2 detection methodology |
| Exfiltration Over Web Service | T1567 | Telemetry identification (DataDog/Sentry) |
| Adversary-in-the-Middle | T1557 | WPAD exposure identified |

---

## Tools Used

| Tool | Version | Purpose |
|------|---------|---------|
| Wireshark | 4.x | Live packet capture |
| Npcap | 1.87 | Windows packet capture driver |
| Python/Scapy | 3.x / latest | Automated PCAP statistical analysis |
| Nmap | 7.99 | Active host scanning and service fingerprinting |

---

## Next Steps

- [ ] Identify 192.168.1.47 via router DHCP table and MAC lookup
- [ ] Disable WPAD on Sentinel via registry
- [ ] Identify DataDog/Sentry telemetry source application
- [ ] Apply Windows telemetry hardening to Sentinel
- [ ] Capture second PCAP after remediation and compare baseline
- [ ] Install Zeek/Suricata on Sentinel (pending OS decision) for automated detection
- [ ] Correlate findings with Seraph (Wazuh) when SIEM comes online in Phase 2
- [ ] Perform C2 traffic simulation and detection (Phase 1 project continuation)

---

## Conclusion

This baseline capture successfully identified all active hosts on the home network, characterized normal traffic patterns, and surfaced four findings requiring remediation. The dominant traffic pattern (PS5 Netflix streaming) was identified through port analysis and packet signature characteristics — demonstrating the core skill of distinguishing normal from anomalous traffic.

The DNS query log proved to be the most intelligence-rich data source in this capture, revealing application behavior, telemetry destinations, and attack surface (WPAD) that would not be visible in encrypted payload analysis alone. This reinforces the value of DNS monitoring as a detection layer — a principle that will be implemented in Seraph (Wazuh) when the SIEM comes online.

**NIST CSF Mapping:** Identify (ID.AM-1, ID.AM-3), Detect (DE.CM-1, DE.CM-7)
