# Matrix Project: Threat-Informed Purple Team Homelab

**Jarron Jackson** | SPC Cybersecurity A.S. to B.A.S. | Purple Team Operator Track

---

## Operational Metrics

| Metric | Status |
|---|---|
| Degree Progress | A.S. 20% - B.A.S. Planned |
| ATT&CK Techniques Documented | 4 (T1087.001, T1057, T1082, T1049) |
| Portfolio Artifacts Pushed | 8 |
| Active Protective Baselines | 1/4 (Zion hardened) |
| Detection Rules in Production | 0 (Sigma drafts per technique - pending Seraph) |
| VECTR Threat Resilience Score | 0.00% (Phase 1 baseline) |

---

## Infrastructure

| Node | Role | OS | Status |
|---|---|---|---|
| Zion | Hardened Operator Workstation | Windows 11 Home | Production |
| Trinity | Adversary Emulation Platform | Kali Linux 2026.2 | Active |
| Sentinel | Attack Target | Windows 11 | Hardening Pending |
| Nebuchadnezzar | Proxmox Hypervisor | Proxmox VE | Parts Pending |
| Seraph | SIEM / Log Engine | Wazuh + Elastic | Post-Neb |
| Morpheus | Domain Controller | Windows Server + AD | Post-Neb |
| Oracle | AI Inference Node | Ollama / vLLM | Post-Neb |

Full Neb build spec: NEB_BUILD.md

---

## Phase 1 - Baseline and Recon

- [x] Zion OS hardening (VeraCrypt, firewall, UAC, audit logging)
- [x] PCAP baseline analysis - 50k packets, Wireshark/Scapy
- [x] T1087.001 - Local Account Discovery
- [x] T1057 - Process Discovery
- [x] T1082 - System Information Discovery
- [x] T1049 - Network Connection Discovery
- [ ] Sentinel Windows hardening
- [ ] OpenVAS vulnerability scan - Trinity to Sentinel
- [ ] DVWA web app lab (SQLi, XSS, CSRF)
- [ ] iptables hardening - Trinity
- [ ] Password attack labs (John the Ripper, rainbow tables)
- [ ] Network attack labs (ARP poisoning, SYN flood)
- [ ] Rules of Engagement document

Purple team writeups: /purple-team/ | Lab guides: /docs/

---

## Phase 2 - Exploitation

- [ ] T1003 - Credential Dumping (Sentinel)
- [ ] T1053.005 - Scheduled Task Persistence (Sentinel)
- [ ] T1562.001 - Disable Security Tools (Sentinel)
- [ ] Full engagement documented in VECTR
- [ ] Forensic artifact capture during attack chain

---

## Phase 3 - Detection Engineering

- [ ] Seraph deployed on Neb (Wazuh)
- [ ] CALDERA automated attack chains
- [ ] Retest full Phase 1 and 2 chain with detection active
- [ ] Custom Wazuh/Sigma rules per technique
- [ ] VECTR before/after heatmap

---

## Phase 4 - Enterprise Simulation

- [ ] Morpheus domain controller deployed
- [ ] GOAD (Game of Active Directory) attack scenarios
- [ ] Kerberoasting, pass-the-hash, lateral movement
- [ ] IR playbook built from engagement findings
- [ ] SigmaHQ contribution (capstone)

---

## Phase 5 - Infrastructure Hardening

- [ ] OPNsense VM on Neb
- [ ] VLAN segmentation - isolate lab from home network
- [ ] Suricata IDS inside OPNsense
- [ ] Honeypot deployment behind UTM
- [ ] Zeek network monitoring
- [ ] Feed all logs into Seraph

---

## Repository Structure

    homelab/
    purple-team/       ATT&CK technique writeups
    docs/              Lab guides per course and architecture docs
    scripts/           skill_query.py and automation
    NEB_BUILD.md       Nebuchadnezzar hardware spec
    SKILLS_ROADMAP.md  Skill tracking and completion
    README.md          This file

---

## Definition of Done

    [1] Execute    - Run the attack or deploy the control
    [2] Validate   - Confirm in logs, SIEM, or manual observation
    [3] Document   - Write markdown entry in appropriate folder
    [4] Commit     - git add / commit / push to master
