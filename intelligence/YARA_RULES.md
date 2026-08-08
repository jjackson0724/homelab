# YARA Rules - Matrix Homelab

Detection signatures written for Phase 2-4 ATT&CK techniques.
Pending deployment to Seraph once Nebuchadnezzar is built.

---

## T1003.001 - Credential Dumping: LSASS Memory

```yara
rule Credential_Dumping_Tool {

    meta:
        description = "Detects credential dumping tools targeting LSASS"
        author = "Jarron Jackson"
        mitre_attack = "T1003.001"
        phase = "Phase 2"

    strings:
        $s1 = "lsass.exe" nocase
        $s2 = "NtReadVirtualMemory"
        $s3 = "MiniDumpWriteDump"
        $s4 = "SeDebugPrivilege"

    condition:
        2 of them
}
```

---

## T1053.005 - Scheduled Task Persistence

```yara
rule Scheduled_Task_Persistence {

    meta:
        description = "Detects scheduled task creation for persistence"
        author = "Jarron Jackson"
        mitre_attack = "T1053.005"
        phase = "Phase 2"

    strings:
        $s1 = "schtasks" nocase
        $s2 = "/create" nocase
        $s3 = "/sc" nocase
        $s4 = "SYSTEM" nocase

    condition:
        3 of them
}
```

---

## T1562.001 - Disable Security Tools

```yara
rule Disable_Security_Tools {

    meta:
        description = "Detects attempts to disable security tools or AV"
        author = "Jarron Jackson"
        mitre_attack = "T1562.001"
        phase = "Phase 2"

    strings:
        $s1 = "Set-MpPreference" nocase
        $s2 = "DisableRealtimeMonitoring" nocase
        $s3 = "DisableAntispyware" nocase
        $s4 = "net stop" nocase
        $s5 = "sc stop" nocase

    condition:
        2 of them
}
```

---

## T1021.002 - Lateral Movement: SMB/Admin Shares

```yara
rule Lateral_Movement_SMB {

    meta:
        description = "Detects lateral movement via SMB admin shares"
        author = "Jarron Jackson"
        mitre_attack = "T1021.002"
        phase = "Phase 4"

    strings:
        $s1 = "ADMIN$" nocase
        $s2 = "IPC$" nocase
        $s3 = "net use" nocase
        $s4 = "\\\\\\\\*\\\\ADMIN$" nocase

    condition:
        2 of them
}
```

---

## T1558.003 - Kerberoasting

```yara
rule Kerberoasting_Activity {

    meta:
        description = "Detects Kerberoasting tools and activity"
        author = "Jarron Jackson"
        mitre_attack = "T1558.003"
        phase = "Phase 4"

    strings:
        $s1 = "Invoke-Kerberoast" nocase
        $s2 = "GetUserSPNs" nocase
        $s3 = "KerberosRequestorSecurityToken" nocase
        $s4 = "RC4-HMAC" nocase

    condition:
        2 of them
}
```

---

## References

- [YARA Documentation](https://yara.readthedocs.io)
- [MITRE ATT&CK](https://attack.mitre.org)
- [Wazuh YARA Integration](https://documentation.wazuh.com/current/user-manual/capabilities/malware-detection/yara-integration.html)
