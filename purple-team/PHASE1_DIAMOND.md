\# Phase 1 — Diamond Model Writeups



\## Phase 1 Overview

Establish lab environment, harden endpoints, and baseline normal network behavior. Simulate how nation-state actors conduct initial reconnaissance before touching a target.



\*\*Techniques completed:\*\*

\- T1087.001 — Local Account Discovery

\- T1057 — Process Discovery

\- T1082 — System Information Discovery

\- T1049 — System Network Connections Discovery



\*\*Attack origin:\*\* Trinity (Kali Linux) — 192.168.161.128

\*\*Target:\*\* Sentinel — 192.168.161.0/24

\*\*Documented in VECTR:\*\* Home\_LAB environment

\*\*Threat Resilience Score:\*\* 0.00%



\---



\## Event PT-001 — T1087.001 Local Account Discovery



\*\*Date:\*\* 2026

\*\*ATT\&CK Technique:\*\* T1087.001 — Local Account Discovery

\*\*Phase:\*\* Phase 1

\*\*Tool:\*\* Invoke-AtomicRedTeam / net user



\### Adversary

\- \*\*Simulated Actor:\*\* Generic APT / Red Team operator

\- \*\*Intent:\*\* Enumerate local accounts to identify high-value targets for privilege escalation

\- \*\*Sophistication:\*\* Nation-state / Criminal



\### Capability

\- \*\*Tool Used:\*\* Invoke-AtomicRedTeam, net.exe

\- \*\*ATT\&CK Technique:\*\* T1087.001

\- \*\*Delivery Method:\*\* PowerShell execution on Trinity

\- \*\*YARA Rule Written:\*\* No

\- \*\*Sigma Rule Written:\*\* No



\### Infrastructure

\- \*\*Attack Origin:\*\* Trinity VM — 192.168.161.128

\- \*\*Redirector Used:\*\* No

\- \*\*C2 Channel:\*\* Local Atomic Red Team execution

\- \*\*TLS Fingerprint (JA4):\*\* Not captured



\### Victim

\- \*\*Target Machine:\*\* Sentinel

\- \*\*Target Service:\*\* Local account database

\- \*\*Impact:\*\* Local accounts enumerated

\- \*\*Detected by Seraph:\*\* No

\- \*\*Detection Rule Triggered:\*\* None



\### IoCs Generated

| Type | Value | Notes |

|---|---|---|

| Process name | net.exe | Account enumeration |

| Command line | net user | Discovery command |



\### MISP Event

\- \*\*Logged to MISP:\*\* No (pending Neb build)

\- \*\*Event ID:\*\* PT-001

\- \*\*Tags:\*\* tlp:white, mitre-attack:T1087.001, purple-team



\### Analyst Notes

Detection gap identified — Seraph did not alert on local account enumeration. Detection rule needed for net.exe execution with user enumeration arguments.



\---



\## Event PT-002 — T1057 Process Discovery



\*\*Date:\*\* 2026

\*\*ATT\&CK Technique:\*\* T1057 — Process Discovery

\*\*Phase:\*\* Phase 1

\*\*Tool:\*\* Invoke-AtomicRedTeam / tasklist



\### Adversary

\- \*\*Simulated Actor:\*\* Generic APT / Red Team operator

\- \*\*Intent:\*\* Enumerate running processes to identify security tools and high-value targets

\- \*\*Sophistication:\*\* Nation-state / Criminal



\### Capability

\- \*\*Tool Used:\*\* Invoke-AtomicRedTeam, tasklist.exe

\- \*\*ATT\&CK Technique:\*\* T1057

\- \*\*Delivery Method:\*\* PowerShell execution on Trinity

\- \*\*YARA Rule Written:\*\* No

\- \*\*Sigma Rule Written:\*\* No



\### Infrastructure

\- \*\*Attack Origin:\*\* Trinity VM — 192.168.161.128

\- \*\*Redirector Used:\*\* No

\- \*\*C2 Channel:\*\* Local Atomic Red Team execution

\- \*\*TLS Fingerprint (JA4):\*\* Not captured



\### Victim

\- \*\*Target Machine:\*\* Sentinel

\- \*\*Target Service:\*\* Process list

\- \*\*Impact:\*\* Running processes enumerated including security tools

\- \*\*Detected by Seraph:\*\* No

\- \*\*Detection Rule Triggered:\*\* None



\### IoCs Generated

| Type | Value | Notes |

|---|---|---|

| Process name | tasklist.exe | Process enumeration |

| Command line | tasklist /v | Verbose process list |



\### MISP Event

\- \*\*Logged to MISP:\*\* No (pending Neb build)

\- \*\*Event ID:\*\* PT-002

\- \*\*Tags:\*\* tlp:white, mitre-attack:T1057, purple-team



\### Analyst Notes

Detection gap identified — process enumeration went undetected. Wazuh rule needed for tasklist.exe execution in non-admin context.



\---



\## Event PT-003 — T1082 System Information Discovery



\*\*Date:\*\* 2026

\*\*ATT\&CK Technique:\*\* T1082 — System Information Discovery

\*\*Phase:\*\* Phase 1

\*\*Tool:\*\* Invoke-AtomicRedTeam / systeminfo



\### Adversary

\- \*\*Simulated Actor:\*\* Generic APT / Red Team operator

\- \*\*Intent:\*\* Collect system information for target profiling and vulnerability identification

\- \*\*Sophistication:\*\* Nation-state / Criminal



\### Capability

\- \*\*Tool Used:\*\* Invoke-AtomicRedTeam, systeminfo.exe

\- \*\*ATT\&CK Technique:\*\* T1082

\- \*\*Delivery Method:\*\* PowerShell execution on Trinity

\- \*\*YARA Rule Written:\*\* No

\- \*\*Sigma Rule Written:\*\* No



\### Infrastructure

\- \*\*Attack Origin:\*\* Trinity VM — 192.168.161.128

\- \*\*Redirector Used:\*\* No

\- \*\*C2 Channel:\*\* Local Atomic Red Team execution

\- \*\*TLS Fingerprint (JA4):\*\* Not captured



\### Victim

\- \*\*Target Machine:\*\* Sentinel

\- \*\*Target Service:\*\* System configuration

\- \*\*Impact:\*\* OS version, patch level, and hardware info collected

\- \*\*Detected by Seraph:\*\* No

\- \*\*Detection Rule Triggered:\*\* None



\### IoCs Generated

| Type | Value | Notes |

|---|---|---|

| Process name | systeminfo.exe | System enumeration |

| Command line | systeminfo | Full system info dump |



\### MISP Event

\- \*\*Logged to MISP:\*\* No (pending Neb build)

\- \*\*Event ID:\*\* PT-003

\- \*\*Tags:\*\* tlp:white, mitre-attack:T1082, purple-team



\### Analyst Notes

Detection gap identified — system information collection went undetected. Low priority detection but should be correlated with other discovery techniques for chained detection.



\---



\## Event PT-004 — T1049 System Network Connections Discovery



\*\*Date:\*\* 2026

\*\*ATT\&CK Technique:\*\* T1049 — System Network Connections Discovery

\*\*Phase:\*\* Phase 1

\*\*Tool:\*\* Invoke-AtomicRedTeam / netstat



\### Adversary

\- \*\*Simulated Actor:\*\* Generic APT / Red Team operator

\- \*\*Intent:\*\* Map active network connections to identify lateral movement opportunities

\- \*\*Sophistication:\*\* Nation-state / Criminal



\### Capability

\- \*\*Tool Used:\*\* Invoke-AtomicRedTeam, netstat.exe

\- \*\*ATT\&CK Technique:\*\* T1049

\- \*\*Delivery Method:\*\* PowerShell execution on Trinity

\- \*\*YARA Rule Written:\*\* No

\- \*\*Sigma Rule Written:\*\* No



\### Infrastructure

\- \*\*Attack Origin:\*\* Trinity VM — 192.168.161.128

\- \*\*Redirector Used:\*\* No

\- \*\*C2 Channel:\*\* Local Atomic Red Team execution

\- \*\*TLS Fingerprint (JA4):\*\* Not captured



\### Victim

\- \*\*Target Machine:\*\* Sentinel

\- \*\*Target Service:\*\* Network connection table

\- \*\*Impact:\*\* Active connections and listening ports enumerated

\- \*\*Detected by Seraph:\*\* No

\- \*\*Detection Rule Triggered:\*\* None



\### IoCs Generated

| Type | Value | Notes |

|---|---|---|

| Process name | netstat.exe | Network enumeration |

| Command line | netstat -ano | All connections with PIDs |



\### MISP Event

\- \*\*Logged to MISP:\*\* No (pending Neb build)

\- \*\*Event ID:\*\* PT-004

\- \*\*Tags:\*\* tlp:white, mitre-attack:T1049, purple-team



\### Analyst Notes

Detection gap identified — network connection enumeration went undetected. Should be correlated with T1087 and T1057 for chained discovery detection rule in Wazuh.



\---



\## Phase 1 Summary



| Event | Technique | Tool | Detected | YARA | MISP |

|---|---|---|---|---|---|

| PT-001 | T1087.001 | net.exe | No | No | Pending |

| PT-002 | T1057 | tasklist.exe | No | No | Pending |

| PT-003 | T1082 | systeminfo.exe | No | No | Pending |

| PT-004 | T1049 | netstat.exe | No | No | Pending |



\*\*Overall Detection Rate: 0%\*\*



\*\*Priority Actions:\*\*

\- \[ ] Write Wazuh detection rules for all four techniques

\- \[ ] Write Sigma rules for chained discovery detection

\- \[ ] Log all IoCs to MISP once Seraph is deployed on Neb

\- \[ ] Capture JA4 fingerprints during Phase 2 simulations

\- \[ ] Update ATT\&CK Navigator layer with Phase 1 techniques

