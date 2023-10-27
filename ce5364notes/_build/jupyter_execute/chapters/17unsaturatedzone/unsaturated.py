#!/usr/bin/env python
# coding: utf-8

# # Unsaturated Zone Flow
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
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/porepressure.png" alt="porepressure.png" width="200%"/>
# <!--![](porepressure.png)-->
# 
# The capillary rise (capillary pressure) is related to the pore size - small pores, large negative pressure at a water table.
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/suctionpressure.png" alt="suctionpressure.png" width="200%"/>
# 
# <!--![](suctionpressure.png)-->

# ## Soil Characteristic Curves
# 
# pp. 291-295 of textbook discusses relationships between water content and suction pressure. Unique for each soil, but many, many soils already characterized.  Methods are discussed below.
# 
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/soilcharcurve.png" alt="soilcharcurve.png" width="200%"/>
# 
# <!--![](soilcharcurve.png)-->
# 
# The soil characteristic curve is often modeled using one of several models such as (both models below are incorporated into Chemflo-2000):
# 
# 1. [**Local Copy** Brooks, R.H. and Corey, A.T. (1964) Hydraulic Properties of Porous Media. Hydrology Paper, Vol. 3, Colorado State University, Fort Collins. (local copy)](http://54.243.252.9/ce-5364-webroot/3-Readings/BrooksCorey2.PDF)
# 3. [**Local Copy** van Genuchten, M.T. (1980), A Closed-form Equation for Predicting the Hydraulic Conductivity of Unsaturated Soils. Soil Science Society of America Journal, 44: 892-898.](http://54.243.252.9/ce-5364-webroot/3-Readings/291980vGClosed-formKh.pdf)
# 
# The Brooks and Corey model is:
# 
# $ k = k_0~\text{for}~p_c \le p_b \\
#   k = k_0(\frac{p_b}{p_c})^n~\text{for}~p_c \ge p_b$
#    
# Where the Brooks and Corey parameters are: <br>
# $k_0$, saturation permeability (divide by viscosity to get hydraulic conductivity)<br>
# $p_b$, the bubbling pressure (air entry pressure) <br>
# $n$, pore-size distribution index (its obviously a power-law model and $n$ is related to the pore size distribution.
# 
# The outputs are $k$, the effective permeability at some suction pressure, $p_c$, at a particular water content. - units are unusual (pressure is dynes/cm$^2$) peremability is cm$^2$, the result needs division by dynamic viscosity to recover convential hydraulic conductivity dimensionality and units adjustment (we will let software handle this when we use ChemFlow)
# 
# The van Genuchten model (from the reference above) is:
# 
# ![](vanGneuchten.png)

# typeset for clarity:
# 
# $K_r(\Theta) = \Theta^2 [1-(1-\Theta^{\frac{1}{m}})^m] \\
# ~~where~~ \\
# m=1-\frac{2}{n}\\
# 0<m<1; n>2\\
# \Theta~\text{is the effective saturation}$
# 
# The output is relative hydraulic conductivity.
# 
# Both models have been used extensively and many soils are already characterized; both documents describe how to conduct necessary experiments to determine soil properties for use in the models.

# ## Darcy's Law in Unsaturated Flow
# 
# pp. 295-297 discusses unsaturated flow equations
# 
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/unsatdarcy.png" alt="unsatdarcy.png" width="200%"/>
# 
# <!--![](unsatdarcy.png)-->
# 
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/retardseqn.png" alt="retardseqn.png" width="200%"/>
# 
# <!--![](retardseqn.png)-->

# ## Measurement of Soil Properties
# 
# pg 297-298 of textbook discusses measurements
# 
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/soilproperties1.png" alt="soilproperties4.png" width="200%"/>
# <!--![](soilproperties1.png)-->
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/soilproperties2.png" alt="soilproperties4.png" width="200%"/>
# <!--![](soilproperties2.png)-->
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/soilproperties3.png" alt="soilproperties4.png" width="200%"/>
# <!--![](soilproperties3.png)-->
# 
# Instead of the hanging column a more modern technique uses a [Tempe Cell](https://www.soilmoisture.com/TEMPE-CELL-2-1-4-DIAM.-6-CM-1-BAR-STD-CERAMIC/)
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/soilproperties4.png" alt="soilproperties4.png" width="200%"/>
# <!--![](soilproperties4.png)-->

# ### Relative Permeability
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/relativeperm.png" alt="relativeperm.png" width="200%"/>
# <!--![](relativeperm.png)-->
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/relativeperm2.png" alt="relativeperm2.png" width="200%"/>
# <!--![](relativeperm2.png)-->

# ## Infiltration Models
# 
# pp. 298-303 discusses infiltration models - a few are examined in my notes below
# 
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/infiltration1.png" alt="infiltration1.png" width="200%"/>
# <!--![](infiltration1.png)-->
# 
# Similar plots from numerical experiments by [Pickens, J. F., and Gillham, R. W. (1980), Finite element analysis of solute transport under hysteretic unsaturated flow conditions, Water Resour. Res., 16(6), 1071–1078, doi:10.1029/WR016i006p01071. ](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/WR016i006p01071) are:
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/GilhamandPickensinfiltrationdata.png" alt="GilhamandPickensinfiltrationdata.png" width="120%"/>
# 
# <!--![](GilhamandPickensinfiltrationdata.png)-->

# ### Green-Ampt Model
# 
# The following is a simple model of infiltration based on Green-Ampt concept as explained by [Polubarinova-Kochina, 1962 (translated by J. DeWeist)](http://54.243.252.9/ce-3354-webroot/3-Readings/Green-Ampt-PBK/Polubarinova-Kochina.pdf)
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/green-ampt.png" alt="greenampt1.png" width="200%"/>
# 
# <!--![](green-ampt.png)-->
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/greenampt2.png" alt="greenampt2.png" width="200%"/>
# 
# <!--![](greenampt2.png)-->
# <img src="http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/17unsaturatedzone/greenampt3.png" alt="greenampt3.png" width="200%"/>
# 
# <!--![](greenampt3.png)-->

# ## References
# 
# 1. [Brooks, R.H. and Corey, A.T. (1964) Hydraulic Properties of Porous Media. Hydrology Paper, Vol. 3, Colorado State University, Fort Collins. (DOE link)](https://www.wipp.energy.gov/library/cra/2009_cra/references/Others/Brooks_Corey_1964_Hydraulic_Properties_ERMS241117.pdf)
# 2. [van Genuchten, M.T. (1980), A Closed-form Equation for Predicting the Hydraulic Conductivity of Unsaturated Soils. Soil Science Society of America Journal, 44: 892-898.](https://doi.org/10.2136/sssaj1980.03615995004400050002x)
# 3. [Mori, H., Trevisan, L., Illangasekare, T H. (2015) Evaluation of relative permeability functions as inputs to multiphase flow models simulating supercritical CO2 behavior in deep geologic formations, International Journal of Greenhouse Gas Control, Volume 41, Pages 328-335](https://www.sciencedirect.com/science/article/pii/S1750583615001863)
# 4. [GREEN-AMPT INFILTRATION PARAMETERS FROM SOILS DATA J. Hydraul. Eng., 1983, 109(1): 62-70](https://dnrftp.state.co.us/DWR/DamSafety/HydrologyGuidelines_doNOTdelete/Guidelines_References/Rawls%20et%20al%20Green-Ampt%20Infiltration%20parameters%20from%20soils%20data%20ASCE%201983.pdf)

# In[ ]:




