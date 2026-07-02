# B.A.S. Cybersecurity - High-Value Course Lab Guide
**Author:** Jarron Jackson | **Lab:** Matrix Homelab | **Post A.S. Track**

---

## Overview

The B.A.S. builds on A.S. foundations with upper-division courses weighted toward threat detection, penetration testing, cloud security, and AI/emerging tech. The courses below represent the highest employer and career value in the curriculum.

---

## CTS 4124 - Threat Detection and Mitigation

### What You Will Do
This course is Phase 3 at the advanced level. By this course, Seraph is online, Wazuh is deployed, and you have a full detection engineering track running.

Lab extensions:
- Build threat hunting queries in Wazuh/Elastic for Phase 2 techniques
- Implement MITRE ATT&CK Navigator heatmap from VECTR data
- Configure automated response playbooks (SOAR concepts)
- Build custom dashboards for purple team engagement review
- Contribute detection rules to SigmaHQ

### Skills Learned
- Advanced SIEM query construction
- Behavioral analytics and anomaly detection
- Threat hunting methodology
- SOAR playbook concepts
- SigmaHQ rule contribution

### Purple Team Relevance
By this course, you have run 7+ techniques against Sentinel with real data to hunt against. SigmaHQ contribution (Mad Hat project 2 capstone) targets this course.

### Artifacts
labs/bas/cts4124-threat-detection/
labs/bas/cts4124-threat-detection/sigma-contribution.md

### NIST CSF
DE.CM-7, DE.AE-2, RS.AN-1, RS.AN-4

---

## CIS 4200 - Security Penetration Testing

### What You Will Do
By this course, you have a complete professional pentest portfolio. Lab work extends into advanced exploitation.

Lab extensions:
- GOAD (Game of Active Directory) full engagement on Morpheus
- Advanced Kerberoasting and DCSync attacks
- Metasploit module usage and customization
- Advanced evasion and AMSI bypass techniques
- Full professional pentest report for homelab

### Skills Learned
- Advanced Active Directory attacks
- Metasploit framework mastery
- Evasion and bypass techniques
- Advanced web application exploitation
- Professional pentest report writing

### Purple Team Relevance
CIS 4200 is where the purple team track reaches full maturity. You are running full attack chains against a real AD environment with real detection. The VECTR heatmap should show substantial improvement from the Phase 1 0.00% baseline.

### Artifacts
labs/bas/cis4200-pentest/
labs/bas/cis4200-pentest/goad-engagement-report.md

---

## CIS 4776 - Cyber Warfare

### What You Will Do
Nation-state TTPs, APT simulation, and advanced adversary emulation. Lab work focuses on APT-style attack profiles.

Lab extensions:
- Build CALDERA adversary profiles based on real APT groups (APT29, APT41)
- Run multi-phase APT simulation: reconnaissance to initial access to persistence to lateral movement to exfiltration
- Document IOCs for each phase
- Build threat intelligence report from engagement

### Skills Learned
- APT TTP mapping to ATT&CK
- Multi-phase engagement planning
- IOC identification and documentation
- Threat intelligence report writing
- Nation-state attack simulation methodology

### Artifacts
labs/bas/cis4776-cyber-warfare/
labs/bas/cis4776-cyber-warfare/apt-simulation-report.md

---

## ISM 4571 - Emerging Security Technologies

### What You Will Do
AI security, LLM attacks, and next-generation threat vectors. Oracle (AI inference node on Neb) is operational by this course.

Lab extensions:
- LLM prompt injection attacks against Oracle (Ollama/vLLM)
- Adversarial ML concepts applied to security models
- AI-assisted threat hunting in Wazuh
- AI-vs-AI detection scenarios
- Document AI attack surface for homelab

### Skills Learned
- LLM prompt injection methodology
- AI model security concepts
- Adversarial ML fundamentals
- AI-assisted detection techniques
- Emerging threat landscape analysis

### Purple Team Relevance
Your Oracle AI node and the skill_query.py RAG script put you ahead of most practitioners. LLM prompt injection (Mad Hat project 8) targets this course.

### Artifacts
labs/bas/ism4571-emerging-tech/
labs/bas/ism4571-emerging-tech/llm-prompt-injection-lab.md
labs/bas/ism4571-emerging-tech/ai-security-assessment.md

---

## ISM 4914 - Security Capstone

### What You Will Do
Portfolio finalization and open-source contribution. SigmaHQ contribution is ready to submit.

Capstone deliverables:
- Complete GitHub homelab repo (all phases documented)
- SigmaHQ detection rule contribution (Mad Hat project 2)
- VECTR final heatmap showing full engagement coverage
- Professional portfolio and LinkedIn project showcase
- Internship/job application package

### Artifacts
labs/bas/ism4914-capstone/
labs/bas/ism4914-capstone/sigmahq-contribution.md
labs/bas/ism4914-capstone/portfolio-summary.md

---

## B.A.S. Medium-Value Courses

| Course | Lab Focus | Artifact |
|---|---|---|
| ISM 4330 - Info Security Policy Admin | NIST CSF policy documentation | labs/bas/ism4330-policy/security-policy-framework.md |
| ISM 4573 - Compliance and Data Governance | Map homelab controls to PCI-DSS/HIPAA | labs/bas/ism4573-compliance/compliance-mapping.md |
| ISM 4321 - Strategic Cybersecurity | Executive risk report from VECTR data | labs/bas/ism4321-strategy/executive-risk-report.md |
| ISM 4329 - Incident Investigation and Forensics | Advanced forensic artifact catalog | labs/bas/ism4329-forensics/advanced-artifact-catalog.md |
| CIS 3661 - Security Architectures | Phase 5 network architecture documentation | labs/bas/cis3661-architecture/lab-security-architecture.md |
| CIS 3083 - Cloud Computing Foundations | Oracle VM cloud security lab | labs/bas/cis3083-cloud/oracle-cloud-security.md |
| CNT 3421 - Securing the Cloud | Oracle hardening documentation | labs/bas/cnt3421-cloud/oracle-hardening.md |

---

## B.A.S. Phase Alignment

| Phase | B.A.S. Courses Activated |
|---|---|
| Phase 3 (Seraph/Wazuh) | CTS 4124, ISM 4329 |
| Phase 4 (Morpheus/AD) | CIS 4200, CIS 4776 |
| Phase 5 (Infrastructure) | CIS 3661, ISM 4321 |
| Oracle Online | CIS 3083, CNT 3421, ISM 4571 |
| Capstone | ISM 4914 |
