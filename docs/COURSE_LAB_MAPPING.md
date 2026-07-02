# SPC Course → Homelab Mapping
## Matrix Homelab | Purple Team Track
**Author:** Jarron Jackson  
**Updated:** July 2, 2026

---

## Overview

Each course in the SPC Cybersecurity A.S. maps directly to active homelab work. This document tracks the lab project running parallel to each course so classroom theory is immediately applied to real infrastructure.

---

## Summer 2026

### CIS 1358 — Operating System Security

**Course covers:** OS hardening, access controls, security configurations, patch management.

**Lab work:**
- Zion hardening session complete — VeraCrypt FDE, firewall rules, UAC, audit logging, Brave hardening
- Extend by hardening Sentinel using same methodology
- Document each hardening step mapped to NIST CSF control
- Before/after comparison pushed to GitHub

**Portfolio artifact:** Zion hardening report + Sentinel hardening report  
**NIST CSF alignment:** PR.IP-1, PR.AC-1, PR.PT-3  
**Status:** Zion complete. Sentinel pending.

---

## Fall 2026

### CET 1600 — Introduction to Networks

**Course covers:** Network fundamentals, IP addressing, subnetting, protocols.

**Lab work:**
- T1049 network discovery already documented — Trinity at 192.168.161.128, segment /24
- Build full network diagram of lab — Trinity, Sentinel, Zion, Neb
- Document IP assignments, subnets, traffic flows
- When Neb is built, add OPNsense VM and document VLAN segmentation

**Portfolio artifact:** Lab network diagram + VLAN configuration documentation  
**NIST CSF alignment:** ID.AM-3, PR.AC-5  
**Status:** Network discovery complete. Diagram pending.

---

### CTS 1314 — Network Defense/Countermeasures

**Course covers:** Defensive tools, IDS/IPS, firewalls, security monitoring.

**Lab work:**
- This course IS Phase 2 of the purple team roadmap
- Deploy Seraph (Wazuh) on Neb when built
- Configure Wazuh to watch Sentinel
- Write detection rules for each Phase 1 technique (T1087.001, T1057, T1082, T1049, T1003, T1053.005, T1562.001)
- Document each rule against the countermeasure concept from class
- VECTR outcomes updated from None to Alerted/Blocked

**Portfolio artifact:** Wazuh detection rules + VECTR before/after heatmap  
**NIST CSF alignment:** DE.CM-1, DE.CM-7, RS.AN-1  
**Status:** Pending Neb build.

---

### CET 1610 — Switch, Routing, and Wireless Essentials

**Course covers:** VLANs, routing protocols, switching, wireless configuration.

**Lab work:**
- OPNsense VM on Neb — configure inter-VLAN routing
- Set up firewall rules between lab segments
- Isolate Trinity/Sentinel attack traffic from home network via VLAN
- Document traffic flow and routing decisions

**Portfolio artifact:** OPNsense configuration documentation + network topology  
**NIST CSF alignment:** PR.AC-5, PR.PT-4  
**Status:** Pending Neb build.

---

### CET 2691 — Laws & Legal Aspects/IT Security

**Course covers:** CFAA, privacy law, rules of engagement, legal frameworks for security testing.

**Lab work:**
- Write a formal Rules of Engagement (ROE) document for homelab engagements
- Map VECTR engagement reports to legal authorization framework
- Document scope, authorization, and limitations for Trinity → Sentinel attacks
- Research responsible disclosure process for Mad Hat project #20

**Portfolio artifact:** Homelab Rules of Engagement document  
**NIST CSF alignment:** GV.PO-1, GV.OC-1  
**Status:** Pending.

---

### CIS 2352 — Ethical Hacking

**Course covers:** Penetration testing methodology, reconnaissance, exploitation, reporting.

**Lab work:**
- Everything in the purple team attack chain IS this course applied
- Phase 1 complete by course start: T1087.001, T1057, T1082, T1049 (Trinity), T1003, T1053.005, T1562.001 (Sentinel)
- Phase 2 underway: CALDERA automated chains, Wazuh detection
- GitHub repo serves as lab notebook
- VECTR reports serve as professional pentest documentation

**Portfolio artifact:** Full GitHub purple-team/ folder + VECTR engagement reports  
**NIST CSF alignment:** ID.RA-1, DE.AE-2, RS.AN-2  
**Status:** Phase 1 Trinity complete. Sentinel attacks next.

---

## Spring 2027

### CJE 1686 — Forensic Computer Related Crime

**Course covers:** Digital forensics, evidence collection, chain of custody, artifact analysis.

**Lab work:**
- PCAP analysis report (June 27, 2026) already a forensic artifact
- Capture traffic during Sentinel attack chain — what does credential dumping look like on the wire?
- Document Windows event log artifacts created by each ATT&CK technique
- Build forensic artifact reference for T1003, T1053.005, T1562.001
- Chain of custody documentation for evidence handling

**Portfolio artifact:** Forensic artifact catalog per ATT&CK technique + PCAP analysis report  
**NIST CSF alignment:** RS.AN-1, RS.AN-3, DE.AE-3  
**Status:** PCAP baseline complete. Attack artifact documentation pending.

---

### CGS 2811 — Incident Response & Disaster Recovery

**Course covers:** IR lifecycle, containment, eradication, recovery, DR planning.

**Lab work:**
- Build a full IR playbook for the homelab based on Phase 1 techniques
- For each ATT&CK technique: detection step, containment step, eradication step, recovery step
- VECTR heatmap becomes incident evidence exhibit
- This is Mad Hat project #17 (IR playbook + tabletop)
- Map playbook to NIST SP 800-61 IR framework

**Portfolio artifact:** Homelab IR Playbook + VECTR evidence exhibit  
**NIST CSF alignment:** RS.RP-1, RS.CO-1, RC.RP-1  
**Status:** Pending. Attack chain must be complete first.

---

### CTS 2106 — Fundamentals Linux Operating System

**Course covers:** Linux command line, file system, process management, user administration.

**Lab work:**
- All Trinity attack sessions are Linux administration case studies
- Document command output from T1087.001 (user management), T1057 (process management), T1082 (system info), T1049 (networking)
- Write a Linux reference guide based on actual attack commands and their defensive counterparts
- Trinity itself is a living Linux lab

**Portfolio artifact:** Linux command reference built from real attack sessions  
**NIST CSF alignment:** PR.AC-1, PR.IP-1  
**Status:** Content exists across purple team writeups. Consolidation pending.

---

### CTS 2940 — Cybersecurity Internship

**Course covers:** Applied cybersecurity in a professional environment.

**Lab work:**
- GitHub repo, VECTR documentation, and portfolio writeups ARE the internship application
- SigmaHQ contribution (#2) should be complete before this semester
- Target: purple team operator internship or SOC analyst role
- Army veteran status + portfolio depth = strong candidate profile

**Portfolio artifact:** Complete GitHub homelab repo + all project writeups  
**Status:** Build continuously through Fall 2026 and Spring 2027.

---

## Course → Lab Quick Reference

| Semester | Course | Lab Parallel | Phase |
|---|---|---|---|
| Summer 2026 | CIS 1358 OS Security | Sentinel hardening | Phase 1 |
| Fall 2026 | CET 1600 Networks | Lab network diagram | Phase 1/2 |
| Fall 2026 | CTS 1314 Network Defense | Wazuh on Seraph | Phase 2 |
| Fall 2026 | CET 1610 Switching/Routing | OPNsense VLAN config | Phase 2 |
| Fall 2026 | CET 2691 Laws/Legal | ROE document | Phase 1 |
| Fall 2026 | CIS 2352 Ethical Hacking | Full attack chain | Phase 1/2 |
| Spring 2027 | CJE 1686 Forensics | Attack artifact catalog | Phase 2 |
| Spring 2027 | CGS 2811 IR/DR | IR Playbook | Phase 2/3 |
| Spring 2027 | CTS 2106 Linux | Linux reference guide | Phase 1 |
| Spring 2027 | CTS 2940 Internship | Portfolio completion | All phases |
