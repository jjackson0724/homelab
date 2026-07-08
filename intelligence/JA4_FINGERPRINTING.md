\# JA4/JA3 TLS Fingerprinting — Matrix Homelab Intelligence Layer



JA4 and JA3 are TLS fingerprinting techniques used by intelligence agencies and threat intel firms to identify malicious tools and C2 servers even when network traffic is fully encrypted. This file documents JA4/JA3 analysis conducted during purple team simulations.



\---



\## What is TLS Fingerprinting



When a client (malware, hacking tool, or browser) initiates a TLS connection, it sends a ClientHello packet that contains specific parameters — cipher suites, TLS version, extensions, and elliptic curves. These parameters are unique enough to fingerprint the tool or malware making the connection, even without decrypting the traffic.



\- \*\*JA3\*\* — Original fingerprinting method, MD5 hash of TLS ClientHello parameters

\- \*\*JA4\*\* — Improved successor to JA3, more granular and resistant to evasion



\---



\## Why Intelligence Agencies Use This



Nation-state actors encrypt their C2 traffic to avoid content inspection. JA4/JA3 fingerprinting allows analysts to identify the specific tool being used (Cobalt Strike, Metasploit, custom implant) based on how it initiates TLS connections — without ever decrypting a single byte.



FBI and NSA analysts use JA4 fingerprints to:

\- Identify C2 frameworks across global threat infrastructure

\- Link separate intrusions to the same tool or actor

\- Build detection rules that work on encrypted traffic



\---



\## Lab Setup — Capturing JA4 Fingerprints



\### Step 1: Capture traffic on Trinity during attack simulation



```bash

sudo tcpdump -i eth0 -w /tmp/attack\_capture.pcap

```



\### Step 2: Extract JA3 fingerprints with Zeek



Install Zeek on Trinity:

```bash

sudo apt install zeek

```



Run Zeek against your PCAP:

```bash

zeek -r /tmp/attack\_capture.pcap

cat ssl.log | zeek-cut ja3 ja3s id.orig\_h id.resp\_h

```



\### Step 3: Extract JA4 fingerprints with ja4plus



Install ja4plus:

```bash

git clone https://github.com/FoxIO-LLC/ja4.git

cd ja4/python

pip install -r requirements.txt

```



Run against your PCAP:

```bash

python ja4.py /tmp/attack\_capture.pcap

```



\### Step 4: Look up fingerprints



Search your JA3/JA4 hash at:

\- https://ja3er.com

\- https://sslbl.abuse.ch/ja3-fingerprints/



\---



\## Fingerprint Log



Document every JA3/JA4 fingerprint captured during lab simulations:



| Date | Tool Used | ATT\&CK Technique | JA3 Hash | JA4 Hash | Notes |

|---|---|---|---|---|---|

| | Invoke-AtomicRedTeam | T1071.001 | | | PowerShell C2 traffic |

| | Mimikatz | T1003.001 | | | LSASS access |

| | Sliver C2 | T1071.001 | | | Encrypted C2 beacon |

| | Metasploit | T1059.001 | | | Meterpreter TLS |



\---



\## Detection Rules Based on JA4 Fingerprints



\### Suricata rule example

```

alert tls any any -> any any (msg:"Known Cobalt Strike JA3 Fingerprint"; ja3.hash; content:"72a7c13520dc9f5035f20b3f3dd2e22c"; sid:1000001;)

```



\### Zeek detection script example

```zeek

event ssl\_client\_hello(c: connection, version: count, record\_version: count, possible\_ts: time, client\_random: string, session\_id: string, ciphers: index\_vec, comp\_methods: index\_vec) {

&#x20;   local ja3\_hash = sslv3\_hash(c);

&#x20;   if (ja3\_hash == "72a7c13520dc9f5035f20b3f3dd2e22c") {

&#x20;       print fmt("Cobalt Strike detected from %s", c$id$orig\_h);

&#x20;   }

}

```



\---



\## Phase Integration



| Phase | Activity | JA4 Task |

|---|---|---|

| Phase 1 | Network baseline | Capture normal TLS fingerprints from Zion and Sentinel |

| Phase 2 | Credential access | Capture JA3/JA4 from PowerShell C2 traffic |

| Phase 3 | Lateral movement | Fingerprint WMI and SMB TLS handshakes |

| Phase 4 | AD attacks | Fingerprint Kerberos and DCSync traffic patterns |



\---



\## Resources



\- JA4 GitHub: https://github.com/FoxIO-LLC/ja4

\- JA3 Database: https://ja3er.com

\- Zeek Network Monitor: https://zeek.org

\- SSL Blacklist: https://sslbl.abuse.ch

