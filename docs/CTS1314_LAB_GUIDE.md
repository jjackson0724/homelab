# CTS 1314 - Network Defense/Countermeasures: Lab Guide
**Author:** Jarron Jackson | **Lab:** Matrix Homelab | **Semester:** Fall 2026

---

## Lab 1 - Seraph Deployment (Wazuh on Neb)

### What You Will Do
Deploy Wazuh SIEM on the Seraph VM on Nebuchadnezzar. Configure the Wazuh manager, install agents on Sentinel and Trinity, and verify log ingestion. Build initial dashboards.

Deployment steps:
- Install Wazuh manager on Seraph
- Deploy Wazuh agents on Sentinel (Windows) and Trinity (Linux)
- Configure syscheck (file integrity monitoring)
- Configure log analysis for Windows Event Logs and Linux syslog
- Verify agent connectivity and log ingestion

### Skills Learned
- SIEM architecture and deployment
- Wazuh manager and agent configuration
- Windows Event Log ingestion
- Linux syslog ingestion
- File integrity monitoring
- SIEM dashboard construction

### Purple Team Relevance
This is the detection layer that makes Phase 3 possible. Without Seraph watching, every Phase 1 technique outcome is None. With Wazuh active, the full chain is retested and the VECTR score becomes a real number.

### Artifact
labs/cts1314/seraph-wazuh-deployment.md

### NIST CSF
DE.CM-1, DE.CM-7, DE.AE-2

---

## Lab 2 - Custom Detection Rules per ATT&CK Technique

### What You Will Do
Write custom Wazuh detection rules for each technique in the Phase 1 attack chain. Retest each technique after rule deployment.

Rules to write:
- T1087.001 - Alert on rapid sequential execution of id, groups, cat /etc/passwd
- T1057 - Alert on ps aux output redirected to /tmp
- T1082 - Alert on sequential fingerprinting commands within 30 seconds
- T1049 - Alert on ss, netstat, who in rapid succession
- T1003 - Alert on LSASS memory access on Windows
- T1053.005 - Alert on scheduled task creation via schtasks
- T1562.001 - Alert on Windows Defender service stop attempt

### Skills Learned
- Wazuh rule syntax (XML)
- Log pattern matching
- Alert threshold configuration
- False positive tuning
- ATT&CK technique to detection rule mapping

### Purple Team Relevance
Writing detection rules is the core blue team skill that purple team teaches. You fired the attack, you know what it looks like in logs, now you write the rule that catches it.

### Artifacts
labs/cts1314/wazuh-detection-rules/
labs/cts1314/detection-engineering-report.md

### NIST CSF
DE.CM-7, DE.AE-2, RS.AN-1

---

## Lab 3 - VECTR Before/After Heatmap

### What You Will Do
After Wazuh rules are deployed, retest all Phase 1 and Phase 2 techniques using CALDERA. Log updated outcomes in VECTR. Generate before vs after heatmap. Document Threat Resilience Score improvement.

### Artifacts
labs/cts1314/vectr-before-after-heatmap.md
labs/cts1314/caldera-attack-profiles/

### NIST CSF
DE.CM-1, ID.RA-1, RS.AN-2

---

## Lab 4 - Suricata IDS in OPNsense

### What You Will Do
Deploy Suricata IDS inside OPNsense on Neb. Configure rules to detect ARP poisoning, SYN floods, and port scanning. Run Phase 1 network attack labs with Suricata watching.

### Artifact
labs/cts1314/suricata-ids-deployment.md

### NIST CSF
DE.CM-1, DE.AE-2, PR.PT-4
