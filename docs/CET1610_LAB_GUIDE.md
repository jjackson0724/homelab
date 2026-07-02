# CET 1610 - Switch, Routing and Wireless Essentials: Lab Guide
**Author:** Jarron Jackson | **Lab:** Matrix Homelab | **Semester:** Fall 2026

## Lab 1 - OPNsense VM Deployment on Neb

### What You Will Do
Deploy OPNsense as a VM on Nebuchadnezzar. Configure inter-VLAN routing, WAN/LAN interfaces, and basic firewall rules.

OPNsense roles:
- WAN: home network uplink
- LAN: lab management network
- VLAN 10: Attacker segment (Trinity)
- VLAN 20: Target segment (Sentinel)
- VLAN 30: SIEM/Management (Seraph/Zion)

### Skills Learned
- Router/firewall deployment and configuration
- Inter-VLAN routing
- WAN/LAN interface configuration
- Firewall rule logic

### Purple Team Relevance
OPNsense is the network chokepoint between Trinity and Sentinel. Properly configured VLAN ACLs limit lateral movement paths.

### Artifacts
labs/cet1610/opnsense-deployment.md
labs/cet1610/vlan-acl-configuration.md

### NIST CSF
PR.AC-5, PR.PT-4

## Lab 2 - VLAN Segmentation

### What You Will Do
Configure VLAN segmentation on OPNsense. Test isolation by confirming Trinity cannot reach home network devices while still reaching Sentinel.

### Artifact
labs/cet1610/vlan-segmentation-lab.md

## Lab 3 - Wireless Security Analysis

### What You Will Do
Document home wireless network security posture. Identify WPA2/WPA3 configuration and SSID hardening.

### Artifact
labs/cet1610/wireless-security-review.md

### NIST CSF
PR.AC-3, DE.CM-1
