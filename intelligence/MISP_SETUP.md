\# MISP — Malware Information Sharing Platform



MISP is an open-source threat intelligence platform used by the FBI, CISA, and private threat intel firms to collect, store, and share Indicators of Compromise (IoCs). This file documents the MISP deployment plan and IoC logging workflow for the Matrix Homelab intelligence layer.



\---



\## What is MISP



MISP is the platform threat intelligence teams use to:

\- Log and track IoCs (file hashes, IPs, domains, registry keys)

\- Tag indicators with MITRE ATT\&CK techniques

\- Share threat intelligence with partner organizations

\- Build threat actor profiles from accumulated IoC data



When the FBI shares threat intelligence with private sector partners after a nation-state intrusion, it often comes packaged as a MISP event feed.



\---



\## Deployment Plan



MISP will run as a VM on Neb (Seraph node) once hardware is built.



\*\*VM Specs:\*\*

\- 4GB RAM minimum (8GB recommended)

\- 50GB storage

\- Ubuntu 22.04 LTS

\- Accessible at http://192.168.x.x on home network



\*\*Until Neb is built:\*\*

\- Log IoCs manually in the IoC tracking table below

\- Use MISP Online Demo at https://misp-project.org/demo/ for familiarization



\---



\## Install MISP on Ubuntu (Seraph VM)



```bash

\# Update system

sudo apt update \&\& sudo apt upgrade -y



\# Install MISP using the official installer

wget -O /tmp/INSTALL.sh https://raw.githubusercontent.com/MISP/MISP/2.4/INSTALL/INSTALL.sh

bash /tmp/INSTALL.sh

```



Access MISP at: `https://YOUR-SERAPH-IP`

Default credentials: `admin@admin.test / admin`



\---



\## IoC Taxonomy — What to Log



| IoC Type | Example | MISP Category |

|---|---|---|

| File hash (MD5) | d41d8cd98f00b204e9800998ecf8427e | Payload delivery |

| File hash (SHA256) | e3b0c44298fc1c149afb... | Payload delivery |

| IP address | 192.168.161.128 | Network activity |

| Domain | evil.c2.domain.com | Network activity |

| Registry key | HKLM\\Software\\Microsoft\\... | Persistence |

| Process name | lsass.exe | Payload delivery |

| Mutex | Global\\MimikatzMutex | Payload delivery |

| YARA rule | Mimikatz\_Strings | External analysis |

| JA3 hash | 72a7c13520dc9f5035... | Network activity |



\---



\## IoC Log — Manual Tracking (Pre-Neb)



Document all IoCs generated during lab simulations here until MISP is deployed:



| Date | Phase | ATT\&CK Technique | IoC Type | Value | Tool Source | MISP Logged |

|---|---|---|---|---|---|---|

| | Phase 1 | T1087.001 | Process name | net.exe | Atomic Red Team | No |

| | Phase 1 | T1057 | Process name | tasklist.exe | Atomic Red Team | No |

| | Phase 1 | T1082 | Registry key | HKLM\\SYSTEM\\... | Atomic Red Team | No |

| | Phase 1 | T1049 | Process name | netstat.exe | Atomic Red Team | No |



\---



\## MISP Event Structure



Every purple team simulation generates one MISP event:



```

Event Title: \[Phase X] — \[ATT\&CK Technique] — \[Date]

Example: \[Phase 2] — T1003.001 LSASS Credential Dump — 2026-07-08



Tags:

\- mitre-attack:T1003.001

\- tlp:white

\- purple-team

\- homelab



Attributes:

\- File hashes of tools used

\- Registry keys modified

\- Process names involved

\- IP addresses of attack origin

\- JA3/JA4 fingerprints captured

\- YARA rule reference

```



\---



\## MISP Feeds to Subscribe To



Once MISP is deployed on Seraph, subscribe to these free threat intel feeds:



| Feed | URL | Content |

|---|---|---|

| CIRCL OSINT | https://www.circl.lu/doc/misp/feed-osint/ | General threat intel |

| Abuse.ch | https://abuse.ch | Malware hashes and C2 IPs |

| AlienVault OTX | https://otx.alienvault.com | Community threat intel |

| CISA Known Exploited | https://www.cisa.gov/known-exploited-vulnerabilities-catalog | KEV catalog |



\---



\## Workflow — Per Attack Simulation



1\. Run attack simulation on Trinity against Sentinel

2\. Collect all artifacts (hashes, keys, IPs, process names)

3\. Create new MISP event with ATT\&CK technique tag

4\. Add all IoCs as attributes to the event

5\. Reference YARA rule written for this technique

6\. Reference Diamond Model writeup for this event

7\. Tag with TLP:WHITE for homelab sharing

8\. Update IoC log table above



\---



\## Resources



\- MISP Project: https://misp-project.org

\- MISP GitHub: https://github.com/MISP/MISP

\- MISP Training: https://www.misp-project.org/misp-training/

\- ATT\&CK Taxonomy for MISP: https://github.com/MISP/misp-galaxy

