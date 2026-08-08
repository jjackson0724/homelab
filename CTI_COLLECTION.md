# CTI Collection System - Matrix Homelab

Structured intelligence collection feeding the CTI-to-Purple loop.

## Dedicated CTI Inbox

Create a dedicated email (e.g. matrix-cti@proton.me) for threat intel feeds.
Keep it separate from personal email - it becomes a searchable archive.

---

## Feed Subscriptions

### Government
| Source | URL | Cadence |
|---|---|---|
| CISA Advisories | cisa.gov/subscribe-updates-cisa | As published |
| CISA KEV Catalog | cisa.gov/known-exploited-vulnerabilities-catalog | Weekly |
| FBI Flash Alerts | ic3.gov | As published |
| NSA Advisories | nsa.gov/Press-Room/Cybersecurity-Advisories-Guidance | As published |

### Vendor
| Source | URL | Cadence |
|---|---|---|
| Mandiant Blog | mandiant.com/resources/blog | Weekly |
| CrowdStrike Blog | crowdstrike.com/blog | Weekly |
| Microsoft MSTIC | microsoft.com/en-us/security/blog | Weekly |
| Palo Alto Unit 42 | unit42.paloaltonetworks.com | Weekly |

### Community
| Source | URL | Cadence |
|---|---|---|
| SCYTHE ThreatThursday | scythe.io/threatthursday | Weekly Thursdays |
| AlienVault OTX | otx.alienvault.com | Daily digest |
| SANS ISC | isc.sans.edu | Daily |
| The DFIR Report | thedfirreport.com | Weekly |

---

## Weekly Collection Routine - 20 Minutes Per Day

| Day | Focus | Action |
|---|---|---|
| Monday | Government | Check CISA advisories, note TTPs and actors |
| Tuesday | Vendor | Read one Mandiant or CrowdStrike post, extract IOCs |
| Wednesday | Community | AlienVault OTX digest, SANS ISC |
| Thursday | SCYTHE | Download ThreatThursday


cd C:\Users\Jarron\matrix-homelab

# Remove the accidental zip
if (Test-Path "files.zip") { git rm files.zip }

Set-Content -Path "CTI_COLLECTION.md" -Encoding utf8 -Value @"
# CTI Collection System - Matrix Homelab

Structured intelligence collection feeding the CTI-to-Purple loop.

## Dedicated CTI Inbox

Create a dedicated email (e.g. matrix-cti@proton.me) for threat intel feeds.
Keep it separate from personal email - it becomes a searchable archive.

---

## Feed Subscriptions

### Government
| Source | URL | Cadence |
|---|---|---|
| CISA Advisories | cisa.gov/subscribe-updates-cisa | As published |
| CISA KEV Catalog | cisa.gov/known-exploited-vulnerabilities-catalog | Weekly |
| FBI Flash Alerts | ic3.gov | As published |
| NSA Advisories | nsa.gov/Press-Room/Cybersecurity-Advisories-Guidance | As published |

### Vendor
| Source | URL | Cadence |
|---|---|---|
| Mandiant Blog | mandiant.com/resources/blog | Weekly |
| CrowdStrike Blog | crowdstrike.com/blog | Weekly |
| Microsoft MSTIC | microsoft.com/en-us/security/blog | Weekly |
| Palo Alto Unit 42 | unit42.paloaltonetworks.com | Weekly |

### Community
| Source | URL | Cadence |
|---|---|---|
| SCYTHE ThreatThursday | scythe.io/threatthursday | Weekly Thursdays |
| AlienVault OTX | otx.alienvault.com | Daily digest |
| SANS ISC | isc.sans.edu | Daily |
| The DFIR Report | thedfirreport.com | Weekly |

---

## Weekly Collection Routine - 20 Minutes Per Day

| Day | Focus | Action |
|---|---|---|
| Monday | Government | Check CISA advisories, note TTPs and actors |
| Tuesday | Vendor | Read one Mandiant or CrowdStrike post, extract IOCs |
| Wednesday | Community | AlienVault OTX digest, SANS ISC |
| Thursday | SCYTHE | Download ThreatThursday plan, map to ATT&CK, queue for Trinity |
| Friday | Wrap | Log findings in COLLECTION_LOG.md, push IOCs to MISP |

---

## CTI Courses

### 1. CISA Introduction to Cyber Threat Intelligence
- Cost: Free - no account required
- URL: cisa.gov/resources-tools/training/introduction-cyber-threat-intelligence
- Covers: Intelligence cycle, collection methodology, analysis frameworks, dissemination
- When: 2026 - take this first
- Deliverable: Completion certificate saved to docs/

### 2. Cybrary Cyber Threat Intelligence
- Cost: Free with account
- URL: cybrary.it/course/cyber-threat-intelligence
- Covers: Collection planning, source evaluation, IOC analysis, threat actor profiling
- When: 2026 alongside THM beginner paths
- Deliverable: Course badge to LinkedIn and docs/

### 3. MAD20 CTI Defense Recommendations Badge
- Cost: MAD20 subscription
- URL: mad20.com
- Covers: ATT&CK-mapped CTI for defensive recommendations
- When: 2027 - required prerequisite for MAD20 Purple Teaming cert
- Deliverable: MITRE-issued badge to GitHub and LinkedIn

---

## References

- MITRE ATT&CK CTI: attack.mitre.org/resources/working-with-attack/cti
- CISA Free Training: cisa.gov/resources-tools/training
- Cybrary: cybrary.it
- The DFIR Report: thedfirreport.com
