\# Diamond Model of Intrusion Analysis — Template



The Diamond Model is a framework used by intelligence agencies including the FBI Cyber Division and CIA to analyze and attribute cyber intrusions. Every intrusion event has four core features connected at the vertices of a diamond.



\---



\## The Four Vertices



| Vertex | Definition | Example |

|---|---|---|

| \*\*Adversary\*\* | The threat actor behind the intrusion | APT28, Lazarus Group, insider threat |

| \*\*Capability\*\* | The tools, malware, or TTPs used | Mimikatz, Cobalt Strike, custom binary |

| \*\*Infrastructure\*\* | The systems used to conduct the attack | C2 server, redirector VM, phishing domain |

| \*\*Victim\*\* | The target of the intrusion | Sentinel machine, Morpheus domain controller |



\---



\## Meta-Features



| Meta-Feature | Description |

|---|---|

| \*\*Timestamp\*\* | When the event occurred |

| \*\*Phase\*\* | Which kill chain phase (recon, exploit, persist, exfil) |

| \*\*Result\*\* | Success, failure, or unknown |

| \*\*Direction\*\* | Adversary-to-Infrastructure, Infrastructure-to-Victim |

| \*\*Methodology\*\* | How the capability was delivered |

| \*\*Resources\*\* | What the adversary needed (tools, knowledge, access) |



\---



\## Diamond Model — Filled Template



\*\*Event ID:\*\* \[e.g. PT-001]  

\*\*Date:\*\* \[YYYY-MM-DD]  

\*\*MITRE ATT\&CK Technique:\*\* \[e.g. T1003.001 — LSASS Memory]  

\*\*Phase:\*\* \[Phase 1 / 2 / 3 / 4]



\---



\### Adversary

\- \*\*Simulated Actor:\*\* \[e.g. APT28 / Red Team operator]

\- \*\*Intent:\*\* \[e.g. credential theft for lateral movement]

\- \*\*Sophistication:\*\* \[Nation-state / Criminal / Insider]



\---



\### Capability

\- \*\*Tool Used:\*\* \[e.g. Mimikatz, Invoke-AtomicRedTeam]

\- \*\*ATT\&CK Technique:\*\* \[e.g. T1003.001]

\- \*\*Delivery Method:\*\* \[e.g. PowerShell execution on Trinity]

\- \*\*YARA Rule Written:\*\* \[Yes / No — link if yes]

\- \*\*Sigma Rule Written:\*\* \[Yes / No — link if yes]



\---



\### Infrastructure

\- \*\*Attack Origin:\*\* \[e.g. Trinity VM — 192.168.161.128]

\- \*\*Redirector Used:\*\* \[Yes / No]

\- \*\*C2 Channel:\*\* \[e.g. Atomic Red Team local / Sliver / Cobalt Strike]

\- \*\*TLS Fingerprint (JA4):\*\* \[if captured]



\---



\### Victim

\- \*\*Target Machine:\*\* \[e.g. Sentinel — 192.168.161.x]

\- \*\*Target Service:\*\* \[e.g. LSASS process]

\- \*\*Impact:\*\* \[e.g. NTLM hashes extracted]

\- \*\*Detected by Seraph:\*\* \[Yes / No]

\- \*\*Detection Rule Triggered:\*\* \[e.g. Wazuh rule 87002]



\---



\### IoCs Generated



| Type | Value | Notes |

|---|---|---|

| File hash | \[SHA256] | Tool binary |

| Registry key | \[path] | Persistence artifact |

| IP address | \[192.168.x.x] | Attack origin |

| Process name | \[e.g. lsass.exe access] | Execution artifact |



\---



\### MISP Event

\- \*\*Logged to MISP:\*\* \[Yes / No]

\- \*\*Event ID:\*\* \[MISP event number]

\- \*\*Tags:\*\* \[e.g. tlp:white, mitre-attack:T1003.001]



\---



\### Analyst Notes

\[Free text — what did you observe, what did you miss, what would a real analyst flag here]



\---



\### ATT\&CK Navigator

\- \*\*Technique highlighted:\*\* \[Yes / No]

\- \*\*Layer file updated:\*\* \[Yes / No — link]

