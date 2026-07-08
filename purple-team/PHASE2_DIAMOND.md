\# Phase 2 — Diamond Model Writeups



\## Phase 2 Overview

Simulate how attackers establish a foothold and maintain access after initial compromise. Covers credential dumping, scheduled task persistence, and defense evasion. Intelligence layer: map every attack using the Diamond Model for attribution analysis and log all IoCs into MISP as formal threat intelligence events.



\*\*Techniques planned:\*\*

\- T1003 — Credential Dumping (LSASS Memory)

\- T1053.005 — Scheduled Task Persistence

\- T1562.001 — Disable or Modify Tools (Defense Evasion)



\*\*Attack origin:\*\* Trinity (Kali Linux) — 192.168.161.128

\*\*Target:\*\* Sentinel — 192.168.161.0/24

\*\*Next pivot:\*\* Morpheus (Domain Controller) on Neb



\---



\## Event PT-005 — T1003 Credential Dumping



\*\*Date:\*\* \[To be completed]

\*\*ATT\&CK Technique:\*\* T1003 — OS Credential Dumping

\*\*Phase:\*\* Phase 2

\*\*Tool:\*\* Mimikatz / Invoke-AtomicRedTeam



\### Adversary

\- \*\*Simulated Actor:\*\* APT28 / Red Team operator

\- \*\*Intent:\*\* Extract NTLM hashes and plaintext credentials for lateral movement to Morpheus

\- \*\*Sophistication:\*\* Nation-state



\### Capability

\- \*\*Tool Used:\*\* Mimikatz, Invoke-AtomicRedTeam

\- \*\*ATT\&CK Technique:\*\* T1003.001 — LSASS Memory

\- \*\*Delivery Method:\*\* PowerShell execution on Trinity

\- \*\*YARA Rule Written:\*\* Yes — see YARA\_RULES.md (Mimikatz\_Strings)

\- \*\*Sigma Rule Written:\*\* No



\### Infrastructure

\- \*\*Attack Origin:\*\* Trinity VM — 192.168.161.128

\- \*\*Redirector Used:\*\* No

\- \*\*C2 Channel:\*\* Local Atomic Red Team execution

\- \*\*TLS Fingerprint (JA4):\*\* \[Capture during execution]



\### Victim

\- \*\*Target Machine:\*\* Sentinel

\- \*\*Target Service:\*\* LSASS process

\- \*\*Impact:\*\* \[To be completed after execution]

\- \*\*Detected by Seraph:\*\* \[To be completed]

\- \*\*Detection Rule Triggered:\*\* \[To be completed]



\### IoCs Generated

| Type | Value | Notes |

|---|---|---|

| Process name | lsass.exe | Target process |

| Tool binary hash | \[SHA256 after execution] | Mimikatz binary |

| Privilege | SeDebugPrivilege | Required for LSASS access |



\### MISP Event

\- \*\*Logged to MISP:\*\* No (pending Neb build)

\- \*\*Event ID:\*\* PT-005

\- \*\*Tags:\*\* tlp:white, mitre-attack:T1003.001, purple-team



\### Analyst Notes

\[To be completed after execution — document what Seraph caught, what it missed, and what detection rule gaps exist]



\---



\## Event PT-006 — T1053.005 Scheduled Task Persistence



\*\*Date:\*\* \[To be completed]

\*\*ATT\&CK Technique:\*\* T1053.005 — Scheduled Task/Job

\*\*Phase:\*\* Phase 2

\*\*Tool:\*\* Invoke-AtomicRedTeam / schtasks.exe



\### Adversary

\- \*\*Simulated Actor:\*\* APT28 / Red Team operator

\- \*\*Intent:\*\* Establish persistent access that survives system reboots

\- \*\*Sophistication:\*\* Nation-state



\### Capability

\- \*\*Tool Used:\*\* Invoke-AtomicRedTeam, schtasks.exe

\- \*\*ATT\&CK Technique:\*\* T1053.005

\- \*\*Delivery Method:\*\* PowerShell execution on Trinity

\- \*\*YARA Rule Written:\*\* Yes — see YARA\_RULES.md (Scheduled\_Task\_Persistence)

\- \*\*Sigma Rule Written:\*\* No



\### Infrastructure

\- \*\*Attack Origin:\*\* Trinity VM — 192.168.161.128

\- \*\*Redirector Used:\*\* No

\- \*\*C2 Channel:\*\* Local Atomic Red Team execution

\- \*\*TLS Fingerprint (JA4):\*\* \[Capture during execution]



\### Victim

\- \*\*Target Machine:\*\* Sentinel

\- \*\*Target Service:\*\* Windows Task Scheduler

\- \*\*Impact:\*\* \[To be completed after execution]

\- \*\*Detected by Seraph:\*\* \[To be completed]

\- \*\*Detection Rule Triggered:\*\* \[To be completed]



\### IoCs Generated

| Type | Value | Notes |

|---|---|---|

| Process name | schtasks.exe | Task creation |

| Registry key | HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Schedule | Persistence location |

| Command line | schtasks /create | Task creation command |



\### MISP Event

\- \*\*Logged to MISP:\*\* No (pending Neb build)

\- \*\*Event ID:\*\* PT-006

\- \*\*Tags:\*\* tlp:white, mitre-attack:T1053.005, purple-team



\### Analyst Notes

\[To be completed after execution — document persistence mechanism, detection gaps, and remediation steps]



\---



\## Event PT-007 — T1562.001 Disable or Modify Tools



\*\*Date:\*\* \[To be completed]

\*\*ATT\&CK Technique:\*\* T1562.001 — Disable or Modify Tools

\*\*Phase:\*\* Phase 2

\*\*Tool:\*\* Invoke-AtomicRedTeam / PowerShell



\### Adversary

\- \*\*Simulated Actor:\*\* APT28 / Red Team operator

\- \*\*Intent:\*\* Disable security tools on Sentinel to blind Seraph and enable follow-on activity

\- \*\*Sophistication:\*\* Nation-state



\### Capability

\- \*\*Tool Used:\*\* Invoke-AtomicRedTeam, PowerShell

\- \*\*ATT\&CK Technique:\*\* T1562.001

\- \*\*Delivery Method:\*\* PowerShell execution on Trinity

\- \*\*YARA Rule Written:\*\* No

\- \*\*Sigma Rule Written:\*\* No



\### Infrastructure

\- \*\*Attack Origin:\*\* Trinity VM — 192.168.161.128

\- \*\*Redirector Used:\*\* No

\- \*\*C2 Channel:\*\* Local Atomic Red Team execution

\- \*\*TLS Fingerprint (JA4):\*\* \[Capture during execution]



\### Victim

\- \*\*Target Machine:\*\* Sentinel

\- \*\*Target Service:\*\* Windows Defender / Wazuh agent

\- \*\*Impact:\*\* \[To be completed after execution]

\- \*\*Detected by Seraph:\*\* \[To be completed]

\- \*\*Detection Rule Triggered:\*\* \[To be completed]



\### IoCs Generated

| Type | Value | Notes |

|---|---|---|

| Process name | powershell.exe | Defense evasion tool |

| Command line | Set-MpPreference -DisableRealtimeMonitoring | Defender disable |

| Event ID | 5001 | Windows Defender disabled |



\### MISP Event

\- \*\*Logged to MISP:\*\* No (pending Neb build)

\- \*\*Event ID:\*\* PT-007

\- \*\*Tags:\*\* tlp:white, mitre-attack:T1562.001, purple-team



\### Analyst Notes

\[To be completed after execution — this technique should trigger immediate Seraph alert. Document whether detection fires correctly]



\---



\## Phase 2 Summary



| Event | Technique | Tool | Detected | YARA | MISP |

|---|---|---|---|---|---|

| PT-005 | T1003.001 | Mimikatz | Pending | Yes | Pending |

| PT-006 | T1053.005 | schtasks.exe | Pending | Yes | Pending |

| PT-007 | T1562.001 | PowerShell | Pending | No | Pending |



\*\*Overall Detection Rate: Pending\*\*



\*\*Priority Actions:\*\*

\- \[ ] Execute T1003 on Trinity against Sentinel

\- \[ ] Execute T1053.005 on Trinity against Sentinel

\- \[ ] Execute T1562.001 on Trinity against Sentinel

\- \[ ] Capture JA4 fingerprints during all executions

\- \[ ] Complete all Diamond Model writeups after execution

\- \[ ] Log all IoCs to MISP once Seraph is deployed on Neb

\- \[ ] Update ATT\&CK Navigator layer with Phase 2 techniques

\- \[ ] Pivot to Morpheus DC for Phase 3

