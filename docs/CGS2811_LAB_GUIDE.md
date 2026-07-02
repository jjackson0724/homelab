# CGS 2811 - Incident Response and Disaster Recovery: Lab Guide
**Author:** Jarron Jackson | **Lab:** Matrix Homelab | **Semester:** Spring 2027

---

## Lab 1 - Homelab IR Playbook (NIST SP 800-61)

### What You Will Do
Build a complete Incident Response Playbook for the Matrix homelab using NIST SP 800-61. For every technique in the attack chain, define the full IR lifecycle.

For each technique (T1087.001, T1057, T1082, T1049, T1003, T1053.005, T1562.001):

Detection: What Wazuh rule fires? What Event ID? What is the alert text?
Triage: Is this a true positive or false positive? How do you verify?
Containment: Isolate affected system? Block IP? Kill process?
Eradication: Remove persistence? Patch vulnerability? Reset credentials?
Recovery: Restore from backup? Rebuild? Re-image?
Lessons Learned: What detection rule was missing? What hardening would have prevented this?

### Skills Learned
- NIST SP 800-61 IR framework application
- Playbook construction methodology
- Containment strategy selection
- Eradication and recovery procedures
- Post-incident lessons learned documentation

### Purple Team Relevance
The IR playbook is the direct output of purple team work. You ran the attacks, you know what they look like, you wrote the detection rules, now you write what to do when those rules fire. Mad Hat project 17 complete.

### Artifact
labs/cgs2811/homelab-ir-playbook.md

### NIST CSF
RS.RP-1, RS.CO-1, RS.AN-1, RC.RP-1

---

## Lab 2 - Tabletop Exercise

### What You Will Do
Run a solo tabletop exercise using a realistic attack scenario. Choose a scenario (ransomware hitting Sentinel, credential dumping leading to lateral movement to Architect) and walk through the IR playbook. Document decisions, time to detect, time to contain, and gaps identified.

### Artifact
labs/cgs2811/tabletop-exercise-report.md

---

## Lab 3 - Backup and Recovery Procedure

### What You Will Do
Configure Windows File History on Sentinel. Configure VM snapshots in VMware for Trinity and Architect. Document recovery procedure for a fully compromised Sentinel.

### Skills Learned
- Backup strategy selection
- Windows File History configuration
- VM snapshot management
- Recovery time objective documentation
- Recovery point objective planning

### Artifact
labs/cgs2811/backup-recovery-procedures.md

### NIST CSF
RC.RP-1, PR.IP-4, PR.IP-9
