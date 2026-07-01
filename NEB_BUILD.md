<img width="1024" height="559" alt="NebRender" src="https://github.com/user-attachments/assets/c42aaf30-3664-444b-bae4-8c0e43b3c19e" />
\# Nebuchadnezzar (Neb) — Build Specification



Matrix-themed Proxmox homelab server and Oracle AI inference node.

RGB theme: Matrix green (#00FF88) unified across all components via Corsair iCUE.



\---



\## Parts List



| Component | Part | Est. Price |

|---|---|---|

| CPU | AMD Ryzen 7 7700 (65W, 8c/16t, AM5) | $237 |

| Cooler | Corsair iCUE H100i Elite RGB 240mm AIO | $120 |

| Motherboard | ASRock X670E PG Lightning (AM5, ATX) | $209 |

| RAM | Corsair Vengeance RGB 64GB (2x32GB) DDR5-6000 CL36 | \~$580 |

| Storage 1 | Samsung 990 Pro 2TB NVMe M.2 (OS + VMs) | $370 |

| Storage 2 | 2TB SATA SSD (Splunk logs + VM backups) | \~$80 |

| GPU | MSI RTX 3060 Ventus 12GB (Oracle AI node) | $300 |

| Case | Lian Li LANCOOL 216 RGB (black) | $90 |

| PSU | Corsair RM750x 750W 80+ Gold Fully Modular | $140 |

| Cables | CableMod custom sleeved black/green | $80 |

| ARGB | Interior ARGB LED strips | $20 |

| GPU Mount | Vertical GPU mount bracket | $30 |

| NIC | Intel I226 PCIe 2.5GbE (Amazon) | \~$35 |

| \*\*Total\*\* | | \*\*\~$2,291\*\* |



\---



\## Aesthetic



\- Case: Lian Li LANCOOL 216 RGB black with tempered glass panel

\- RGB color: #00FF88 (Matrix green) unified in Corsair iCUE

\- Custom black/green sleeved cables (CableMod)

\- Vertical GPU mount so RTX 3060 faces the glass

\- ARGB strips lining interior top and bottom edges

\- AIO radiator mounted top with green RGB fans



\---



\## Proxmox VM Layout



| VM | Role | RAM Allocation |

|---|---|---|

| Oracle | AI inference — Ollama/vLLM + RTX 3060 passthrough | 16GB |

| Morpheus | Domain controller (Active Directory) | 4GB |

| Seraph | Wazuh/Splunk SIEM node | 16GB |

| Trinity | Kali Linux attacker machine | 4GB |

| Host reserve | Proxmox overhead | 4GB |



\---



\## Setup Notes



\- RAM: use 2x32GB kit only — AMD Ryzen 7000 memory controller runs 4x DDR5 DIMMs unstably at 6000MHz. Two slots populated = full speed + stability + room to expand later

\- GPU passthrough: enable IOMMU in BIOS (AMD SVM), blacklist Nvidia drivers on Proxmox host, configure VFIO so Oracle VM gets exclusive GPU access

\- NIC: use Intel I226 add-in card for Proxmox bridging — ignore onboard Realtek RTL8125B

\- Storage 1: Samsung 990 Pro for Proxmox OS and VM images (fast NVMe)

\- Storage 2: cheap 2TB SATA SSD dedicated to Splunk indices and VM backups — Splunk logs grow exponentially and will fill Storage 1 quickly without this

\- Proxmox resource limits: set strict vCPU and RAM limits per VM so Seraph doesn't starve Oracle during heavy log indexing

\- RGB: set all Corsair components to #00FF88 in iCUE for unified Matrix theme

\- Proxmox ISO: flash to USB via Rufus on Zion, boot Neb from USB to install



\---



\## Architecture Notes 



\- RTX 3060 12GB VRAM handles 7B and 13B parameter LLMs without offloading to system RAM

\- Purple team pipeline: Morpheus (AD) feeds logs into Seraph (Wazuh/Splunk) while Trinity attacks and Sentinel is the target — mirrors real SOC infrastructure

\- Zion manages Neb headlessly via browser (Proxmox web UI at https://192.168.x.x:8006)

\- CPU contention expected under heavy load — mitigate with Proxmox resource limits per VM



\---



\## PCPartPicker List



https://pcpartpicker.com/list/xQcrMF



\---



\## Status



\- \[ ] Parts sourced

\- \[ ] Build complete

\- \[ ] Proxmox installed

\- \[ ] Oracle VM configured

\- \[ ] GPU passthrough working

\- \[ ] Morpheus DC deployed

\- \[ ] Seraph SIEM deployed

\- \[ ] Trinity Kali configured

\- \[ ] Matrix green RGB unified

\- \[ ] Splunk log storage configured

