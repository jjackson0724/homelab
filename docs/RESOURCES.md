\# Learning Resources \& Study Tools



Documentation of tools, platforms, and resources used for skill development, retention, and portfolio building across the Matrix Homelab project.



\---



\## AI-Powered Study Tools



\### Google NotebookLM

\*\*URL:\*\* https://notebooklm.google.com

\*\*Cost:\*\* Free

\*\*What it is:\*\* AI research and study tool that ingests your own documents and generates personalized learning content from them.



\*\*How it's used in this lab:\*\*

\- Upload all homelab markdown files as sources

\- Generate podcast-style Audio Overview covering lab architecture, purple team pipeline, intelligence layer, and career context

\- Generate Flashcards for Security+ and ISC2 cert prep based on actual lab content

\- Generate Quiz questions for self-assessment before exams

\- Generate Mind Map showing relationships between Diamond Model, YARA, MISP, and JA4

\- Generate Slide Deck for Black Hat presentations

\- Chat with your own documentation for instant clarification on any topic



\*\*Why this works for retention:\*\*

Hearing your own lab discussed in conversational audio format reinforces concepts differently than reading. Every concept is anchored to real lab work you've done, making retention significantly more effective than studying generic material.



\*\*Sources uploaded:\*\*

\- README.md

\- NEB\_BUILD.md

\- SKILLS\_ROADMAP.md

\- PHASE1\_DIAMOND.md

\- PHASE2\_DIAMOND.md

\- intelligence/DIAMOND\_MODEL\_TEMPLATE.md

\- intelligence/YARA\_RULES.md

\- intelligence/JA4\_FINGERPRINTING.md

\- intelligence/MISP\_SETUP.md

\- purple-team/OPSEC\_INFRASTRUCTURE.md

\- purple-team/ATTACK\_NAVIGATOR\_GUIDE.md

\- ZION\_Hardening\_Report.md

\- Individual SKILL.md files per technique



\*\*Studio features available:\*\*

| Feature | Use Case |

|---|---|

| Audio Overview | Commute study — full lab podcast |

| Video | Short video overviews (beta) |

| Flashcards | Cert prep — Security+, ISC2 |

| Quiz | Self assessment before exams |

| Mind Map | Visual concept relationships |

| Slide Deck | Black Hat presentation material |

| Reports | Structured written summaries |

| Infographic | Visual lab overview (beta) |

| Data Table | Organized reference data |



\---



\## Local AI Tools



\### skill\_query.py + Ollama

\*\*Location:\*\* `scripts/skill\_query.py`

\*\*Model:\*\* Llama 3.2 (local, no internet required)

\*\*What it does:\*\* Queries 754 structured cybersecurity skills via local LLM — loads any skill's SKILL.md as context and answers questions about it



\*\*How to use for cert prep:\*\*

```bash

py scripts/skill\_query.py

\# Search for relevant skill

\# Ask: "explain this to me for Security+ exam prep"

\# Ask: "quiz me on this topic"

\# Ask: "how does this map to NIST CSF"

```



\*\*Skills installed at:\*\* `C:\\Users\\Jarron\\.claude\\skills\\cybersecurity`

\*\*Total skills:\*\* 754 — mapped to MITRE ATT\&CK, NIST CSF, D3FEND, MITRE ATLAS, NIST AI RMF



\---



\## Hands-On Practice Platforms



\### TryHackMe

\*\*URL:\*\* https://tryhackme.com

\*\*Handle:\*\* P3rplex.Actual

\*\*Cost:\*\* Free tier + optional subscription

\*\*Use:\*\* Guided labs for Security+ domains, hands-on technique practice



\### VECTR Community Edition

\*\*URL:\*\* https://vectr.io

\*\*Instance:\*\* https://sravectr.internal:8081 (Zion)

\*\*Use:\*\* Purple team engagement tracking, before/after detection heatmaps, threat resilience scoring



\### MITRE ATT\&CK Navigator

\*\*URL:\*\* https://mitre-attack.github.io/attack-navigator/

\*\*Use:\*\* Build and maintain heatmap of completed techniques, visualize defensive gaps



\---



\## Video Learning



\### Professor Messer Security+

\*\*URL:\*\* https://www.professormesser.com

\*\*Cost:\*\* Free on YouTube

\*\*Use:\*\* Security+ exam prep — aligned exactly to exam objectives



\### Antisyphon Training

\*\*Active Defense \& Cyber Deception\*\* — John Strand (June 29 — July 2)

\*\*AI Security Agents\*\* — Faan Rossouw (June 12, recording access 6 months)



\---



\## Reference Frameworks



| Framework | URL | Use |

|---|---|---|

| MITRE ATT\&CK | https://attack.mitre.org | Technique mapping |

| NIST CSF | https://www.nist.gov/cyberframework | Control mapping |

| D3FEND | https://d3fend.mitre.org | Defensive technique mapping |

| MITRE ATLAS | https://atlas.mitre.org | AI threat mapping |

| OWASP | https://owasp.org | Web app security reference |



\---



\## Community \& Networking



\### Discord Servers

\- \*\*Black Hills Information Security (BHIS)\*\* — John Strand's company, Active Defense course community

\- \*\*John Hammond\*\* — CTFs and hands-on learning

\- \*\*NahamSec\*\* — Bug bounty, recon, offensive security

\- \*\*TCM Security\*\* — Penetration testing and certifications



\### Conferences

\- \*\*Black Hat USA 2026\*\* — Aug 3-7, Planet Hollywood Las Vegas (scholarship recipient)

\- \*\*BSides Las Vegas 2026\*\* — $35 student ticket

\- \*\*DEF CON\*\* — Runs same week as Black Hat



\---



\## Certification Roadmap



| Cert | Status | Target |

|---|---|---|

| CompTIA Security+ | In progress | 2026 |

| ISC2 CC | In progress | 2026 |

| PNPT (TCM Security) | Planned | Post B.A.S. |

| OSCP | Planned | Long term |



\---



\## Retention Strategy



The core retention approach for this lab is \*\*context-anchored learning\*\* — every concept studied is immediately tied to a real implementation in the homelab:



1\. \*\*Study the concept\*\* — Professor Messer, TryHackMe, skill\_query.py

2\. \*\*Implement it\*\* — Run the attack or deploy the control in the lab

3\. \*\*Document it\*\* — Diamond Model writeup, YARA rule, MISP IoC

4\. \*\*Reinforce it\*\* — NotebookLM audio, flashcards, quiz

5\. \*\*Commit it\*\* — Push to GitHub as portfolio evidence



Isolated facts don't stick. Experiences do.

