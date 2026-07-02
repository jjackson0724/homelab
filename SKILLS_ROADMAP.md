# Cybersecurity Skills Roadmap

754 structured cybersecurity skills installed at:

`C:\\Users\\Jarron\\.claude\\skills\\cybersecurity`

Query them using: `py C:\\Users\\Jarron\\matrix-homelab\\scripts\\skill_query.py`

---

## Lab Phases

### Phase 1 — Current (Pre-June 29)
- [x ] PCAP/C2 analysis (#16) — Zion/Trinity
- [ ] LLM prompt injection (#8) — Zion

### Phase 2 — Post-Course (July)
- [ ] Home SIEM (#1) — Seraph on Nebuchadnezzar
- [ ] Honeypot (#3) — Seraph on Nebuchadnezzar

### Phase 3 — Once Morpheus is Built
- [ ] AD attack-and-defend (#14)
- [ ] Malware reverse engineering (#5)
- [ ] SigmaHQ contribution (#2) ← capstone

### Phase 4 — Network Infrastructure
- [ ] Source cheap mini PC with dual NICs ($50-100 eBay)
- [ ] Install OPNsense UTM — sits between router and entire lab network
- [ ] Configure Suricata IDS inside OPNsense
- [ ] VLAN segmentation — isolate lab traffic from home network
- [ ] Feed UTM logs into Seraph (Wazuh)
- [ ] Place Honeypot behind UTM for realistic traffic analysis

---

## Track 1 — Security+ Exam Prep

### Cryptography & PKI
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

### Identity & Access
- [ ] configuring-multi-factor-authentication-with-duo
- [ ] detecting-privilege-escalation-attempts
- [ ] implementing-disk-encryption-with-bitlocker

---

## Track 2 — Purple Team / Active Defense 

### Deception & Active Defense
- [ ] deploying-active-directory-honeytokens
- [ ] implementing-honeypot-for-ransomware-detection
- [ ] implementing-honeytokens-for-breach-detection
- [ ] implementing-canary-tokens-for-network-intrusion
- [ ] deploying-decoy-files-for-ransomware-detection
- [ ] implementing-deception-based-detection-with-canaries
- [ ] performing-deception-technology-deployment
- [ ] implementing-network-deception-with-honeypots

### Purple Team Exercises
- [x ] performing-purple-team-exercise
- [x ] performing-purple-team-atomic-testing
- [x ] performing-threat-emulation-with-atomic-red-team
- [ ] executing-red-team-exercise

---

## Track 3 — ISC2 CC & NIST Framework Alignment
- [ ] performing-nist-csf-maturity-assessment
- [x ] mapping-mitre-attack-techniques
- [x ] implementing-mitre-attack-coverage-mapping
- [ ] building-incident-response-playbook
- [ ] performing-soc2-type2-audit-preparation
- [ ] implementing-pci-dss-compliance-controls

---

## Track 4 — Lab Infrastructure & Network Architecture

### UTM / Firewall
- [ ] configuring-opnsense-firewall-rules
- [ ] configuring-pfsense-firewall-rules
- [ ] implementing-network-segmentation-with-vlans
- [ ] configuring-ids-ips-with-suricata

### Network Monitoring
- [ ] deploying-zeek-network-monitoring
- [ ] configuring-suricata-ids-alerts
- [x ] performing-pcap-analysis-with-wireshark
- [ ] building-network-baseline-with-zeek-logs

### SIEM & Log Management
- [ ] deploying-wazuh-siem
- [ ] configuring-wazuh-agent-deployment
- [ ] building-splunk-dashboards-for-threat-detection
- [ ] implementing-log-aggregation-pipeline

---

## How to use

1. Run skill_query.py
2. Search for the skill name
3. Ask it questions relevant to your current study topic
4. Check off the skill when done
5. Document which NIST CSF controls it maps to for portfolio evidence
