# -----------------------------------------------
# Gibson–Ashby Foam Property Functions
# Stratofoam Project
# -----------------------------------------------

# Solid (parent) aluminum properties
E_s_default = 69e9            # Young's modulus [Pa]
G_s_default = 26e9            # Shear modulus [Pa]
sigma_y_s_default = 35e6      # Yield strength [Pa]
k_s_default = 205             # Thermal conductivity [W/mK]

# Default densities
rho_solid_default = 2700      # Aluminum [kg/m^3]


# ----------- Functions for each metric -----------
def relative_density(rho_foam, rho_solid=rho_solid_default):
    return rho_foam / rho_solid


def foam_Youngs_modulus(phi, E_s=E_s_default, C=1.0):
    return C * E_s * phi**2


def foam_shear_modulus(phi, G_s=G_s_default, C=1.0):
    return C * G_s * phi**2


def foam_yield_strength(phi, sigma_y_s=sigma_y_s_default, C=0.3):
    return C * sigma_y_s * phi**1.5


def foam_thermal_conductivity(phi, k_s=k_s_default):
    return k_s * phi


# ----------- Example calculation (Stratofoam Foam) -----------
rho_foam = 764  # measured foam density

phi = relative_density(rho_foam)

E_f = foam_Youngs_modulus(phi)
G_f = foam_shear_modulus(phi)
sigma_f = foam_yield_strength(phi)
k_f = foam_thermal_conductivity(phi)

# ----------- Print results -----------

print("\n--- Gibson–Ashby Properties (Functions Version) ---")
print(f"Relative density (phi): {phi:.4f}\n")

print(f"Foam Young's modulus (E_f):       {E_f/1e9:.3f} GPa")
print(f"Foam Shear modulus (G_f):         {G_f/1e9:.3f} GPa")
print(f"Foam Yield Strength (sigma_f):    {sigma_f/1e6:.3f} MPa")
print(f"Foam Thermal Conductivity (k_f):  {k_f:.2f} W/mK")
