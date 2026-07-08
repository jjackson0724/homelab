\# YARA Rules — Matrix Homelab Intelligence Layer



YARA is the gold standard tool used by threat intelligence analysts at the FBI, CIA, and private threat intel firms to scan file systems and memory for malware signatures. This file documents custom YARA rules written during purple team simulations.



\---



\## What is YARA



YARA rules are pattern-matching signatures that identify malware, tools, or artifacts based on strings, byte sequences, or behavioral patterns. A YARA rule can detect a specific hacking tool, a malware family, or a custom artifact generated during an attack simulation.



\---



\## Rule Structure



```yara

rule Rule\_Name {

&#x20;   meta:

&#x20;       description = "What this rule detects"

&#x20;       author = "Jarron Jackson"

&#x20;       date = "YYYY-MM-DD"

&#x20;       mitre\_attack = "T1234.001"

&#x20;       phase = "Phase 1 / 2 / 3 / 4"

&#x20;   strings:

&#x20;       $string1 = "suspicious string"

&#x20;       $hex1 = { 4D 5A 90 00 }

&#x20;       $regex1 = /malicious\[0-9]+/

&#x20;   condition:

&#x20;       any of them

}

```



\---



\## Phase 2 Rules — Credential Access



```yara

rule Mimikatz\_Strings {

&#x20;   meta:

&#x20;       description = "Detects common Mimikatz strings in memory or on disk"

&#x20;       author = "Jarron Jackson"

&#x20;       mitre\_attack = "T1003.001 — LSASS Memory"

&#x20;       phase = "Phase 2"

&#x20;       reference = "https://attack.mitre.org/techniques/T1003/001/"

&#x20;   strings:

&#x20;       $s1 = "sekurlsa::logonpasswords"

&#x20;       $s2 = "privilege::debug"

&#x20;       $s3 = "lsadump::sam"

&#x20;       $s4 = "mimikatz"

&#x20;       $s5 = "mimilib"

&#x20;   condition:

&#x20;       any of them

}

```



```yara

rule Credential\_Dumping\_Tool {

&#x20;   meta:

&#x20;       description = "Detects credential dumping tools targeting LSASS"

&#x20;       author = "Jarron Jackson"

&#x20;       mitre\_attack = "T1003.001"

&#x20;       phase = "Phase 2"

&#x20;   strings:

&#x20;       $s1 = "lsass.exe" nocase

&#x20;       $s2 = "NtReadVirtualMemory"

&#x20;       $s3 = "MiniDumpWriteDump"

&#x20;       $s4 = "SeDebugPrivilege"

&#x20;   condition:

&#x20;       2 of them

}

```



\---



\## Phase 2 Rules — Persistence



```yara

rule Scheduled\_Task\_Persistence {

&#x20;   meta:

&#x20;       description = "Detects artifacts from scheduled task persistence"

&#x20;       author = "Jarron Jackson"

&#x20;       mitre\_attack = "T1053.005 — Scheduled Task"

&#x20;       phase = "Phase 2"

&#x20;   strings:

&#x20;       $s1 = "schtasks" nocase

&#x20;       $s2 = "/create" nocase

&#x20;       $s3 = "/sc onlogon" nocase

&#x20;       $s4 = "HKLM\\\\Software\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Schedule"

&#x20;   condition:

&#x20;       2 of them

}

```



\---



\## Phase 3 Rules — Defense Evasion



```yara

rule PowerShell\_Obfuscation {

&#x20;   meta:

&#x20;       description = "Detects common PowerShell obfuscation patterns"

&#x20;       author = "Jarron Jackson"

&#x20;       mitre\_attack = "T1027 — Obfuscated Files or Information"

&#x20;       phase = "Phase 3"

&#x20;   strings:

&#x20;       $s1 = "FromBase64String" nocase

&#x20;       $s2 = "IEX" nocase

&#x20;       $s3 = "Invoke-Expression" nocase

&#x20;       $s4 = "-EncodedCommand" nocase

&#x20;       $s5 = "System.Reflection.Assembly" nocase

&#x20;   condition:

&#x20;       2 of them

}

```



\---



\## Phase 4 Rules — Active Directory Attacks



```yara

rule Kerberoasting\_Tool {

&#x20;   meta:

&#x20;       description = "Detects Kerberoasting tool artifacts"

&#x20;       author = "Jarron Jackson"

&#x20;       mitre\_attack = "T1558.003 — Kerberoasting"

&#x20;       phase = "Phase 4"

&#x20;   strings:

&#x20;       $s1 = "GetUserSPNs" nocase

&#x20;       $s2 = "Invoke-Kerberoast" nocase

&#x20;       $s3 = "KerberosRequestorSecurityToken" nocase

&#x20;       $s4 = "RC4\_HMAC\_MD5"

&#x20;   condition:

&#x20;       any of them

}

```



```yara

rule DCSync\_Attack {

&#x20;   meta:

&#x20;       description = "Detects DCSync attack artifacts from Mimikatz"

&#x20;       author = "Jarron Jackson"

&#x20;       mitre\_attack = "T1003.006 — DCSync"

&#x20;       phase = "Phase 4"

&#x20;   strings:

&#x20;       $s1 = "lsadump::dcsync" nocase

&#x20;       $s2 = "DRSGetNCChanges"

&#x20;       $s3 = "/domain:" nocase

&#x20;       $s4 = "krbtgt" nocase

&#x20;   condition:

&#x20;       2 of them

}

```



\---



\## How to Run YARA Rules



Install YARA on Trinity (Kali):

```bash

sudo apt install yara

```



Scan a file:

```bash

yara YARA\_RULES.yar /path/to/suspicious/file

```



Scan a directory recursively:

```bash

yara -r YARA\_RULES.yar /path/to/directory

```



Scan memory (requires root):

```bash

yara -r YARA\_RULES.yar /proc

```



\---



\## Rule Development Log



| Rule Name | ATT\&CK Technique | Phase | Date Written | Tested |

|---|---|---|---|---|

| Mimikatz\_Strings | T1003.001 | Phase 2 | | |

| Credential\_Dumping\_Tool | T1003.001 | Phase 2 | | |

| Scheduled\_Task\_Persistence | T1053.005 | Phase 2 | | |

| PowerShell\_Obfuscation | T1027 | Phase 3 | | |

| Kerberoasting\_Tool | T1558.003 | Phase 4 | | |

| DCSync\_Attack | T1003.006 | Phase 4 | | |

