#!/usr/bin/env python
# coding: utf-8

# # Essential Groundwater Review - II

# ## Darcy's Law
# 
# Darcy's Law is a fundamental principle in hydrogeology that describes the movement of groundwater through porous media and its transport of contaminants. It provides a mathematical relationship between the flow rate of groundwater, the hydraulic gradient, and the properties of the porous medium.
# 
# In the context of groundwater flow, Darcy's Law states that the flow rate of groundwater (Q) is directly proportional to the hydraulic conductivity (K) of the porous medium, the cross-sectional area perpendicular to the flow (A), and the hydraulic gradient (∇h) along which the groundwater is moving. Mathematically, it can be expressed as:
# 
# Q = -K * A * ∇h
# 
# Here, the negative sign indicates that groundwater flows from higher hydraulic head (pressure) to lower hydraulic head.
# 
# Darcy's Law is also applicable to the transport of dissolved contaminants in groundwater. In this case, it is modified to include the concentration of the contaminant (C) and its dispersion coefficient (D):
# 
# Q = -D * A * (∇C / C)
# 
# This modified form describes the movement of contaminants within the flowing groundwater. The dispersion coefficient accounts for the spreading and mixing of the contaminant as it moves through the porous medium, due to the heterogeneity of the subsurface.
# 
# Overall, Darcy's Law serves as a cornerstone in groundwater hydrology and contaminant transport studies, providing a quantitative basis for understanding and modeling the behavior of groundwater flow and mass transport in various geological settings.
# 
# 
# 
# 

# ## Pore Velocity
# 
# Pore velocity, in the context of groundwater flow, refers to the speed at which water molecules move through the interconnected void spaces (pores) within a porous medium, such as soil or rock. It is a measure of the actual velocity of water within these tiny channels and cavities, which collectively form the pathways for groundwater movement.
# 
# Pore velocity is influenced by several factors, including the hydraulic gradient (the change in hydraulic head per unit distance), the hydraulic conductivity of the porous medium (which dictates how easily water can flow through it), and the porosity of the material (the volume of pore space compared to the total volume of the material). Additionally, the degree of saturation and the properties of the fluid itself also play a role in determining pore velocity.
# 
# Understanding pore velocity is crucial for assessing groundwater flow rates, transport of contaminants, and the overall behavior of groundwater within subsurface formations. It helps hydrogeologists and scientists model and predict the movement of groundwater and the transport of dissolved substances, providing valuable insights into water resource management, environmental impact assessment, and remediation efforts.
# 

# ## Anisotropy
# 
# Anisotropy in the context of groundwater flow refers to the property of subsurface materials that causes the flow of groundwater to exhibit varying degrees of preferential directionality. In other words, the hydraulic conductivity of the underground formation is not the same in all directions. This anisotropic behavior is often observed in geological formations composed of layered or oriented materials such as sedimentary rocks, fractured bedrock, or layered aquifer systems.
# 
# Anisotropy can significantly impact the movement of groundwater. When the hydraulic conductivity is higher in one direction compared to another, groundwater will tend to flow more readily along the path of least resistance, following the direction of higher conductivity. This can lead to uneven flow patterns and the development of preferential flow pathways within the subsurface.
# 
# Understanding anisotropy is crucial for accurate modeling and prediction of groundwater movement and contaminant transport. Groundwater flow simulations must account for anisotropic behavior to effectively predict the direction and rate of groundwater flow, as well as the dispersion and spread of contaminants through the subsurface. Neglecting anisotropy can lead to inaccurate predictions and improper management of groundwater resources and contamination issues.
# 
# ### Principal Directions of Hydraulic Conductivity
# 
# To determine the principal values of the hydraulic conductivity tensor in 2D, you would typically follow these steps:
# 
# > **Define the Hydraulic Conductivity Tensor**: The hydraulic conductivity tensor represents the anisotropic properties of the subsurface material in terms of its ability to transmit water. In 2D, the hydraulic conductivity tensor is a symmetric matrix with three components: Kxx, Kyy, and Kxy (or Kyx). Kxx represents the hydraulic conductivity in the x-direction, Kyy represents the hydraulic conductivity in the y-direction, and Kxy (or Kyx) represents the cross-component.
# 
# > **Formulate the Hydraulic Conductivity Matrix**: Arrange the components of the hydraulic conductivity tensor into a 2x2 matrix, typically denoted as [K]. In matrix form, the hydraulic conductivity tensor for 2D becomes:
# 
# $$
# \begin{gather}
# \mathbf{K} =
# \begin{pmatrix}
# K_{xx} & K_{xy} \\
# ~\\
# K_{yx} & K_{yy} \\
# \end{pmatrix}
# ~
# \end{gather}
# $$
# 
# >**Solve for Eigenvalues**: Determine the eigenvalues of the hydraulic conductivity matrix [K]. Eigenvalues represent the principal values of the matrix and provide information about the directional properties of the hydraulic conductivity tensor.
# 
# >**Calculate Principal Values**: The eigenvalues of the hydraulic conductivity matrix [K] correspond to the principal values of the hydraulic conductivity tensor. These principal values represent the maximum and minimum hydraulic conductivities in the directions determined by the corresponding eigenvectors.
# 
# >**Interpret the Results**: The principal values of the hydraulic conductivity tensor provide insights into the anisotropic nature of fluid flow in the subsurface. The larger eigenvalue corresponds to the direction of maximum hydraulic conductivity, while the smaller eigenvalue represents the direction of minimum hydraulic conductivity.
# 
# Obtaining accurate values for the hydraulic conductivity components involves field measurements and laboratory testing of soil or rock samples.
# 
# In 3D the determination is simply the natural extension of the 2D process.  The matrix (tensor) is
# 
# $$
# \begin{gather}
# \mathbf{K} =
# \begin{pmatrix}
# K_{xx} & K_{xy} & K_{xz}\\
# ~\\
# K_{yx} & K_{yy} & K_{yz} \\
# ~\\
# K_{zx} & K_{zy} & K_{zz} \\
# \end{pmatrix}
# ~
# \end{gather}
# $$

# In[ ]:





# ## Cell Balance Models (Flow)

# [Well Hydraulics and Aquifer Tests](https://pubs.usgs.gov/wsp/wsp1536-E/pdf/wsp_1536-E.pdf)

# ## 

# ## 

# 

# ## References
# 
# 1. [My notes](http://54.243.252.9/ce-5364-webroot/3-Readings/GroundwaterReview.pdf)
# 

# In[ ]:




