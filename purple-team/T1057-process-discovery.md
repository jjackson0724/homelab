# Purple Team Lab Report
## T1057 — Process Discovery
**Date:** July 1, 2026  
**Author:** Jarron Jackson  
**Lab:** Matrix Homelab  
**Phase:** Phase 1 — Pre-SIEM Baseline  
**ATT&CK Technique:** [T1057](https://attack.mitre.org/techniques/T1057/)  
**MITRE Tactic:** Discovery  

---

## Objective

Execute MITRE ATT&CK technique T1057 (Process Discovery) using Atomic Red Team on the Trinity attack machine, document the full output from an attacker's perspective, and record the detection outcome in VECTR as part of a Phase 1 purple team baseline engagement.

This is technique #2 in the Matrix Homelab attack chain, following T1087.001 (Local Account Discovery).

---

## Attack Chain Context

| Order | Technique | ID | Status |
|---|---|---|---|
| 1 | Local Account Discovery | T1087.001 | ✅ Complete |
| 2 | Process Discovery | T1057 | ✅ Complete |
| 3 | System Information Discovery | T1082 | Planned |
| 4 | Network Connection Discovery | T1049 | Planned |
| 5 | Credential Dumping | T1003 | Planned |
| 6 | Cron Job Persistence | T1053.003 | Planned |
| 7 | Disable Security Tools | T1562.001 | Planned |

---

## Environment

| Role | Machine | OS | Notes |
|---|---|---|---|
| Attacker | Trinity | Kali Linux 2026.1 | VMware VM on Zion |
| Target | Trinity (local) | Kali Linux 2026.1 | Self-targeted for Phase 1 baseline |
| Documentation | Zion | Windows 11 | VECTR CE 9.12.2 running via Docker |
| Detection | None | N/A | Pre-Seraph. No SIEM active. |

---

## Tools Used

### Execution Layer
| Tool | Purpose |
|---|---|
| Atomic Red Team | Library of 1,000+ MITRE ATT&CK-mapped attack scripts |
| Invoke-AtomicRedTeam (PowerShell module v2.3.0) | Test runner — executes individual Atomics by technique ID |

### Management & Tracking Layer
| Tool | Purpose |
|---|---|
| VECTR Community Edition 9.12.2 | Purple team engagement tracking, outcome documentation, and MITRE ATT&CK heatmap generation |

### Planned (Phase 2)
| Tool | Purpose |
|---|---|
| MITRE CALDERA | Automated adversary emulation — will replace manual Atomic execution with multi-step attack chains watched by Wazuh in real time |

---

## What Is T1057?

After identifying who is on a compromised machine (T1087.001), an attacker's next move is to understand what is running on it. T1057 covers Process Discovery — enumerating all active processes to identify security tools, running services, databases, and privileged processes that can be targeted or avoided.

On Linux, `ps aux` is the primary tool. It dumps every running process with its owner, PID, CPU/memory usage, and full command line. An attacker scans the COMMAND column looking for:

- EDR/AV processes (CrowdStrike, Defender, Carbon Black, Wazuh)
- Monitoring agents (Splunk forwarder, auditd)
- Database processes (mysqld, postgres) that may contain credentials
- Web servers running as root
- Any process that can be hijacked or killed to blind the defender

---

## Execution

**Command used:**
```powershell
Invoke-AtomicTest T1057 -PathToAtomicsFolder ~/atomic-red-team/atomics
```

One sub-test executed:

| Test # | Name | Command(s) | Output |
|---|---|---|---|
| T1057-1 | Process Discovery - ps | `ps >> /tmp/loot.txt` then `ps aux >> /tmp/loot.txt` | Full process list saved to disk |

**Exit code: 0** — successful execution.

---

## Attack Output Analysis

**Key processes observed in /tmp/loot.txt:**

```
kali  92696  /usr/libexec/glycin-loaders/2+/glycin-image-rs --dbus-fd 44
kali  92701  sh -c ps >> /tmp/loot.txt; ps aux >> /tmp/loot.txt
kali  92704  ps aux
```

**Attacker interpretation:**

| Process | Attacker Assessment |
|---|---|
| `glycin-image-rs` (PID 92696) | Desktop image renderer — zero value, skip |
| `sh -c ps >> /tmp/loot.txt` (PID 92701) | The enumeration script itself captured mid-run — confirms shell execution via `pts/0` interactive session |
| `ps aux` (PID 92704) | Process discovery command captured in its own output |

**Critical attacker finding:** No EDR, no monitoring agent, no Wazuh, no Splunk forwarder present in the process list. Trinity is running a clean Kali desktop with no defensive tooling active. The attacker can proceed without concern for endpoint detection.

**The loot file:** Output was saved to `/tmp/loot.txt` — in a real engagement this file would be exfiltrated to the attacker's C2 server for offline analysis. The full process list gives the attacker a complete map of the machine's running state.

---

## Blue Team Perspective

**What makes T1057 detectable:**

The raw `ps aux` command itself is not suspicious — system administrators run it regularly. What is suspicious is the behavioral context:

1. `ps aux` output being redirected to a file in `/tmp`
2. The parent process being PowerShell (`pwsh`) spawning `sh` spawning `ps`
3. The output file being named `loot.txt` — an obvious indicator but real attackers use innocuous names

**The parent-child chain that should trigger an alert:**
```
pwsh → sh → ps aux >> /tmp/loot.txt
```

PowerShell spawning a shell spawning a recon command writing to `/tmp` is not normal user behavior. A Wazuh rule watching process creation events would flag this chain immediately.

---

## VECTR Documentation

| Field | Value |
|---|---|
| Environment | Home_LAB |
| Assessment | Phase 1 - Process Discovery |
| Campaign | T1057 - Process Discovery |
| Defense Tool | Phase 1 Baseline (Manual Observation) |
| Technique | T1057 — Process Discovery |
| Phase | Discovery |
| Status | Completed |
| Outcome | **None** |
| Defense Success | **Unsuccessful** |
| Attack Source | Trinity (Kali Linux 2026.1) |
| Attack Target | Trinity (local — self) |

No alerts. No logs. No blocks. Process list dumped to disk silently.

---

## Detection Opportunity (Future Wazuh Rule)

**Sigma rule concept:**
```yaml
title: Process Discovery via ps with File Output
status: experimental
description: Detects ps aux output being redirected to a file, indicating process enumeration for exfiltration
logsource:
  category: process_creation
  product: linux
detection:
  selection:
    ParentImage|endswith:
      - 'pwsh'
      - 'bash'
      - 'sh'
    CommandLine|contains|all:
      - 'ps'
      - '/tmp'
  condition: selection
falsepositives:
  - Legitimate system administration scripts
level: medium
tags:
  - attack.discovery
  - attack.t1057
```

This rule will be implemented on Seraph post-build. T1057 will be re-executed via CALDERA agent on Sentinel, with Wazuh watching process creation events in real time. VECTR outcome will be updated from **None** to reflect actual detection.

---

## Phase 2 Plan — CALDERA Integration

In Phase 2, T1057 will be chained with T1087.001 in a single CALDERA adversary profile:

1. CALDERA agent deployed on Sentinel
2. Profile executes T1087.001 → T1057 in sequence (realistic attacker order)
3. Wazuh watches for the full enumeration chain
4. Detection of the chain (not just individual commands) is the goal
5. VECTR outcomes updated for both techniques

---

## Remediation Notes

- Deploy auditd with rules capturing process execution events
- Configure Wazuh to ingest auditd logs and alert on `ps aux` redirected to `/tmp`
- Alert on PowerShell spawning shell processes on Linux endpoints
- Restrict write access to `/tmp` for non-system processes where possible

---

## References

- [MITRE ATT&CK T1057](https://attack.mitre.org/techniques/T1057/)
- [Atomic Red Team T1057](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.md)
- [VECTR Community Edition](https://vectr.io)
- [MITRE CALDERA](https://caldera.mitre.org)
