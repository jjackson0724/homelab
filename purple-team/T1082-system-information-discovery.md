# Purple Team Lab Report
## T1082 — System Information Discovery
**Date:** July 1, 2026  
**Author:** Jarron Jackson  
**Lab:** Matrix Homelab  
**Phase:** Phase 1 — Pre-SIEM Baseline  
**ATT&CK Technique:** [T1082](https://attack.mitre.org/techniques/T1082/)  
**MITRE Tactic:** Discovery  

---

## Objective

Execute MITRE ATT&CK technique T1082 (System Information Discovery) using Atomic Red Team on the Trinity attack machine, document the full output from an attacker's perspective, and record the detection outcome in VECTR as part of a Phase 1 purple team baseline engagement.

This is technique #3 in the Matrix Homelab attack chain, following T1087.001 (Local Account Discovery) and T1057 (Process Discovery).

---

## Attack Chain Context

| Order | Technique | ID | Status |
|---|---|---|---|
| 1 | Local Account Discovery | T1087.001 | ✅ Complete |
| 2 | Process Discovery | T1057 | ✅ Complete |
| 3 | System Information Discovery | T1082 | ✅ Complete |
| 4 | Network Connection Discovery | T1049 | Planned |
| 5 | Credential Dumping | T1003 | Planned |
| 6 | Cron Job Persistence | T1053.003 | Planned |
| 7 | Disable Security Tools | T1562.001 | Planned |

---

## Environment

| Role | Machine | OS | Notes |
|---|---|---|---|
| Attacker | Trinity | Kali Linux 2026.2 | VMware VM on Zion |
| Target | Trinity (local) | Kali Linux 2026.2 | Self-targeted for Phase 1 baseline |
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

## What Is T1082?

After identifying who is on a machine (T1087.001) and what is running on it (T1057), an attacker fingerprints the machine itself. T1082 covers System Information Discovery — collecting OS version, kernel version, hostname, hardware details, and environment variables.

Every piece of this information informs exploit selection and next steps:

- **Kernel version** — checked against known local privilege escalation exploits
- **OS version** — determines which tools and techniques are compatible
- **Hostname** — in enterprise environments reveals the machine's role (DC01, FILESERVER, PAYROLL-PC)
- **Environment variables** — can reveal running agents, loaded credentials, SSH keys, and tool paths
- **VM detection** — sophisticated malware aborts execution if it detects a sandbox/VM environment

---

## Execution

**Command used:**
```powershell
Invoke-AtomicTest T1082 -TestNumbers 3,4,8,12 -PathToAtomicsFolder ~/atomic-red-team/atomics
```

Sub-tests selected and rationale:

| Test # | Name | Selected | Reason |
|---|---|---|---|
| T1082-3 | List OS Information | ✅ | Core fingerprinting — always relevant |
| T1082-4 | Linux VM Check via Hardware | ✅ | Trinity is a VMware VM — will return real results |
| T1082-5 | Linux VM Check via Kernel Modules | ❌ | Requires elevation, low priority for this chain |
| T1082-6 | FreeBSD VM Check | ❌ | Not applicable — Trinity runs Linux |
| T1082-8 | Hostname Discovery | ✅ | Always relevant — one command, instant value |
| T1082-12 | Environment Variables | ✅ | High value — reveals SSH agent, tool paths, credentials |
| T1082-24 | Azure Security Scan | ❌ | Requires Azure credentials — not applicable |
| T1082-25 | Linux Kernel Modules | ❌ | Low priority for current chain |

All selected tests returned **Exit code: 0** (successful execution). Test 4 returned Exit code 1 on some sub-checks but still returned meaningful VMware confirmation data.

---

## Attack Output Analysis

### Test 3 — OS Information

**Raw output:**
```
Linux kali 6.19.14+kali-amd64 #1 SMP PREEMPT_DYNAMIC Kali 6.19.14-1+kali1 (2026-05-05) x86_64 GNU/Linux
PRETTY_NAME="Kali GNU/Linux Rolling"
NAME="Kali GNU/Linux"
VERSION_ID="2026.2"
VERSION="2026.2"
VERSION_CODENAME=kali-rolling
ID=kali
 01:24:59 up 4:27, 1 user, load average: 0.21, 0.26, 0.12
```

**Attacker interpretation:**

| Finding | Value | Attacker Significance |
|---|---|---|
| OS | Kali GNU/Linux 2026.2 | Confirmed attacker machine — not a typical victim |
| Kernel | 6.19.14 | Check against kernel CVE database for local privesc exploits |
| Architecture | x86_64 | 64-bit — rules out 32-bit specific exploits |
| Uptime | 4 hours 27 minutes | Recently started — fewer logged events to review |
| Users | 1 active | Single user session — low chance of interruption |

---

### Test 4 — VM Detection

**Raw output (key lines):**
```
VMware Virtual Platform
Manufacturer: VMware, Inc.
Product Name: VMware Virtual Platform
Serial Number: VMware-56 4d c7 9d 4c cd f4 a1-65 d5 8d bc f4 ff 0b f9
Description: VMware SVGA II
00:0f.0 VGA compatible controller: VMware SVGA II Adapter
```

**Attacker interpretation:**

Trinity is confirmed as a VMware Virtual Machine. This is critical intelligence for two reasons:

1. **Sandbox detection** — sophisticated malware checks for VM indicators before executing. If this were a sandbox, the malware would abort. Knowing the target is a VM tells the attacker their tools will behave normally.
2. **Escape potential** — VMware VM escape vulnerabilities (rare but documented) become relevant if the attacker wants to reach the hypervisor host (Zion).

The VMware serial number is also a unique identifier that could be used to track this specific VM across engagements.

---

### Test 8 — Hostname

**Raw output:**
```
kali
```

**Attacker interpretation:**

Default hostname unchanged from Kali installation. In an enterprise environment, hostnames reveal role — `DC01` means domain controller, `FILESERVER` means file server, `PAYROLL-PC` means sensitive financial data. `kali` means default workstation, no special role, but confirms the operator hasn't hardened basic system settings.

---

### Test 12 — Environment Variables (Highest Value)

**Key findings from raw output:**

| Variable | Value | Attacker Significance |
|---|---|---|
| `USER` | `kali` | Username confirmed |
| `SHELL` | `/usr/bin/zsh` | ZSH shell — attacker uses zsh-compatible syntax |
| `SSH_AUTH_SOCK` | `/home/kali/.ssh/agent/s.RDJpj98jBr...` | **SSH agent is running** |
| `SSH_AGENT_PID` | `1463` | SSH agent process ID — can be targeted directly |
| `PATH` | `/opt/microsoft/powershell/7:...` | **PowerShell installed at /opt/microsoft/powershell/7** |
| `DISPLAY` | `:0.0` | X11 display active — screenshot/keylog capability |
| `HOME` | `/home/kali` | Home directory confirmed |
| `XDG_SESSION_TYPE` | `x11` | X11 session — not Wayland |
| `POWERSHELL_TELEMETRY_OPTOUT` | `1` | Operator disabled PS telemetry — security conscious user |

**The SSH agent is the most significant finding.**

An active SSH agent (`SSH_AUTH_SOCK` present) means SSH keys may be loaded in memory. An attacker can hijack the SSH agent socket to authenticate to other machines using the victim's loaded keys — without ever seeing the private key file or needing a password. This is a direct lateral movement path.

**Attack path unlocked:** SSH agent hijacking → authenticate to other machines on the network as the kali user → expand foothold beyond Trinity.

---

## Combined Intelligence Picture (After 3 Techniques)

| Category | Finding | Attacker Action |
|---|---|---|
| Identity | kali / uid=1000 / sudo group | Privilege escalation path via sudo confirmed |
| Defenses | No EDR, no Wazuh, no AV | Proceed without evasion — no detection risk |
| OS | Kali 2026.2 / kernel 6.19.14 | Check kernel CVEs for local privesc |
| Hardware | VMware Virtual Platform | VM confirmed — tools will execute normally |
| Network | SSH agent running | SSH agent hijacking lateral movement available |
| Execution | PowerShell installed | Can use pwsh for cross-platform attack scripts |
| Monitoring | No SIEM, no auditd visible | Zero logging of attacker activity |

The attacker now has a complete profile of Trinity and multiple identified attack paths. Next step: T1049 (Network Connection Discovery) — map what other machines Trinity is talking to before moving laterally.

---

## VECTR Documentation

| Field | Value |
|---|---|
| Environment | Home_LAB |
| Assessment | Phase 1 - System Information Discovery |
| Campaign | T1082 - System Information Discovery |
| Defense Tool | Phase 1 Baseline (Manual Observation) |
| Technique | T1082 — System Information Discovery |
| Phase | Discovery |
| Status | Completed |
| Outcome | **None** |
| Defense Success | **Unsuccessful** |
| Attack Source | Trinity (Kali Linux 2026.2) |
| Attack Target | Trinity (local — self) |

No alerts. No logs. No blocks. Full system fingerprint retrieved silently including active SSH agent discovery.

---

## Detection Opportunity (Future Wazuh Rule)

**Sigma rule concept:**
```yaml
title: System Information Discovery - Linux
status: experimental
description: Detects sequential execution of system fingerprinting commands
logsource:
  category: process_creation
  product: linux
detection:
  selection:
    CommandLine|contains:
      - 'uname -a'
      - 'cat /etc/os-release'
      - 'cat /etc/lsb-release'
      - 'hostname'
      - 'env'
  timeframe: 30s
  condition: selection | count() > 2
falsepositives:
  - System administrators running diagnostic scripts
level: medium
tags:
  - attack.discovery
  - attack.t1082
```

The key detection indicator is multiple fingerprinting commands executed in rapid succession within a short timeframe. A single `hostname` command is not suspicious. Five fingerprinting commands in 30 seconds from a shell spawned by PowerShell is.

---

## Phase 2 Plan — CALDERA Integration

In Phase 2, T1082 will be chained with T1087.001 and T1057 in a single CALDERA adversary profile executed against Sentinel:

1. T1087.001 → T1057 → T1082 run in sequence automatically
2. Wazuh watches for the full discovery chain
3. Detection goal: alert on the behavioral pattern of all three techniques together, not just individual commands
4. VECTR outcomes updated for the full chain

---

## Remediation Notes

- Deploy auditd to capture process execution events
- Alert on sequential fingerprinting commands within short timeframes
- Restrict SSH agent forwarding where not explicitly required
- Set a non-default hostname to reduce OS fingerprinting confidence
- Implement process execution logging via Wazuh

---

## References

- [MITRE ATT&CK T1082](https://attack.mitre.org/techniques/T1082/)
- [Atomic Red Team T1082](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.md)
- [VECTR Community Edition](https://vectr.io)
- [MITRE CALDERA](https://caldera.mitre.org)
