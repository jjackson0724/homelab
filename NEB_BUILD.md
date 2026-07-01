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

| RAM | Corsair Vengeance RGB 32GB DDR5-6000 CL36 | $480 |

| Storage | Samsung 990 Pro 2TB NVMe M.2 | $370 |

| GPU | MSI RTX 3060 Ventus 12GB (Oracle AI node) | $300 |

| Case | Lian Li LANCOOL 216 RGB (black) | $90 |

| PSU | Corsair RM750x 750W 80+ Gold Fully Modular | $140 |

| Cables | CableMod custom sleeved black/green | $80 |

| ARGB | Interior ARGB LED strips | $20 |

| GPU Mount | Vertical GPU mount bracket | $30 |

| NIC | Intel I226 PCIe 2.5GbE (Amazon \~$35) | $35 |

| \*\*Total\*\* | | \*\*\~$2,111\*\* |



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

| Seraph | Wazuh/Splunk SIEM node | 8GB |

| Trinity | Kali Linux attacker machine | 4GB |



\---



\## Setup Notes



\- Boot drive: separate NVMe recommended when budget allows (\~$70 for 500GB)

\- RAM: 32GB now, expand to 64GB when DDR5 prices drop

\- GPU passthrough: enable IOMMU in BIOS (AMD SVM), configure VFIO in Proxmox

\- NIC: use Intel I226 add-in card, ignore onboard Realtek RTL8125B for Proxmox bridging

\- RGB: set all Corsair components to #00FF88 in iCUE for unified Matrix theme

\- Proxmox ISO: flash to USB via Rufus on Zion, boot Neb from USB to install



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

\- \[ ] Matrix green RGB unified

