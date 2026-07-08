<img width="1024" height="559" alt="NebRender" src="https://github.com/user-attachments/assets/c42aaf30-3664-444b-bae4-8c0e43b3c19e" />
\ # Nebuchadnezzar (Neb) — Build Specification

Matrix-themed Proxmox homelab server and Oracle AI inference node.
RGB theme: Matrix green (#00FF88) unified across all components via Corsair iCUE and Lian Li L-Connect.

---

## Final Parts List

| Component | Part | Est. Price |
|---|---|---|
| CPU | AMD Ryzen 7 7700 (65W, 8c/16t, AM5) | $237 |
| Cooler | Thermalright Phantom Spirit 120 SE Air Cooler | $35 |
| Motherboard | GIGABYTE B650 AORUS ELITE AX (AM5, ATX) | $150 |
| RAM | Corsair Vengeance RGB 64GB (2x32GB) DDR5-6000 CL36 | ~$290 |
| Storage 1 | Samsung 990 Pro 2TB NVMe M.2 (OS + VMs) | $370 |
| Storage 2 | Crucial/TeamGroup 2TB NVMe (Splunk logs + VM backups) | ~$80 |
| GPU | MSI RTX 3060 Ventus 12GB (Oracle AI node) | $300 |
| Case | Geometric Future M5 Black/Green (5 fans included) | $160 |
| PSU | Corsair RM750x 750W 80+ Gold Fully Modular | $140 |
| Cables | CableMod custom sleeved black/green | $80 |
| ARGB | Interior ARGB LED strips | $20 |
| GPU Mount | Vertical GPU mount bracket | $30 |
| NIC | Intel I226 PCIe 2.5GbE (Amazon) | ~$35 |
| **Total** | | **~$1,927** |

---

## PCPartPicker List

https://pcpartpicker.com/list/xQcrMF

---

## Why These Parts

| Decision | Reason |
|---|---|
| Ryzen 7 7700 (non-X) | 65W TDP runs cool 24/7, no overclocking needed for Proxmox |
| Thermalright air cooler | No pump failure risk for 24/7 server — more reliable than AIO long term |
| B650 vs X670E | Right-sized for non-overclocking workload, saves $60 |
| 2x32GB RAM only | AMD Ryzen 7000 unstable at DDR5-6000 with 4 DIMMs — 2 sticks = full speed + stability |
| Budget log storage | Splunk indices don't need NVMe speeds — saves $50 vs second 990 Pro |
| Geometric Future M5 | Pre-themed black/green exterior, 5 ARGB fans included, tempered glass |
| Intel I226 NIC | Onboard Realtek RTL8125B incompatible with Proxmox bridging |
| RTX 3060 12GB | 12GB VRAM handles 7B-13B LLM inference without offloading to system RAM |

---

## Aesthetic

- Case: Geometric Future M5 — black with green panels, tempered glass
- RGB color: #00FF88 (Matrix green) set in Lian Li L-Connect for case fans
- Custom black/green sleeved cables (CableMod)
- Vertical GPU mount so RTX 3060 faces the glass
- ARGB strips lining interior edges

---

## Proxmox VM Layout

| VM | Role | RAM | vCPU |
|---|---|---|---|
| Oracle | AI inference — Ollama/vLLM + RTX 3060 passthrough | 16GB | 4 |
| Morpheus | Domain controller (Active Directory) | 4GB | 2 |
| Seraph | Wazuh/Splunk SIEM + MISP | 8GB | 4 |
| Trinity | Kali Linux attacker machine | 4GB | 2 |
| Host reserve | Proxmox overhead | 4GB | — |

---

## Setup Notes

- **RAM:** 2x32GB only — never use 4x16GB on AM5 DDR5-6000, causes instability
- **GPU passthrough:** Enable IOMMU in BIOS (AMD SVM) → blacklist Nvidia drivers on Proxmox host → configure VFIO → assign GPU to Oracle VM
- **NIC:** Use Intel I226 add-in card for all Proxmox VM bridging — ignore onboard Realtek
- **Storage 1:** Samsung 990 Pro for Proxmox OS and VM images
- **Storage 2:** Budget NVMe for Splunk indices and VM backups — Splunk logs grow exponentially
- **Resource limits:** Set strict vCPU and RAM limits per VM in Proxmox — Seraph/Splunk will starve Oracle under heavy log indexing without limits
- **Proxmox install:** Flash ISO to USB via Rufus on Zion, boot Neb from USB
- **RGB:** Set Geometric Future M5 fans to #00FF88 in L-Connect, set Corsair RAM to #00FF88 in iCUE

---

## Upgrade Path

| Upgrade | Trigger | Cost |
|---|---|---|
| RAM 64GB → 128GB | DDR5 prices drop | ~$290 additional |
| RTX 3060 → RTX 4070 12GB | Need faster inference | ~$280 additional |
| Add boot NVMe | Budget allows | ~$70 |

---

## AI Review Notes

- **Gemini:** Flagged 4x16GB RAM instability — fixed with 2x32GB kit
- **Third reviewer:** Flagged X670E overkill, AIO unreliable 24/7, RAM overpriced — all fixed
- **AI TWO:** Rated 7.5/10 — "Solid foundation, needs RAM gains" — upgrade path documented above
- **RTX 3060 12GB:** Adequate for home inference (VRAM is king for LLM) — upgrade to 4070 optional

---

## Status Checklist

- [ ] Parts sourced
- [ ] Build complete
- [ ] Proxmox installed
- [ ] Oracle VM configured
- [ ] GPU passthrough working
- [ ] Morpheus DC deployed
- [ ] Seraph SIEM deployed
- [ ] MISP deployed on Seraph
- [ ] Trinity Kali configured
- [ ] Matrix green RGB unified
- [ ] Splunk log storage configured
- [ ] Intel NIC verified working in Proxmox
- [ ] Resource limits set per VM



