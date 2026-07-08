\# ATT\&CK Navigator — Heatmap Guide



The MITRE ATT\&CK Navigator is a free web-based tool used by CIA briefers and threat intelligence analysts to visually demonstrate defensive gaps and attack coverage to decision-makers. This file documents how to build and maintain your ATT\&CK Navigator layer for the Matrix Homelab purple team engagement.



\---



\## What is ATT\&CK Navigator



ATT\&CK Navigator is a heatmap visualization tool that maps techniques onto the MITRE ATT\&CK framework matrix. Each technique can be colored to show:



\- \*\*Red\*\* — Technique simulated, not detected (gap)

\- \*\*Green\*\* — Technique simulated, detected successfully

\- \*\*Yellow\*\* — Technique simulated, partially detected

\- \*\*Blue\*\* — Technique in scope but not yet simulated



When you show this heatmap to a hiring manager at CrowdStrike or Mandiant, they immediately see the depth and structure of your purple team engagement.



\---



\## Access ATT\&CK Navigator



Free web tool — no install required:

\- \*\*Online:\*\* https://mitre-attack.github.io/attack-navigator/

\- \*\*Local:\*\* Clone and run locally for offline use



```bash

git clone https://github.com/mitre-attack/attack-navigator.git

cd attack-navigator/nav-app

npm install

npm start

```



Access at: http://localhost:4200



\---



\## Creating Your Layer



\### Step 1 — Open Navigator

Go to https://mitre-attack.github.io/attack-navigator/



\### Step 2 — Create New Layer

\- Click \*\*Create New Layer\*\*

\- Select \*\*Enterprise ATT\&CK\*\*

\- Select latest version



\### Step 3 — Add Your Techniques



For each completed technique:

1\. Search for the technique ID in the search bar

2\. Click the technique to select it

3\. Right click → \*\*Add to selection\*\*

4\. Assign a color based on detection status



\### Step 4 — Color Coding



Use this consistent color scheme:



| Color | Hex | Meaning |

|---|---|---|

| Red | #ff0000 | Simulated — not detected |

| Green | #00ff00 | Simulated — detected |

| Yellow | #ffff00 | Simulated — partially detected |

| Blue | #0000ff | Planned — not yet simulated |

| Matrix Green | #00ff88 | Completed with full intelligence writeup |



\---



\## Current Layer Status



\### Phase 1 — Completed (use Red — not detected)



| Technique ID | Name | Status | Detection |

|---|---|---|---|

| T1087.001 | Local Account Discovery | Complete | Not detected |

| T1057 | Process Discovery | Complete | Not detected |

| T1082 | System Information Discovery | Complete | Not detected |

| T1049 | System Network Connections Discovery | Complete | Not detected |



\### Phase 2 — Planned (use Blue — not yet simulated)



| Technique ID | Name | Status | Detection |

|---|---|---|---|

| T1003.001 | LSASS Memory | Planned | Pending |

| T1053.005 | Scheduled Task | Planned | Pending |

| T1562.001 | Disable or Modify Tools | Planned | Pending |



\### Phase 3 — Planned



| Technique ID | Name | Status | Detection |

|---|---|---|---|

| T1021.002 | SMB/Windows Admin Shares | Planned | Pending |

| T1047 | WMI | Planned | Pending |

| T1550.002 | Pass the Hash | Planned | Pending |

| T1027 | Obfuscated Files or Information | Planned | Pending |



\### Phase 4 — Planned



| Technique ID | Name | Status | Detection |

|---|---|---|---|

| T1558.003 | Kerberoasting | Planned | Pending |

| T1003.006 | DCSync | Planned | Pending |

| T1484.001 | Group Policy Modification | Planned | Pending |

| T1207 | Rogue Domain Controller | Planned | Pending |



\---



\## Exporting Your Layer



\### Export as JSON

1\. Click the download icon in Navigator

2\. Select \*\*Layer JSON\*\*

3\. Save as `attack\_navigator\_layer.json`

4\. Commit to `/purple-team/` folder in GitHub



\### Export as SVG Image

1\. Click the download icon

2\. Select \*\*SVG\*\*

3\. Save as `attack\_navigator\_heatmap.svg`

4\. Embed in README.md



\### Embed in README.md

```markdown

\## ATT\&CK Coverage Heatmap

!\[ATT\&CK Navigator Heatmap](purple-team/attack\_navigator\_heatmap.svg)

```



\---



\## Updating Your Layer



Update your Navigator layer after every purple team phase:



1\. Open your saved layer JSON in Navigator

2\. Add newly completed techniques

3\. Update colors based on detection results

4\. Export updated SVG and JSON

5\. Commit both files to GitHub

6\. Update README.md embed



\---



\## How to Present This at Black Hat



When talking to threat intel or purple team hiring managers:



1\. Pull up your GitHub on your phone

2\. Show the ATT\&CK Navigator heatmap embedded in README.md

3\. Walk through the red techniques — "these are gaps I identified and am building detections for"

4\. Walk through any green techniques — "these are techniques Seraph caught and I documented with YARA rules and Diamond Model writeups"

5\. Reference the intelligence layer — "every red technique has a corresponding Diamond Model writeup, YARA rule, and IoC logged in MISP"



That five minute conversation gets you remembered.



\---



\## Resources



\- ATT\&CK Navigator: https://mitre-attack.github.io/attack-navigator/

\- ATT\&CK GitHub: https://github.com/mitre-attack/attack-navigator

\- ATT\&CK Enterprise Matrix: https://attack.mitre.org/matrices/enterprise/

\- Navigator Layer Format: https://github.com/mitre-attack/attack-navigator/blob/master/LAYER\_FORMAT.md



\---



\## Status



\- \[ ] Navigator account created

\- \[ ] Phase 1 techniques added and colored red

\- \[ ] Phase 2 techniques added and colored blue

\- \[ ] Layer JSON exported and committed to GitHub

\- \[ ] SVG heatmap exported and embedded in README.md

\- \[ ] Layer updated after each phase completion

