#!/usr/bin/env python
# coding: utf-8

# # Computational Tools

# ## Calculators and Spreadsheets
# 
# These tools are useful for most of the 1D situations (with some programming 2D can be addressed using spreadsheets).  
# 
# In most analytical solutions you will need some special functions:
# 
# - erf() error function
# - erfc() complimentary error function
# - besseli(,) bessel function type i
# - besselj(,) bessel function type j
# - Ei() exponential integral 
# 
# There are a few more, but these handle many of the cases. In Excel they are part of the Analysis Add-in, similarily with LibreOffice use Insert/Function/AddIn and a pull down menu appears with; alternatively they can be programmed using VBA and polynomial approximations to the functions.
# 
# 

# ## Specialized Software
# 
# More complex cases usually will require special software:
# 
# - MODFLOW
# - MODPATH
# - MT3D
# - USGS-MOC (2D)
# - Chemflow-2000 are envisioned in this course.
# 
# In many instances the output must be post processed to make graphical representations.

# :::{note}
# We will probably use USGS-MOC, and output postprocessing for this course.
# :::
# 
# 
# 

# ## References
# 
# 1. [MODFLOW/MT3D](https://www.usgs.gov/software/mt3d-usgs-groundwater-solute-transport-simulator-modflow)
# 2. [MODFLOW/MT3D Python Wrappers](https://flopy.readthedocs.io/en/3.4.2/introduction.html)
# 2. [USGS-MOC](https://water.usgs.gov/nrp/gwsoftware/moc/moc.html)
# 3. [Chemflow-2000](https://www.epa.gov/water-research/chemflo-2000-interactive-software-simulating-water-and-chemical-movement-unsaturated)

# In[ ]:




