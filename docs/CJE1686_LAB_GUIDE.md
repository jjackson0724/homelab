# CJE 1686 - Forensic Computer Related Crime: Lab Guide
**Author:** Jarron Jackson | **Lab:** Matrix Homelab | **Semester:** Spring 2027

---

## Lab 1 - Forensic Drive Imaging

### What You Will Do
Create a forensic drive image using DC3DD and verify integrity with MD5/SHA256 hashing. Examine the image with Autopsy. Document the full chain of custody.

    sudo apt install -y dc3dd autopsy
    dc3dd if=/dev/sdb of=/tmp/forensic-image.dd hash=sha256 log=/tmp/dc3dd.log
    sha256sum /tmp/forensic-image.dd

### Skills Learned
- Forensic imaging methodology (bit-for-bit copy)
- Hash verification for evidence integrity
- Chain of custody documentation
- Autopsy forensic examination
- Evidence handling standards

### Purple Team Relevance
Understanding forensic imaging tells you what artifacts survive on disk after an attack. When T1070.004 (File Deletion) runs, does the file actually disappear forensically? This informs both attack planning and detection.

### Artifact
labs/cje1686/forensic-imaging-lab.md

---

## Lab 2 - Attack Chain Artifact Catalog

### What You Will Do
For every technique in Phase 1 and Phase 2, document forensic artifacts left behind on Sentinel.

| Technique | Windows Event IDs | File System | Network |
|---|---|---|---|
| T1087.001 | 4688 | - | - |
| T1057 | 4688 | /tmp/loot.txt | - |
| T1082 | 4688 | /tmp/T1082.txt | - |
| T1049 | 4688 | - | Netflow |
| T1003 | 4688, 4656, 4663 | LSASS dump | - |
| T1053.005 | 4698, 4702 | Task XML | - |
| T1562.001 | 7036, 7040 | - | - |

### Skills Learned
- Windows Event Log forensics
- Registry forensics
- File system artifact analysis
- Network forensics correlation
- ATT&CK technique-to-artifact mapping

### Purple Team Relevance
The artifact catalog IS the detection engineering reference for Wazuh rules. Every Event ID listed becomes a potential Wazuh rule trigger.

### Artifact
labs/cje1686/attack-artifact-catalog.md

---

## Lab 3 - PCAP Forensic Analysis During Attack Chain

### What You Will Do
Capture network traffic during the Phase 2 Sentinel attack chain. Analyze PCAP for attack signatures. Document protocol signatures for each technique.

### Artifact
labs/cje1686/attack-chain-pcap-analysis.md

---

## Lab 4 - Timeline Reconstruction

### What You Will Do
Using Windows Event Logs, Wazuh alerts, VECTR timestamps, and PCAP data, reconstruct a complete attack timeline from first reconnaissance through persistence establishment.

### Artifact
labs/cje1686/attack-timeline-reconstruction.md

### NIST CSF
RS.AN-1, RS.AN-3, DE.AE-5
