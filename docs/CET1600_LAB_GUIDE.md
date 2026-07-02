# CET 1600 - Introduction to Networks: Lab Guide
**Author:** Jarron Jackson | **Lab:** Matrix Homelab | **Semester:** Fall 2026

## Lab 1 - Homelab Network Topology Diagram

### What You Will Do
Build a complete network topology diagram of the Matrix homelab. Document current state and planned Phase 5 segmented architecture with OPNsense VLANs.

Current topology:
- Home router: 192.168.1.0/24
- VMware NAT: 192.168.161.0/24 (Trinity/VM segment)
- Sentinel: home network via Wi-Fi
- Zion: home network at 192.168.1.35

Planned Phase 5:
- VLAN 10 - Attacker (Trinity)
- VLAN 20 - Target (Sentinel)
- VLAN 30 - Management (Zion/Seraph)
- VLAN 40 - AI/Oracle

### Skills Learned
- Network topology documentation
- IP addressing and subnetting
- VLAN design and segmentation
- Traffic flow analysis

### Purple Team Relevance
T1049 confirmed Trinity segment. A full topology diagram shows exactly what an attacker maps during discovery. VLAN design limits lateral movement paths.

### Artifacts
labs/cet1600/homelab-network-topology.md
labs/cet1600/homelab-network-diagram.png

### NIST CSF
ID.AM-3, PR.AC-5

## Lab 2 - Subnetting Documentation

### What You Will Do
Document the subnetting scheme for the planned Phase 5 VLAN architecture.

### Artifact
labs/cet1600/vlan-subnet-scheme.md

## Lab 3 - Protocol Analysis with Wireshark

### What You Will Do
Capture traffic during the Phase 2 Sentinel attack chain. Document protocol signatures for each ATT&CK technique.

### Skills Learned
- Protocol identification (TCP, UDP, ICMP, SMB, NTLM)
- Packet capture and filtering
- Network forensics methodology

### Artifact
labs/cet1600/protocol-analysis-attack-chain.md

### NIST CSF
DE.CM-1, DE.AE-3
