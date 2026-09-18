# Sigma Rules - Matrix Homelab

Detection rules written against Phase 1 ATT&CK techniques executed on Sentinel (Windows 11).

## Log Source Coverage

Each rule covers three detection layers:

| Layer | Event Source | Requirement |
|---|---|---|
| Native Windows | EventID 4688 | Process Command Line auditing via GPO |
| Sysmon | EventID 1 | Sysmon deployed with config |
| PowerShell | EventID 4104 | PS Script Block Logging via GPO |

## Rules

| File | Technique | Tactic | Level |
|---|---|---|---|
| T1087.001-local-account-discovery.yml | T1087.001 | Discovery | Medium |
| T1057-process-discovery.yml | T1057 | Discovery | Low |
| T1082-system-information-discovery.yml | T1082 | Discovery | Low |
| T1049-network-connection-discovery.yml | T1049 | Discovery | Low |

## Deployment Status

Rules are drafted and validated against technique execution logs.
Pending deployment to Seraph (Wazuh) post-Nebuchadnezzar build.

## References

- Sigma HQ: github.com/SigmaHQ/sigma
- MITRE ATT&CK Discovery: attack.mitre.org/tactics/TA0007
- Wazuh Sigma Integration: documentation.wazuh.com
