# CIS 2352 - Ethical Hacking: Lab Guide
**Author:** Jarron Jackson | **Lab:** Matrix Homelab | **Semester:** Fall 2026

---

## Lab 1 - OpenVAS Reconnaissance of Sentinel

### What You Will Do
Run professional vulnerability scan of Sentinel before exploitation. Run unauthenticated (black-box) and authenticated (grey-box) scans. Compare results. Map findings to planned ATT&CK techniques.

### Skills Learned
- Pre-exploitation reconnaissance methodology
- Scan type selection (black-box vs grey-box)
- Finding-to-technique mapping
- Exploitation feasibility assessment

### Purple Team Relevance
OpenVAS findings answer which T1003 variant is most viable against Sentinel. Professional pentesters never exploit blind - they scan first.

### Artifact
labs/cis2352/openvas-preexploit-recon.md

---

## Lab 2 - Phase 2 Exploitation Chain (Trinity to Sentinel)

### What You Will Do

T1003 - Credential Dumping:
- Attempt LSASS memory dump via Task Manager
- Attempt via Mimikatz if Defender allows
- Document Windows Defender response
- Log outcome in VECTR

T1053.005 - Scheduled Task Persistence:
- Create scheduled task on Sentinel via schtasks
- Document task created, trigger, and action
- Verify persistence survives reboot
- Log outcome in VECTR

T1562.001 - Disable Security Tools:
- Attempt to stop Windows Defender service
- Attempt to disable Windows Firewall
- Document what Defender catches vs misses
- Log outcome in VECTR

### Skills Learned
- Cross-machine attack execution
- Credential dumping techniques and countermeasures
- Persistence mechanism deployment
- Security tool evasion/bypass concepts
- Professional engagement documentation

### Purple Team Relevance
Cross-machine attacks demonstrate lateral movement understanding - a core purple team skill. Windows Defender will likely block some techniques, producing Blocked outcomes in VECTR which is more interesting than all-None.

### Artifacts
purple-team/T1003-credential-dumping.md
purple-team/T1053.005-scheduled-task-persistence.md
purple-team/T1562.001-disable-security-tools.md

### NIST CSF
ID.RA-1, DE.AE-2, RS.AN-2

---

## Lab 3 - Pentest Methodology Documentation

### What You Will Do
Frame the full engagement (Phase 1 and Phase 2) in a professional pentest report structure using VECTR output as the evidence base.

Report structure:
- Executive summary (non-technical, risk-focused)
- Scope and methodology
- Findings by severity
- Evidence (VECTR outcomes, command output, screenshots)
- Remediation recommendations
- Appendix (full technique list with ATT&CK IDs)

### Artifact
labs/cis2352/pentest-report-phase1-phase2.md

---

## Lab 4 - CALDERA Automated Attack Chains

### What You Will Do
Automate the full discovery chain in CALDERA. Build adversary profile that chains T1087.001 to T1057 to T1082 to T1049 and deploy against Sentinel automatically. Compare manual vs automated outcomes in VECTR.

### Artifact
labs/cis2352/caldera-automated-chains.md

### NIST CSF
DE.AE-2, RS.AN-1
