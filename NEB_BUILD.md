<img width="1024" height="559" alt="NebRender" src="https://github.com/user-attachments/assets/c42aaf30-3664-444b-bae4-8c0e43b3c19e" />
\ # Nebuchadnezzar (Neb) — Build Specification

Matrix-themed Proxmox homelab server and Oracle AI inference node.
RGB theme: Matrix green (#00FF88) unified across all components via Corsair iCUE and Lian Li L-Connect.

**AI Rating: 9.5/10** — RTX 4070 upgrade transforms this into a legitimate AI inference and purple team platform.

---

## Final Parts List

| Component | Part | Est. Price | % of Build |
|---|---|---|---|
| CPU | AMD Ryzen 7 7700 (65W, 8c/16t, AM5) | $237 | 10.7% |
| Cooler | Thermalright Phantom Spirit 120 SE | $35 | 1.6% |
| Motherboard | GIGABYTE B650 AORUS ELITE AX (AM5, ATX) | $150 | 6.8% |
| RAM | Corsair Vengeance RGB 64GB (2x32GB) DDR5-6000 CL36 | ~$290 | 13.1% |
| Storage 1 | Samsung 990 Pro 2TB NVMe M.2 (OS + VMs) | $370 | 16.8% |
| Storage 2 | Crucial 2TB NVMe (Splunk logs + VM backups) | ~$80 | 3.6% |
| GPU | MSI RTX 4070 12GB (Oracle AI node) | $580 | 26.3% |
| Case | Geometric Future M5 Black/Green (5 fans included) | $160 | 7.2% |
| PSU | Corsair RM750x 750W 80+ Gold Fully Modular | $140 | 6.3% |
| Cables | CableMod custom sleeved black/green | $80 | 3.6% |
| ARGB | Interior ARGB LED strips | $20 | 0.9% |
| GPU Mount | Vertical GPU mount bracket | $30 | 1.4% |
| NIC | Intel I226 PCIe 2.5GbE | ~$35 | 1.6% |
| **Total** | | **~$2,207** | **100%** |

---

## PCPartPicker List

https://pcpartpicker.com/list/xQcrMF

---

## Why These Parts

| Decision | Reason |
|---|---|
| Ryzen 7 7700 (non-X) | 65W TDP runs cool 24/7, no overclocking needed for Proxmox |
| Thermalright air cooler | No pump failure risk for 24/7 server — more reliable than AIO long term |
| B650 vs X670E | Right-sized for non-overclocking workload, saves $60. IOMMU verified on Proxmox |
| 2x32GB RAM only | AMD Ryzen 7000 unstable at DDR5-6000 with 4 DIMMs — 2 sticks = full speed + stability |
| Budget log storage | Splunk indices don't need NVMe speeds — saves $50 vs second 990 Pro |
| RTX 4070 12GB | Ada Lovelace architecture — modern tensor cores, DLSS 3, faster CUDA vs RTX 3060 |
| Geometric Future M5 | Pre-themed black/green exterior, 5 ARGB fans included, tempered glass |
| Intel I226 NIC | Onboard Realtek RTL8125B incompatible with Proxmox bridging |

---

## GPU — RTX 4070 vs RTX 3060 Comparison

| Metric | RTX 3060 12GB | RTX 4070 12GB | Winner |
|---|---|---|---|
| Architecture | Ampere | Ada Lovelace | 4070 |
| VRAM | 12GB | 12GB | Tie |
| CUDA Cores | 3,584 | 5,888 | 4070 |
| Tensor Cores | 3rd gen | 4th gen | 4070 |
| LLM Inference | Good | Excellent | 4070 |
| Price | $300 | $580 | 3060 |
| For Oracle AI | Adequate | Optimal | 4070 |

---

## Aesthetic

- Case: Geometric Future M5 — black with green panels, tempered glass
- RGB color: #00FF88 (Matrix green) set in Lian Li L-Connect for case fans
- Custom black/green sleeved cables (CableMod)
- Vertical GPU mount so RTX 4070 faces the glass
- ARGB strips lining interior edges

---

## Proxmox VM Layout

| VM | Role | RAM | vCPU |
|---|---|---|---|
| Oracle | AI inference — Ollama/vLLM + RTX 4070
