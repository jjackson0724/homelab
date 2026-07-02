# Cybersecurity Skills Roadmap
**Jarron Jackson | Matrix Homelab | SPC A.S. to B.A.S. | Purple Team Operator Track**

754 structured cybersecurity skills installed at:
C:\Users\Jarron\.claude\skills\cybersecurity
Query: py C:\Users\Jarron\matrix-homelab\scripts\skill_query.py

---

## Phase 1 - Baseline and Recon (Current)

- [x] Zion OS hardening - VeraCrypt FDE, firewall, UAC, audit logging
- [x] PCAP analysis - 50k packets, Wireshark/Scapy, DNS analysis, WPAD exposure
- [x] performing-purple-team-exercise
- [x] performing-purple-team-atomic-testing
- [x] performing-threat-emulation-with-atomic-red-team
- [x] mapping-mitre-attack-techniques
- [x] implementing-mitre-attack-coverage-mapping
- [x] performing-pcap-analysis-with-wireshark
- [ ] Sentinel Windows hardening
- [ ] deploying-openvas-vulnerability-scanner
- [ ] performing-vulnerability-scan-with-openvas
- [ ] implementing-vulnerability-management-workflow
- [ ] configuring-dvwa-for-web-app-testing
- [ ] performing-sql-injection-attack
- [ ] performing-xss-attack
- [ ] performing-csrf-attack
- [ ] configuring-iptables-firewall-rules
- [ ] performing-password-attack-with-john-the-ripper
- [ ] cracking-passwords-with-rainbow-tables
- [ ] detecting-arp-poisoning-in-network-traffic
- [ ] analyzing-syn-flood-attack
- [ ] executing-red-team-exercise

## Phase 2 - Exploitation (Pre-Neb)

- [ ] performing-credential-dumping-t1003
- [ ] implementing-scheduled-task-persistence-t1053
- [ ] performing-security-tool-impairment-t1562
- [ ] building-forensic-artifact-catalog
- [ ] capturing-pcap-during-attack-chain
- [ ] documenting-rules-of-engagement

## Phase 3 - Detection Engineering (Post-Neb)

- [ ] deploying-wazuh-siem
- [ ] configuring-wazuh-agent-deployment
- [ ] building-wazuh-detection-rules
- [ ] deploying-caldera-adversary-emulation
- [ ] configuring-caldera-attack-profiles
- [ ] building-sigma-detection-rules
- [ ] building-splunk-dashboards-for-threat-detection
- [ ] implementing-log-aggregation-pipeline

## Phase 4 - Enterprise Simulation (Post-Morpheus)

- [ ] deploying-active-directory-domain-controller
- [ ] deploying-active-directory-honeytokens
- [ ] performing-kerberoasting-attack
- [ ] performing-pass-the-hash-attack
- [ ] performing-lateral-movement-techniques
- [ ] implementing-honeypot-for-ransomware-detection
- [ ] implementing-canary-tokens-for-network-intrusion
- [ ] building-incident-response-playbook
- [ ] performing-nist-csf-maturity-assessment

## Phase 5 - Infrastructure Hardening

- [ ] configuring-opnsense-firewall-rules
- [ ] implementing-network-segmentation-with-vlans
- [ ] configuring-ids-ips-with-suricata
- [ ] configuring-suricata-ids-alerts
- [ ] deploying-zeek-network-monitoring
- [ ] building-network-baseline-with-zeek-logs
- [ ] implementing-network-deception-with-honeypots
- [ ] implementing-honeytokens-for-breach-detection

---

## Security+ Exam Prep Track

### Cryptography and PKI
- [ ] implementing-aes-encryption-for-data-at-rest
- [ ] implementing-rsa-key-pair-management
- [ ] implementing-digital-signatures-with-ed25519
- [ ] implementing-jwt-signing-and-verification
- [ ] configuring-tls-1-3-for-secure-communications
- [ ] performing-ssl-tls-security-assessment

### Network Security
- [ ] configuring-network-segmentation-with-vlans
- [ ] configuring-pfsense-firewall-rules
- [ ] implementing-dmarc-dkim-spf-email-security
- [ ] detecting-arp-poisoning-in-network-traffic

### Identity and Access
- [ ] configuring-multi-factor-authentication-with-duo
- [ ] detecting-privilege-escalation-attempts
- [ ] implementing-disk-encryption-with-bitlocker

---

## ISC2 CC Track

- [ ] performing-nist-csf-maturity-assessment
- [x] mapping-mitre-attack-techniques
- [x] implementing-mitre-attack-coverage-mapping
- [ ] building-incident-response-playbook
- [ ] performing-soc2-type2-audit-preparation
- [ ] implementing-pci-dss-compliance-controls

---

## Definition of Done

    [1] Execute  - Run the attack or deploy the control
    [2] Validate - Confirm in logs, SIEM, or manual observation
    [3] Document - Write markdown entry in appropriate folder
    [4] Commit   - git add / commit / push to master
