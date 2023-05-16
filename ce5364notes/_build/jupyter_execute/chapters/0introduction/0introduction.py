#!/usr/bin/env python
# coding: utf-8

# # Introduction

# ## Scope

# ## Preliminary Concepts
# 
# Solvent phase (soil, air, water) is the phase that contains the solute (constituient) phase. The amount of solute contained in the solvent is usually expressed as some kind of concentration,
# 
# Concentrations are expressed in a variety of units:
# 
# |Type|Meaning|Symbol|
# |---|---|---|
# |Volumetric|mass/volume|$\frac{mg}{L}$|
# |Massic|mass/mass|$ppm$|
# |Molarity|moles/volume|$M=\frac{mol}{L}$|
# |Molality|moles/mass|$$m=\frac{mol}{kg}$$|
# |Mole Fraction (also partial pressures)|moles/moles|$X_{species}$|
# |Equivalents|moles$\times$valence/volume|$Eq$|
# |Activity|disintegrations/second/volume|$\frac{Bq}{L}$ - a contrived unit|
# 
# The most common in environmental flow and transport models are volumetric and massic.  
# 
# There are cases where multiple phases are present (multi-phase transport) and multiple components in a solute mixture (multi-component).
# 
# Emulsions are a special kind of two-(or more)phase system where the emulsion behaves as a single phase with respect to motion.  Oil-in-water, water-in-oil, biosolids-in-water (technically a slurry), coal-in-water (a slurry) are examples of common emulsions.

# I use the terms constituients and pollutants more or less interchangeably; however a pollutant is a value judgement - if the particular constituient is undesirable, for example methyl-ethyl death in water - then its a pollutant, otherwise its just a lowly constituient.  The distinction is irrelevant unless lawyers, judges, and money are involved - then be careful; someone goes to jail, and someone loses their doublewide if you get your mords wixed!
# 
# ## Non-reactive constituients
# 
# Non-reactive constituients are constituients that **do not** undergo changes, exchanges, or reactions while traversing a region of interest.
# 
# Solutes are constituients that are soluible in the solvent or are larger aggregates that to not constitute a distinct mobile phase from the transporting or host fluid.
# 
# Examples include:
# 1. Chemicals dissolved in water
# 2. Solids suspended in water (liquid-solid emulsion)
# 3. Oil **dispersed** in water (liquid-liquid emulsion)
# 4. Water dispersed in air (liquid-gas emulsion)
# 5. nitrogen dissolved in air (mixture)
# 
# Examples of systems that are not strictly solvent-solute pairs  is an oil-water system where each liquid has a distinct phase, such as an oil slick in an estuary (distinct from produced water from a well which is an emulsion) - such a system would be a two-phase system and is dealt with using different but related tools.

# ## Transport Processes
# 
# The main transport processes of interest are listed below
# 
# :::{note}
# Reactions are boundary conditions and while they affect behavior they are not in themselves considered as transport processes. They are most definitely fate processes, so we won't get to ignore them!
# :::
# 
# ### Advection
# 
# Advection is the process by which a physical property, such as heat or a chemical substance, is transported by the motion of a fluid. This motion can be due to *convection*, where a fluid is heated or cooled and subsequently moves because of intrinsic density changes, or it can be due to the movement of the fluid itself by pressure gradients, such as in a river or ocean current, which is called *forced convection*.
# 
# :::{note}
# In meteorology, advection refers to the horizontal movement of air or other atmospheric properties, such as moisture or temperature, by the wind. For example, warm air moving from the tropics to the poles is an example of advection.
# 
# In oceanography, advection refers to the horizontal movement of water or other oceanic properties, such as salinity or nutrients, by ocean currents.
# :::
# 
# In our discussion herein, advection is the transport of solutes by the motion of the host fluid.
# 
# ### Diffusion
# 
# Solute diffusion in groundwater is the process by which solutes, such as dissolved contaminants or nutrients, move through the pore spaces and fractures of soil and rock in the subsurface. The rate and direction of solute diffusion are influenced by several factors, including the concentration gradient, the properties of the solute and the porous medium, and the temperature and pressure of the groundwater.
# 
# The movement of solutes in groundwater can occur through both advection and diffusion. Advection refers to the movement of solutes due to the bulk flow of groundwater, while diffusion refers to the movement of solutes from areas of high concentration to areas of low concentration due to the random motion of molecules.
# 
# The diffusion of solutes in groundwater is affected by the porosity and permeability of the subsurface, as well as the molecular properties of the solutes. For example, larger and more complex molecules may diffuse more slowly than smaller, simpler molecules. The temperature of the groundwater can also affect solute diffusion, as higher temperatures generally result in faster molecular motion and increased diffusion rates.
# 
# Understanding solute diffusion in groundwater is important for predicting the movement and fate of contaminants in the subsurface, as well as for managing and protecting groundwater resources. Models of solute diffusion can be used to predict the transport of contaminants in the subsurface and to evaluate the effectiveness of different remediation strategies.
# 
# A more compact definition is that diffusion is the mixing of solutes by Brownian (random) motion processes. Net transport is proportional to concentration gradients.
# 
# ### Dispersion
# 
# Solute dispersion in groundwater refers to the spreading and mixing of solutes, such as dissolved contaminants or nutrients, as they move through the pore spaces and fractures of soil and rock in the subsurface. The rate and extent of solute dispersion are influenced by several factors, including the properties of the solute and the porous medium, the flow velocity of the groundwater, and the geometry of the flow paths.
# 
# The movement of solutes in groundwater can occur through both advection and dispersion. Advection refers to the movement of solutes due to the bulk flow of groundwater, while dispersion refers to the spreading and mixing of solutes as they move through the subsurface due to variations in the velocity and direction of groundwater flow.
# 
# Solute dispersion in groundwater can be characterized by several different parameters, including the longitudinal dispersivity, which describes the spreading of solutes parallel to the direction of groundwater flow, and the transverse dispersivity, which describes the spreading of solutes perpendicular to the direction of groundwater flow.
# 
# Understanding solute dispersion in groundwater is important for predicting the movement and fate of contaminants in the subsurface, as well as for managing and protecting groundwater resources. Models of solute dispersion can be used to predict the transport of contaminants in the subsurface and to evaluate the effectiveness of different remediation strategies.
# 
# Observe the definition is practically the same as that for diffusion, except the temperature importance is replaced by the concepts of dispersivity.
# 
# The similarity arises in part because ultimately a Fickian-type descrpition is used to explain behavior for either process (the meanings and magnitudes of the dispersion coeficient and the diffusion coefficient are quite different).
# A compact definition is that dispersion is the mixing of solutes by small and large scale variations in the velocity field of the host fluid caused by shear resistance, turbulent fluctuations, and the braided flow paths.  Net transport is usually modeled as proportional to concentration gradients. 
# 
# Dispersion appears in several types:
# 1. Shear induced dispersion (pipes and open channel flows)
# 2. Turbulent dispersion (open flows)
# 3. Hydrodynamic dispersion (porous flows)

# ## References
# 
# 1. [Becquerel (radioactivity unit)](https://en.wikipedia.org/wiki/Becquerel)

# In[ ]:




