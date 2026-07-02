# CIS 1358 - Operating System Security: Full Lab Guide
**Author:** Jarron Jackson | **Lab:** Matrix Homelab | **Status:** In Progress

---

## Chapter Priority Map

| Chapter | Topic | Treatment | Priority |
|---|---|---|---|
| CH4 | Identity, AD, Linux Users | Full lab | High |
| CH5 | Firewalls, VPN, Switch/Router | Full lab | High |
| CH6 | Password Attacks, ARP, SYN Flood | Full lab | High |
| CH7 | Vulnerability Management and OpenVAS | Full lab | High |
| CH8 | OS Hardening, DVWA, iptables | Full lab | High |
| CH9 | IR, Forensics, ELK Stack | Full lab | High |
| CH10 | Containers, Virtualization, Cloud | Medium lab | Medium |
| CH12 | Audits, Risk Management | Documentation | Medium |
| CH3 | Cryptography | Light extension | Low |
| CH1 | Introduction | Conceptual | None |
| CH2 | Social Engineering, Malware | Conceptual | None |
| CH11 | Governance | Documentation | None |
| CH13 | Data Classification | Documentation | None |

---

## CH4 - Identity and Access Management

### What You Will Do
Configure Linux users and groups on Trinity. Practice user creation, password policies, sudo restrictions, and group management. On Architect, configure Active Directory OUs, GPOs, and account policies.

### Skills Learned
- Linux user/group management (useradd, usermod, passwd, groupadd)
- sudo configuration and restriction
- SELinux concepts
- Active Directory OUs, GPOs, account lockout policies
- RADIUS/TACACS+ fundamentals

### Purple Team Relevance
T1087.001 output showed uid=1000(kali) in the sudo group. Understanding user management tells you why that is dangerous and how to detect privilege escalation. AD knowledge feeds into Phase 4 Kerberoasting and pass-the-hash attacks against Morpheus.

### Artifacts
labs/ch4-identity-access/linux-user-hardening.md
labs/ch4-identity-access/active-directory-baseline.md

### NIST CSF
PR.AC-1, PR.AC-4, PR.AC-6

---

## CH5 - Network Architecture and Security Appliances

### What You Will Do
Configure Microsoft Defender Firewall on Sentinel with inbound/outbound rules. Set up a VPN connection between Zion and Trinity. Configure router ACLs and switch security concepts. When OPNsense is deployed on Neb, revisit with real firewall rule configuration.

### Skills Learned
- Firewall rule construction (stateful inspection)
- VPN configuration
- Router ACL syntax and logic
- Switch port security
- Network security zones (DMZ, screened subnet)

### Purple Team Relevance
Firewall rules are what an attacker maps during T1046 (Network Service Discovery). Understanding rule construction tells you which ports are likely filtered and which attack paths are blocked.

### Artifacts
labs/ch5-network-security/sentinel-firewall-rules.md
labs/ch5-network-security/vpn-configuration.md

### NIST CSF
PR.AC-5, PR.PT-4, DE.CM-1

---

## CH6 - Password Attacks, ARP Poisoning, SYN Flood

### What You Will Do

Lab 1 - Password Attacks on Trinity:
Run John the Ripper against /etc/shadow on Trinity. Use rainbow tables to crack hashed passwords.

Lab 2 - ARP Poisoning:
Run arpspoof on Trinity against Sentinel. Capture with Wireshark. Document what the attacker sees and what the defender should detect.

Lab 3 - SYN Flood Analysis:
Use hping3 on Trinity to simulate a SYN flood against Sentinel. Capture with Wireshark.

### Skills Learned
- John the Ripper password cracking
- Rainbow table attacks
- ARP poisoning mechanics and detection
- SYN flood attack structure
- Wireshark traffic analysis for attack signatures

### Purple Team Relevance
Password attacks feed into T1003 (Credential Dumping). ARP poisoning is T1557 (Adversary-in-the-Middle) identified in the PCAP analysis. SYN floods map to T1498 (Network DoS).

### Artifacts
labs/ch6-network-attacks/password-attack-lab.md
labs/ch6-network-attacks/arp-poisoning-lab.md
labs/ch6-network-attacks/syn-flood-analysis.md

### NIST CSF
DE.AE-2, DE.CM-1, RS.AN-1

---

## CH7 - Vulnerability Management and Scanning

### What You Will Do

Lab 1 - OpenVAS on Trinity:
    sudo apt install -y gvm
    sudo gvm-setup
    sudo gvm-start
Run unauthenticated and authenticated scans against Sentinel. Export PDF report. Triage by CVSS score.

Lab 2 - Vulnerability Management Report:
Classify findings by type. Assign risk ratings. Build remediation plan.

Lab 3 - Seraph Architecture Design:
Pre-build design document for Wazuh SIEM.

Lab 4 - Pentest ROE Document:
Formal Rules of Engagement for homelab engagements.

### Skills Learned
- OpenVAS/GVM deployment and configuration
- Authenticated vs unauthenticated scanning
- CVSS score interpretation
- Vulnerability triage and risk rating
- Professional vuln report generation
- SIEM architecture design

### Purple Team Relevance
OpenVAS findings bridge discovery and exploitation. After T1049 confirmed Sentinel IP, scanning confirms which techniques are viable.

### Artifacts
labs/ch7-vulnerability/openvas-sentinel-report.md
labs/ch7-vulnerability/vuln-management-report.md
labs/ch7-vulnerability/seraph-siem-design.md
labs/ch7-vulnerability/homelab-roe.md

### NIST CSF
ID.RA-1, ID.RA-5, DE.CM-8, GV.PO-1

---

## CH8 - OS Hardening, Web App Security, Application Security

### What You Will Do

Lab 1 - Sentinel OS Hardening:
Apply Zion hardening methodology to Sentinel. Configure Defender Firewall, automatic updates, disable unnecessary services.

Lab 2 - NTFS Permissions on Architect:
Build folder structure, configure least-privilege NTFS permissions, disable inheritance.

Lab 3 - iptables on Trinity:
Audit running services, remove unnecessary ones, configure iptables INPUT/OUTPUT/FORWARD chains.

Lab 4 - DVWA Web App:
    docker pull vulnerables/web-dvwa
    docker run -d -p 80:80 vulnerables/web-dvwa
Execute SQLi, XSS, CSRF, command injection. Document with OWASP mapping.

Lab 5 - AppLocker and DEP on Architect:
Configure application allow-listing. Test against unsigned binaries. Configure DEP.

### Skills Learned
- Windows OS hardening methodology
- NTFS ACL configuration
- Linux service reduction and iptables
- SQL injection (union, blind, error-based)
- Cross-site scripting (reflected, stored, DOM)
- CSRF attack construction
- OWASP Top 10 methodology
- AppLocker policy configuration
- Data Execution Prevention

### Purple Team Relevance
DVWA opens web application attack domain - T1190 (Exploit Public-Facing Application) is a primary initial access vector. AppLocker directly defends against T1053.005 execution techniques.

### Artifacts
labs/ch8-hardening/sentinel-os-hardening.md
labs/ch8-hardening/ntfs-permissions-lab.md
labs/ch8-hardening/trinity-iptables.md
labs/ch8-hardening/dvwa-owasp-lab.md
labs/ch8-hardening/applocker-dep-lab.md

### NIST CSF
PR.IP-1, PR.AC-1, PR.PT-3, ID.RA-1, DE.CM-4

---

## CH9 - Incident Response, Log Management and Digital Forensics

### What You Will Do

Lab 1 - IR Process Documentation:
Build IR playbook using NIST SP 800-61 for T1087.001, T1057, T1082, T1049.

Lab 2 - ELK Stack on Zion:
Deploy Elasticsearch + Logstash + Kibana in Docker. Ingest Trinity attack session logs.

Lab 3 - Digital Forensics with Autopsy:
Create forensic drive image with DC3DD. Examine with Autopsy. Document chain of custody.

Lab 4 - Forensic Artifact Catalog:
For each Phase 1 ATT&CK technique, document Windows Event Log IDs, Linux syslog strings, registry keys, file system artifacts.

### Skills Learned
- NIST SP 800-61 IR lifecycle
- ELK stack deployment and log ingestion
- Forensic drive imaging (DC3DD, Guymager)
- Autopsy forensic examination
- Chain of custody documentation
- Windows Event Log forensics
- Artifact correlation by ATT&CK technique

### Purple Team Relevance
The forensic artifact catalog is the blue team detection reference. ELK preview informs Seraph Phase 3 deployment. IR playbook becomes Mad Hat project 17.

### Artifacts
labs/ch9-ir-forensics/ir-playbook-phase1.md
labs/ch9-ir-forensics/elk-stack-deployment.md
labs/ch9-ir-forensics/forensic-drive-imaging.md
labs/ch9-ir-forensics/attack-artifact-catalog.md

### NIST CSF
RS.RP-1, RS.AN-1, RS.AN-3, DE.AE-3, RC.RP-1

---

## CH10 - Virtualization, Containers and Cloud

### What You Will Do
Docker is already running on Zion - document the VECTR container stack as the lab artifact. Deploy DVWA container from CH8. When Neb is built, document Proxmox VM networking.

### Artifacts
labs/ch10-virtualization/docker-container-lab.md
labs/ch10-virtualization/proxmox-vm-networking.md

### NIST CSF
PR.IP-1, PR.PT-3, ID.AM-2

---

## CH12 - Risk Management and Audits

### What You Will Do
Configure Windows Security Log auditing on Sentinel. Map VECTR engagement findings to a risk register. Document residual risk after Phase 1 techniques ran undetected.

### Artifacts
labs/ch12-risk/homelab-risk-register.md
labs/ch12-risk/sentinel-audit-policy.md

### NIST CSF
ID.RA-1, ID.RA-5, GV.RM-1

---

## Build Order

1. CH6 password, ARP, SYN flood labs
2. CH7 OpenVAS scan of Sentinel
3. CH8 Sentinel hardening and DVWA
4. CH9 forensic artifact catalog
5. CH4 Linux user hardening on Trinity
6. CH5 Sentinel firewall rules
7. CH8 iptables on Trinity
8. CH9 ELK stack
9. CH10 Docker documentation
10. CH12 risk register
