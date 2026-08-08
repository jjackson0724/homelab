# CTI Track - Matrix Homelab

Cyber Threat Intelligence integrated into the purple team loop.
CTI feeds Trinity emulation and Seraph detection engineering.

## The CTI-to-Purple Loop

1. Select Threat Actor - Pick a real APT group
2. Collect Intelligence - Pull reports from MITRE, Mandiant, CISA
3. Map to ATT&CK - Identify TTPs and infrastructure patterns
4. Build Emulation Plan - SCYTHE PTEF or Caldera adversary profile
5. Execute on Trinity - Run emulation against Sentinel/Architect
6. Detect on Seraph - Validate coverage, write Sigma rules
7. Write Finished Intel - Diamond Model + YARA + JA4 + MISP IoC
8. Commit - git add / commit / push

---

## CTI Node Assignments

| Node | CTI Role |
|---|---|
| Oracle | Local LLM for report summarization and IOC extraction |
| Seraph | MISP platform for IOC storage and correlation |
| Trinity | Adversary emulation from CTI-derived TTPs |
| Architect | Target environment for CTI-informed simulation |
| Zion | OSINT collection, report writing, ATT&CK Navigator |

---

## Threat Actor Library

| Actor | Origin | Focus | ATT&CK Group | Status |
|---|---|---|---|---|
| APT19 | China | Corporate espionage | G0073 | SCYTHE plan available |
| APT33 | Iran | Energy/aerospace | G0064 | SCYTHE plan available |
| APT3 | China | Defense/tech | G0022 | SCYTHE plan available |
| Orangeworm | Unknown | Healthcare | G0071 | SCYTHE plan available |
| Mustang Panda | China | Government/NGO | G0129 | HTB APT range |
| Salt Typhoon | China | Telecom | - | HTB APT range |

---

## CTI Skills - Tier 1 Foundation (2026)

- [ ] Diamond Model complete for all Phase 1 techniques
- [ ] MISP deployed on Seraph, ingest IOCs from exercises
- [ ] ATT&CK Navigator heatmaps per threat actor
- [ ] OSINT basics: domain pivot, WHOIS, certificate transparency
- [ ] Read 2 vendor threat reports per month

---

## CTI Skills - Tier 2 Intermediate (2027)

- [ ] MAD20 CTI Defense Recommendations badge (free, MITRE-produced)
- [ ] Campaign tracking - link IOCs across multiple exercises
- [ ] JA4/JA3 fingerprinting of C2 traffic on Seraph
- [ ] Pivot analysis: IP to domain to certificate to actor
- [ ] Write first finished intelligence product
- [ ] OpenCTI deployment on Seraph alongside MISP
- [ ] SCYTHE ThreatThursday - one plan per month

---

## CTI Skills - Tier 3 Advanced (2028-2029)

- [ ] FOR578 / GCTI - SANS Cyber Threat Intelligence (GI Bill path)
- [ ] Custom adversary emulation plans from raw CTI reports
- [ ] Threat hunting hypothesis development from CTI
- [ ] Intelligence-driven purple team exercises
- [ ] SigmaHQ contribution mapped to specific threat actor TTPs

---

## Free CTI Resources

| Resource | URL |
|---|---|
| MITRE ATT&CK Groups | attack.mitre.org/groups |
| SCYTHE ThreatThursday | github.com/scythe-io/community-threats |
| CISA Advisories | cisa.gov/news-events/cybersecurity-advisories |
| OpenCTI Platform | github.com/OpenCTI-Platform/opencti |
| MISP Project | misp-project.org |
| AlienVault OTX | otx.alienvault.com |
| Shodan | shodan.io |
| Censys | search.censys.io |
| URLScan | urlscan.io |
