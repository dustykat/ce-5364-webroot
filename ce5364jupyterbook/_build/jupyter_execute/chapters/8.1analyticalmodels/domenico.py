#!/usr/bin/env python
# coding: utf-8

# # Domenico-Robbins Solutions 
# 
# Domenico and Robbins (1985) conjectured that orthogonal (1D) solutions could be combined using superposition (and convolution) to create approximations to 3D behavior for simple, but useful geometries such as
# 
# ![](3Dgeom1.png)
# 
# The Domenico-Robbins (1985) solution is a heuristic simplification of an analytical solution to the advection-dispersion equation with sorption and reaction terms that can be programmed into spreadsheets or scripting environments without a full commitment to learning ... The simplification comes with advantages that make it a reasonable alternative to exact solutions for simulations representative of many realistic scenarios.
# 
# ## Applications and Significance
# 
# The 2D/3D Domenico solutions have been widely used by regulators, practitioners, and researchers due its ease of use and analytical origin. However, the lack of mathematical rigor in its derivation has raised questions about its accuracy with differing conclusions about its suitability for continued use.
# 
# > It has been used as a regulatory tool as recently as 2014 (e.g. [User’s Manual for the Quick Domenico Groundwater Fate-and-Transport Model (2014) Pensylvania Department of Environmental Protection](https://files.dep.state.pa.us/environmentalcleanupbrownfields/LandRecyclingProgram/LandRecyclingProgramPortalFiles/GuidanceTechTools/QD_manual_v3b%2002-28-2014.pdf)). 
# 
# Its significance lies in its ability to provide a rapid approximation of groundwater contamination scenarios, allowing for improved decision-making and risk assessment. 
# As already stated there is criticism that the Domenico solution is unsuitable for use in professional and research applications because of departures from exact solutions under certain conditions. 
# 
# :::{note}
# Given that all models are approximations its kind of a sorry critique. If you are modeling for real money, it would be prudent to apply multiple tools and not make decisions using only these analytical solutions.
# 
# > ... there is no need to ask ‘is the model true?’ The answer is ‘No.’ The only question of interest is ‘Is the model illuminating and useful?’  ([Box, 1979](https://en.wikipedia.org/wiki/All_models_are_wrong) )
# 
# It is worth noting that the strongest argument against use of the Domenico solution is that
# modern computers and readily available \$oftware can provide users with exact solutions or well established numerical models so there is no justification for using anything less. This position has some merit where decisions of weight with financial or environmental consequences depend on the modeling result.
# 
# As a side note readily available \$oftware is NOT easy to install and use; the graphical interfaces tend to tied to specific architecture (x86-64) and specific operating systems. Hence availability does not imply the tools will get used - these simplified models still have value and will for a long time.
# :::
#  
# [Yuan (1995)](http://54.243.252.9/about-me-webroot/about-me/MyWebPapers/thesis/yuan_thesis/Groundwater_transport.pdf) examined the "mathematical rigor" and provides detailed derivations of various solutions using convolution of elementry solutions ([Carslaw and Jaeger 1959](http://54.243.252.9/ce-4363-webroot/3-Readings/carslaw-and-jaeger-conduction-of-heat-in-solids-1959isbn-0198533683.pdf)).  While not at all resolving the critique, it provides interested readers with background and insight into the
# Domenico solution approximation(s).
# 
# ## References
# 
# 1. [Domenico, P.A. and Robbins, G.A. (1985), A New Method of Contaminant Plume Analysis. Groundwater, 23: 476-485. https://doi.org/10.1111/j.1745-6584.1985.tb01497.x](https://ngwa.onlinelibrary.wiley.com/doi/10.1111/j.1745-6584.1985.tb01497.x)
# 2. [Paladino, O. , Moranda, A.,  Massabó, M., and  Robbins, G. (2017). Analytical Solutions of Three-Dimensional Contaminant Transport Models with Exponential Source Decay. Groundwater. 56. 10.1111/gwat.12564. ](http://54.243.252.9/ce-5364-webroot/3-Readings/gwatnorev.pdf)
# 3. [Yuan, D, (1995)  *Accurate approximations for one-, two-, and three-dimensional groundwater mass transport from an exponentially decaying contaminant source.* MS Thesis, Department of Civil and Environmental Engineering, University of Houston. ](http://54.243.252.9/about-me-webroot/about-me/MyWebPapers/thesis/yuan_thesis/Groundwater_transport.pdf)
# 4. [Chuang, Lu-Chia, (1998) *A guidance system for choosing analytical contaminant transport models.* Doctoral Dissertation, Department of Civil and Environmental Engineering, University of Houston, Houston, Texas. 222p.](http://54.243.252.9/about-me-webroot/about-me/MyWebPapers/thesis/ants_dissertation/Luke_Chuang.pdf)
# 5. [Analytical solutions for one-, two-, and three-dimensional solute transport in ground-water systems with uniform flow
# Open-File Report 89-56](https://pubs.usgs.gov/publication/ofr8956)
# 6. [Analytical solutions for one-, two-, and three-dimensional solute transport in ground-water systems with uniform flow
# Techniques of Water-Resources Investigations 03-B7 (supercedes above reference)](https://pubs.usgs.gov/publication/twri03B7)
# 

# In[ ]:




