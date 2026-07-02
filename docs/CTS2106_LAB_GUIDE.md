# CTS 2106 - Fundamentals Linux Operating System: Lab Guide
**Author:** Jarron Jackson | **Lab:** Matrix Homelab | **Semester:** Spring 2027

---

## Lab 1 - Linux Command Reference Guide

### What You Will Do
Build a comprehensive Linux command reference from actual attack session output. For every command run during Phase 1 and Phase 2, document what it does, syntax, example output, and defensive counterpart.

Categories to cover:
- User/group management (useradd, usermod, groups, id, passwd)
- Process management (ps, top, kill, systemctl)
- File system (ls, find, chmod, chown, cat, grep)
- Network (ss, netstat, ip, ping, nmap)
- System info (uname, uptime, hostname, env, lsof)
- Security (iptables, sudo, auditctl)

### Skills Learned
- Linux command mastery through real usage
- Command syntax documentation
- Offensive/defensive command pairing
- Shell scripting fundamentals

### Purple Team Relevance
Every command in the reference guide was used in an actual attack session. The learning is grounded in real execution, not abstract memorization.

### Artifact
labs/cts2106/linux-command-reference.md

### NIST CSF
PR.AC-1, PR.IP-1

---

## Lab 2 - Shell Scripting for Purple Team

### What You Will Do
Write bash scripts to automate repetitive purple team tasks. Start with a script that runs the full Phase 1 discovery chain and logs output to a structured file.

Example script structure:
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    OUTPUT="/tmp/discovery_$TIMESTAMP.txt"
    echo "=== T1087.001 ===" >> $OUTPUT
    id >> $OUTPUT
    groups >> $OUTPUT
    echo "=== T1057 ===" >> $OUTPUT
    ps aux >> $OUTPUT
    echo "=== T1082 ===" >> $OUTPUT
    uname -a >> $OUTPUT
    echo "=== T1049 ===" >> $OUTPUT
    ss -antp >> $OUTPUT

### Skills Learned
- Bash scripting fundamentals
- Script automation for security tasks
- Output formatting and logging
- Error handling in scripts

### Artifact
scripts/phase1-discovery.sh

---

## Lab 3 - Linux System Administration Reference

### What You Will Do
Document Linux administration tasks performed across the homelab - Trinity hardening, Seraph Wazuh configuration, and Proxmox management commands. Build as an operations runbook.

### Artifact
labs/cts2106/linux-admin-runbook.md
