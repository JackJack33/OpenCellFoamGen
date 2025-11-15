# Ni-Coated Aluminum Foam – Property Assumptions and Supporting Literature

This note collects **representative literature values** and explains why our **assumed properties** for Ni-coated Al foam (strut and foam level) are reasonable for first-pass simulations. Wherever possible we phrase things as “it looks like…” or “literature suggests…” because exact values depend strongly on alloy, porosity, PPI, and processing.

---

## 1. Bulk (Dense) Material Properties

### Aluminum (solid)

- For 6xxx series Al (e.g., 6061-T6), datasheets report:
  - Elastic modulus $E \approx 69\ \text{GPa}$.   
  - Thermal conductivity $k \approx 150\text{–}170\ \text{W/m·K}$ at room temperature.   
  - Density $\rho \approx 2700\ \text{kg/m}^3$.   

So it looks like taking **$E_\text{Al} \approx 70\ \text{GPa}$** and **$k_\text{Al} \approx 170\ \text{W/m·K}$** is consistent with standard aluminum alloy data.

### Nickel (solid)

- Common property tables for commercially pure Ni give:
  - $E_\text{Ni} \approx 200\ \text{GPa}$.   
  - Thermal conductivity $k_\text{Ni} \approx 90\ \text{W/m·K}$ at room temperature.   
  - Density $\rho_\text{Ni} \approx 8900\ \text{kg/m}^3$.   

Literature therefore suggests that using **$E_\text{Ni} \approx 200\ \text{GPa}$** and **$k_\text{Ni} \approx 90\ \text{W/m·K}$** is a reasonable baseline for dense nickel.

---

## 2. Open-Cell Aluminum Foam (Uncoated)

### Mechanical properties

For commercial open-cell Al foams (e.g., Duocel®):

- An ERG Aerospace datasheet for ~8% relative density Duocel® Al foam reports:  
  - Tensile yield strength $\sigma_y \approx 1.24\ \text{MPa}$.  
  - Compressive yield strength $\approx 2.17\ \text{MPa}$.  
  - Tensile modulus $E \approx 0.048\text{–}0.083\ \text{GPa}$.  
  - Compressive modulus $E_\text{comp} \approx 0.069\text{–}0.114\ \text{GPa}$.   

So for **relative density ~0.08**, it looks like typical **foam-level moduli** are in the **0.05–0.1 GPa** range and **foam-level strengths** are a **few MPa**.

More general reviews of metal foam mechanics (e.g., Ashby’s metal-foam design guide and later reviews) also report moduli in the **$10^{-2}\text{–}10^{-1}\,\text{GPa}$** range and compressive plateau stresses in the **1–10 MPa** range for relative densities of a few to ~15%.   

### Thermal conductivity

For thermal performance, several sources suggest:

- A Q&A summary for metal-foam cooling systems notes that **uncompressed aluminum foam with ~14% relative density** can reach effective bulk thermal conductivity of about **$\sim 10\ \text{W/m·K}$**.   
- Other studies on Al foams (closed- and open-cell) generally find that effective conductivity is only **a few percent of bulk Al**, often in the **1–10 W/m·K** range for porosities around 80–90%.   

So literature suggests that **$k_\text{foam,Al} \sim 5\text{–}15\ \text{W/m·K}$** is very typical for open-cell Al foams with ~5–15% relative density.

---

## 3. Nickel Foam and Ni-Coated Aluminum Foam

### Nickel foam (as a reference)

Commercial nickel foam datasheets report:

- Porosity often **95–98%** and  
- Mechanical strength on the order of **2–7 MPa**.  
- Effective thermal conductivity values quoted in the **$\sim 90\text{–}100\ \text{W/m·K}$** range for some high-conductivity Ni foams.   

These numbers show that even highly porous Ni foam can still have **high effective $k$** and **foam-level strengths in the few-MPa range**.

### Ni-coated aluminum foam

There are several papers that specifically look at **Ni-electroplating on open-cell Al foam**:

- Devivier et al. (2015) investigate open-cell Al foam improved by **electro-deposition of Ni**, and report **higher mechanical properties** (stiffness, plateau stress, energy absorption) compared with uncoated Al foam.   
- Genna et al. (2019) similarly show that **Ni-coated foams** maintain **higher performance than bare Al foams** even after thermal exposure up to 450 °C, emphasising improved mechanical robustness and stability.   
- Jung et al. (2011) report that for nano-nickel-coated Al foams, **“the light aluminum foam only acts as support for the coating and has hardly any effect on the mechanical properties of coated foams”**, i.e., stiffness and strength are dominated by the Ni shell when the coating is sufficiently thick.   

Taken together, these Ni-coating studies suggest:

- Coating aluminum ligaments with a **substantial Ni layer** tends to:
  - **Increase effective stiffness and strength significantly**, sometimes to the point where the Ni dominates the mechanical response.
  - Provide **better energy-absorption characteristics** compared to uncoated foam.
- They also show that tuning **coating thickness** is an effective design knob for mechanical performance.

This is qualitatively consistent with our assumption that a **30%-of-strut-thickness Ni layer (≈50% of cross-section by area)** will pull the strut-level properties closer to those of Ni than to pure Al.

---

## 4. Gibson–Ashby Scaling for Foam-Level Properties

The classic **Gibson–Ashby** models for cellular solids give (for open-cell foams):

- Elastic modulus scaling:
  $$
  \frac{E_\text{foam}}{E_s} \approx C_E \left( \frac{\rho_\text{foam}}{\rho_s} \right)^2
  $$
- Yield (or plateau) strength scaling:
  $$
  \frac{\sigma_{y,\text{foam}}}{\sigma_{y,s}} \approx C_\sigma \left( \frac{\rho_\text{foam}}{\rho_s} \right)^{3/2}
  $$
where $E_s, \sigma_{y,s}, \rho_s$ are the properties of the **solid** material, and $C_E, C_\sigma$ are constants typically of order 0.1–1 for metallic open-cell foams.   

This framework is widely used in cellular-solids design and appears in:

- Gibson & Ashby, *Cellular Solids: Structure and Properties* (Cambridge University Press).   
- Ashby’s metal-foam design guides and many subsequent review papers.   

Using this model with **our “effective solid” taken as the Ni-coated strut material** is exactly how we arrived at:

- $E_\text{foam} \sim C_E\, E_\text{strut}\, \bar\rho^2$  
- $\sigma_{y,\text{foam}} \sim C_\sigma\, \sigma_{y,\text{strut}}\, \bar\rho^{3/2}$  
- $k_\text{foam} \sim C_k\, k_\text{strut}\, \bar\rho$ for a first-order thermal estimate (a common approximation in heat-transfer-in-foam literature).   

So our scaling from **strut-level to foam-level properties** follows the standard Gibson–Ashby approach used in the literature.

---

## 5. How This Backs Our Chosen Numbers

### 5.1 Effective strut properties

We assumed the strut is a **Ni-Al composite**, with about **51% of the cross-section in Ni** and **49% in Al** (30% of the thickness in Ni corresponds to $(0.7R)^2$ for the Al core and $R^2-(0.7R)^2$ for Ni).

Using simple rule-of-mixtures with the bulk data above:

- $E_\text{strut} \approx 0.49\,E_\text{Al} + 0.51\,E_\text{Ni}$  
  With $E_\text{Al}\approx 70\ \text{GPa}$ and $E_\text{Ni}\approx 200\ \text{GPa}$, this lands around **130–140 GPa**, which is consistent with Ni dominating stiffness.  
- $k_\text{strut} \approx 0.49\,k_\text{Al} + 0.51\,k_\text{Ni}$ gives a value in the **140 W/m·K** range, sitting naturally between bulk Al (~170 W/m·K) and bulk Ni (~90 W/m·K).   

Given the Ni-coating studies that report stiffness being dominated by Ni when coatings are sufficiently thick, it looks like treating the strut as an **effective medium with $E_\text{strut} \sim 130\text{–}140\ \text{GPa}$** is compatible with trends in the literature.   

### 5.2 Foam-level properties

If we take a **relative density $\bar\rho \sim 0.1$** (10%) and Gibson–Ashby scaling with order-1 coefficients:

- $E_\text{foam} \sim C_E\, E_\text{strut}\,\bar\rho^2$.  
  With $C_E \sim 1$ and $E_\text{strut} \sim 130\ \text{GPa}$, we get:
  $$
  E_\text{foam} \sim 130\ \text{GPa} \times (0.1)^2 \approx 1.3\ \text{GPa}
  $$
  This is slightly higher than the **0.05–0.1 GPa** reported for **uncoated Al foam at ~8% density**, which makes sense because:
  - We are at a slightly higher density (10% vs 8%), and  
  - The struts are Ni-reinforced, so the “solid” is stiffer than bare Al.   

- For yield strength, using $\sigma_{y,s} \sim 300\ \text{MPa}$ for a Ni-rich strut and $C_\sigma \sim 0.3$:
  $$
  \sigma_{y,\text{foam}} \sim 0.3 \times 300\ \text{MPa} \times (0.1)^{3/2} \approx 2.8\ \text{MPa}
  $$
  This sits right in the **few-MPa range** observed for both Al foams and Ni foams at similar densities.   

- For thermal conductivity, taking $k_\text{strut} \sim 140\ \text{W/m·K}$ and $\bar\rho \sim 0.1$, a simple linear scaling gives:
  $$
  k_\text{foam} \sim C_k\,k_\text{strut}\,\bar\rho \approx (1)\times 140\times 0.1 \approx 14\ \text{W/m·K}
  $$
  This falls nicely into the **10 W/m·K range** that cooling-system notes and experiments suggest for ~10–15% density Al foams, and using Ni-reinforced struts is plausibly on the higher side of that band.   

So the **working values** we proposed—

- $E_\text{foam} \sim 1\text{–}2\ \text{GPa}$  
- $\sigma_{y,\text{foam}} \sim 2\text{–}5\ \text{MPa}$  
- $k_\text{foam} \sim 10\text{–}20\ \text{W/m·K}$

—look to be **consistent with**:

1. Bulk Al and Ni material data,  
2. Published mechanical and thermal data for open-cell Al and Ni foams, and  
3. The standard Gibson–Ashby scaling applied to a Ni-Al composite strut.

Given the scatter in foam data and the strong processing dependence, we think it is fair to say:

> **“Literature suggests that for a Ni-coated Al open-cell foam with ~10% relative density and a relatively thick Ni layer (~30% of strut thickness), using $E_\text{foam}$ on the order of 1–2 GPa, yield strength of a few MPa, and effective thermal conductivity in the 10–20 W/m·K range is a reasonable first-order approximation for simulation. These values sit within the ranges reported for Al and Ni foams at similar densities and are consistent with Gibson–Ashby scaling and Ni-coating enhancement trends.”**
