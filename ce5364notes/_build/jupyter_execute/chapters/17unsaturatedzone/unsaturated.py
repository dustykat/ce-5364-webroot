#!/usr/bin/env python
# coding: utf-8

# # Unsaturated Zone Transport
# 
# Unsaturated Zone Flow and Transport refers to the movement and transport of water and contaminants in the portion of the subsurface that lies above the groundwater table and contains both air and water within the pore spaces of the soil or rock. In this zone, the pore spaces are not completely saturated with water; rather, they contain a mixture of air and water, with the degree of saturation varying depending on factors such as rainfall, evaporation, and soil properties.
# 
# The unsaturated zone, also known as the vadose zone, is a critical component of the hydrological cycle. Water moves through this zone due to gravity, capillary forces, and pressure gradients. It plays a crucial role in processes like soil moisture replenishment, plant root uptake, and filtration of contaminants. Understanding unsaturated zone flow and transport is essential for managing water resources, assessing the risk of groundwater contamination, and optimizing land use practices to protect both water quality and quantity. 
# 
# ## Infiltration
# 
# The unsaturated zone is the portion of groundwater system where liquids and gasses share the pore space.  The liquid phase may be discontinuous.
# 
# ![](vadose1.png)
# 
# In the rainfall (or fuel spill) runoff process we can discuss the zone as a microcosm of a hydrologic cycle
# 
# ![](abstractions.png)
# 
# ## Tension (suction); Capillary Pressure
# 
# ![](suction1.png)
# 
# The pressure for water to move upward into the sponge (porous medium) is called the suction pressure, tension, or capillary pressure (almost interchangeably).
# 
# In the next figure - we examine the pore scale conditions in comparison to a capillary tube.
# 
# ![](porepressure.png)
# 
# The capillary rise (capillary pressure) is related to the pore size - small pores, large negative pressure at a water table.
# 
# ![](suctionpressure.png)
# 
# ## Soil Characteristic Curves
# 
# These are relationships between water content and suction pressure.  Unique for each soil, but many, many soils already characterized.  Methods are discussed below.
# 
# ![](soilcharcurve.png)
# 
# The soil characteristic curve is often modeled using one of several models such as (both these models are incorporated into Chemflo-2000):
# 
# 1. [**Local Copy** Brooks, R.H. and Corey, A.T. (1964) Hydraulic Properties of Porous Media. Hydrology Paper, Vol. 3, Colorado State University, Fort Collins. (local copy)](http://54.243.252.9/ce-5364-webroot/3-Readings/BrooksCorey2.PDF)
# 3. [**Local Copy** van Genuchten, M.T. (1980), A Closed-form Equation for Predicting the Hydraulic Conductivity of Unsaturated Soils. Soil Science Society of America Journal, 44: 892-898.](http://54.243.252.9/ce-5364-webroot/3-Readings/291980vGClosed-formKh.pdf)
# ## Darcy's Law in Unsaturated Flow
# 
# ![](unsatdarcy.png)
# 
# ![](retardseqn.png)
# 
# ## Measurement of Soil Properties
# 
# ![](soilproperties1.png)
# 
# ![](soilproperties2.png)
# 
# ![](soilproperties3.png)
# 
# Instead of the hanging column a more modern technique uses a [Tempe Cell](https://www.soilmoisture.com/TEMPE-CELL-2-1-4-DIAM.-6-CM-1-BAR-STD-CERAMIC/)
# 
# ![](soilproperties4.png)
# 
# ### Relative Permeability
# 
# ![](relativeperm.png)
# 
# ![](relativeperm2.png)

# ## Infiltration Models
# 
# ![](infiltration1.png)
# 
# ### Green-Ampt Model
# 
# ![](green-ampt.png)
# 
# ![](greenampt2.png)
# 
# ![](greenampt3.png)
# 

# ## References
# 
# 1. [Brooks, R.H. and Corey, A.T. (1964) Hydraulic Properties of Porous Media. Hydrology Paper, Vol. 3, Colorado State University, Fort Collins. (DOE link)](https://www.wipp.energy.gov/library/cra/2009_cra/references/Others/Brooks_Corey_1964_Hydraulic_Properties_ERMS241117.pdf)
# 2. [van Genuchten, M.T. (1980), A Closed-form Equation for Predicting the Hydraulic Conductivity of Unsaturated Soils. Soil Science Society of America Journal, 44: 892-898.](https://doi.org/10.2136/sssaj1980.03615995004400050002x)

# In[ ]:




