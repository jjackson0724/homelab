\# OPSEC Infrastructure \& Covert Attack Simulation



Nation-state actors never attack a target directly from their home machine. They route attacks through a chain of compromised servers and redirectors so that defenders trace back to a dead end instead of the real origin. This file documents how to simulate and detect covert attack infrastructure in the Matrix Homelab.



\---



\## What is a Redirector



A redirector is an intermediate server that forwards attack traffic between the real attacker and the target. From the victim's perspective the attack appears to originate from the redirector — not the actual attacker.



```

Trinity (real attacker) → Redirector VM → Sentinel (target)

192.168.161.128          192.168.161.130   192.168.161.x

```



Real world examples:

\- APT28 (Russia) routed 2016 DNC hack through compromised servers in multiple countries

\- APT41 (China) uses cloud VPS providers as redirectors to obscure origin

\- Lazarus Group (North Korea) chains 3-5 hops before touching targets



\---



\## Lab Setup — Building the Redirector



\### Requirements

\- One additional lightweight Linux VM in VMware on Zion

\- Ubuntu Server 22.04 or Kali Linux (minimal install)

\- 1GB RAM, 20GB disk — very lightweight



\### Step 1 — Create Redirector VM in VMware



1\. Open VMware Workstation on Zion

2\. Create new VM — Ubuntu Server 22.04

3\. Allocate 1GB RAM, 20GB disk

4\. Set network adapter to same network as Trinity and Sentinel

5\. Name it \*\*Architect-Red\*\* or \*\*Redirector-01\*\*

6\. Note its IP address — this becomes your redirector IP



\### Step 2 — Configure socat Redirector



socat is a simple tool that forwards all traffic from one IP/port to another:



```bash

\# Install socat on redirector VM

sudo apt update \&\& sudo apt install socat -y



\# Forward all TCP traffic on port 4444 to Sentinel

sudo socat TCP-LISTEN:4444,fork TCP:192.168.161.x:4444



\# Forward all TCP traffic on port 443 to Sentinel (HTTPS C2)

sudo socat TCP-LISTEN:443,fork TCP:192.168.161.x:443

```



\### Step 3 — Configure iptables Redirector (alternative)



```bash

\# Enable IP forwarding

echo 1 | sudo tee /proc/sys/net/ipv4/ip\_forward



\# Forward all traffic destined for Sentinel through redirector

sudo iptables -t nat -A PREROUTING -p tcp --dport 4444 -j DNAT --to-destination 192.168.161.x:4444

sudo iptables -t nat -A POSTROUTING -j MASQUERADE

```



\### Step 4 — Run Attack Through Redirector



Instead of attacking Sentinel directly from Trinity, route through the redirector:



```bash

\# On Trinity — point your tool at the redirector IP instead of Sentinel

\# Example with netcat

nc 192.168.161.130 4444



\# Example with Metasploit — set LHOST to redirector

set LHOST 192.168.161.130

set LPORT 4444

```



\---



\## Blue Team — Tracing the Attack Back



This is the intelligence analyst exercise. After running the attack through the redirector, switch to blue team mode and trace it back to Trinity.



\### Step 1 — Network Forensics (PCAP Analysis)



```bash

\# Capture traffic on Seraph during attack

sudo tcpdump -i eth0 host 192.168.161.130 -w /tmp/redirector\_capture.pcap



\# Open in Wireshark and look for:

\# 1. Inbound connections TO the redirector

\# 2. Outbound connections FROM the redirector at same timestamp

\# Simultaneous in/out = forwarding traffic, not originating

```



\### Step 2 — Log Correlation



```bash

\# On redirector VM — check connection logs

sudo netstat -antp | grep ESTABLISHED

sudo ss -tunap



\# Cross reference timestamps:

\# Redirector received connection from 192.168.161.128 (Trinity) at T+0ms

\# Redirector forwarded connection to Sentinel at T+2ms

\# Same timestamp = hop chain confirmed

```



\### Step 3 — JA4 Fingerprint Matching



```bash

\# Extract JA4 from inbound connection to redirector

zeek -r /tmp/redirector\_capture.pcap

cat ssl.log | zeek-cut ja3 id.orig\_h id.resp\_h



\# Compare JA4 hash on inbound vs outbound connection

\# Matching fingerprint = same tool passed through

\# This proves Trinity is the origin even though Sentinel only saw the redirector

```



\### Step 4 — TTL Analysis



```bash

\# In Wireshark filter for packets from redirector to Sentinel

\# Check TTL values in IP header

\# Direct connection TTL: 64 (Linux) or 128 (Windows)

\# Forwarded connection TTL: 63 or lower (decremented by each hop)

\# Low TTL = additional hops in the chain

```



\### Step 5 — Attribution Conclusion



Document your findings:

```

Attack Origin:    192.168.161.128 (Trinity)

Redirector:       192.168.161.130 (Redirector-01)

Target:           192.168.161.x (Sentinel)

Evidence:         Timestamp correlation, JA4 fingerprint match, TTL analysis

Confidence:       HIGH

```



\---



\## Diamond Model — Redirector Exercise



\*\*Event ID:\*\* PT-OPSEC-001  

\*\*ATT\&CK Technique:\*\* T1090 — Proxy  

\*\*Phase:\*\* Phase 1 Intelligence Layer



\### Adversary

\- \*\*Simulated Actor:\*\* APT28 style operator

\- \*\*Intent:\*\* Obscure true attack origin to complicate attribution

\- \*\*Sophistication:\*\* Nation-state



\### Capability

\- \*\*Tool Used:\*\* socat / iptables

\- \*\*Delivery Method:\*\* Traffic forwarding through redirector VM

\- \*\*YARA Rule Written:\*\* No

\- \*\*Sigma Rule Written:\*\* No



\### Infrastructure

\- \*\*Real Attack Origin:\*\* Trinity — 192.168.161.128

\- \*\*Redirector:\*\* Redirector-01 — 192.168.161.130

\- \*\*Hop Count:\*\* 2

\- \*\*TLS Fingerprint (JA4):\*\* \[Capture and compare inbound vs outbound]



\### Victim

\- \*\*Target Machine:\*\* Sentinel

\- \*\*Perceived Attack Origin:\*\* 192.168.161.130 (redirector — not real origin)

\- \*\*Detected by Seraph:\*\* \[To be completed]

\- \*\*Attribution Successful:\*\* \[To be completed — did you trace it back to Trinity?]



\### Analyst Notes

Document how long attribution took, what evidence was most useful, and what gaps exist in your detection capability.



\---



\## Real World Context



| APT Group | Redirector Method | Attribution Technique Used |

|---|---|---|

| APT28 (Russia) | Compromised commercial VPS | Timestamp correlation across server logs |

| APT41 (China) | Cloud provider hop chain | JA3 fingerprint matching across hops |

| Lazarus (DPRK) | 3-5 hop chains | TTL analysis and BGP routing records |

| FIN7 (Criminal) | Bulletproof hosting | Infrastructure reuse across campaigns |



\---



\## Status



\- \[ ] Redirector VM created in VMware on Zion

\- \[ ] socat configured and tested

\- \[ ] Attack routed through redirector against Sentinel

\- \[ ] PCAP captured during attack

\- \[ ] Attribution exercise completed

\- \[ ] JA4 fingerprints compared inbound vs outbound

\- \[ ] Diamond Model writeup completed

\- \[ ] Logged to MISP

