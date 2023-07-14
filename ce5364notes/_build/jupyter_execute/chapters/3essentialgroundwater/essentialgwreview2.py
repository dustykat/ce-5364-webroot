#!/usr/bin/env python
# coding: utf-8

# # Essential Groundwater Review - II

# ## Darcy's Law
# 
# 
# 
# 
# 

# ## Pore Velocity
# 
# 

# ## Anisotropy
# 
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

# ## Cell Balance Models (Flow)

# 

# ## 

# ## 

# 

# ## References
# 
# 1. [My notes](http://54.243.252.9/ce-5364-webroot/3-Readings/GroundwaterReview.pdf)
# 

# In[ ]:




