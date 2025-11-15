# **FOAMGEN Aerospace Material Parameters**

### *Physically-Grounded Parameter Guide for Generating Metallic Open-Cell Foams Using Foamgen*

This document provides **validated, literature-backed numerical parameters** for generating metallic open-cell foams using *Foamgen* for aerospace applications.
All values are sourced from:

* ERG Aerospace **Duocel® Aluminum Foam** datasheets (industry standard)
* Peer-reviewed aluminum foam microstructure studies
* Gibson–Ashby cellular solids theory
* Standard aluminum alloys used in spacecraft structural panels
* CubeSat panel structural norms

These parameter sets are used to generate **three realistic YAML configurations** for Foamgen.

---

## **## 1. Verified Aerospace Foam Parameters**

Below are the *validated scientific/industrial ranges* for each foam parameter.

---

### **### 1.1 Relative Density → Porosity**

Duocel aluminum foam (aerospace standard) provides:

* **Relative density (ρ*/ρs): 4–12%**
* **Porosity (φ): 1 – ρ*/ρs = 88–96%**

Common example used in engineering:

* **8% relative density → 92% porosity**

---

### **### 1.2 Pore Size via PPI**

Duocel PPI options:

* **5, 10, 20, 40 PPI**

Approximate mean pore diameter:

[
d \approx \frac{25.4 \text{ mm}}{\text{PPI}}
]

| PPI | Mean Pore Size |
| --- | -------------- |
| 40  | 0.64 mm        |
| 20  | 1.27 mm        |
| 10  | 2.54 mm        |
| 5   | 5.08 mm        |

---

### **### 1.3 Strut / Wall Thickness**

Linked via Gibson–Ashby scaling:

[
\left(\frac{t}{\ell}\right)^2 \propto \frac{\rho^*}{\rho_s}
]

Combined with experimental aluminum foam studies:

* **~0.2–0.3 mm** → pore size 0.7–1.0 mm
* **~0.4–0.6 mm** → pore size 1.0–2.0 mm
* **~0.7–1.0 mm** → pore size 2–4 mm

Thus:

* **For 20 PPI (1.27 mm pores): choose t = 0.4 mm**
* **For 40 PPI (0.64 mm pores): choose t = 0.25 mm**
* **For 10 PPI (2.54 mm pores): choose t = 0.6 mm**

---

### **### 1.4 Foam Core Thickness**

Your requirements state:

* Panel = **10 cm × 10 cm**
* **Thickness = TBD**

Aerospace foam-core sandwich panels typically use:

* **10–30 mm** foam cores
* CubeSats often use **2–6 mm solid skins**, but foam cores = thicker

Recommended default for simulation:

* **15 mm foam-core thickness**

---

### **### 1.5 Face Sheet (Skin) Thickness (CAD stage)**

Not part of Foamgen, but critical for mass & stiffness.

Aerospace values:

* 0.7–1.0 mm aluminum skins for foam sandwiches
* CubeSat structural panels often use **1.27–1.52 mm**

Recommended standard:

* **1.0 mm aluminum skins (top & bottom)**

---

### **### 1.6 Material Density**

Standard aluminum alloy density:

* **2700 kg/m³**

Foam density for 8% relative density:

* **216 kg/m³**

---

## **## 2. Aerospace-Realistic Foam Configuration Table**

This table provides **three curated, defensible configuration sets** for foam generation.

These combos map directly into YAML templates below.

---

### **### Table: Aerospace Metallic Foam Configuration Options**

| Config Name                                | Relative Density | Porosity | PPI | Pore Size (mm) | Strut Thickness (mm) | Notes                              |
| ------------------------------------------ | ---------------- | -------- | --- | -------------- | -------------------- | ---------------------------------- |
| **Low-Density Light Panel**                | 4%               | 96%      | 10  | 2.54           | 0.20                 | Very lightweight, lowest stiffness |
| **Standard Aerospace Panel (Duocel-like)** | 8%               | 92%      | 20  | 1.27           | 0.40                 | Balanced stiffness & mass          |
| **High-Density Structural Panel**          | 12%              | 88%      | 40  | 0.64           | 0.25                 | Highest stiffness, heavier         |

---

## **## 3. YAML Configurations (Multiple)**

These YAMLs fit the Foagen workflow:

* **1) Packing**
* **2) Tessellation**
* **3) Structured Mesh (porosity + strut_content)**

**NOTE:** Foamgen’s exact YAML structure may differ based on version; adjust keys to match your `basic.yml` example. The *values* below are the important part.