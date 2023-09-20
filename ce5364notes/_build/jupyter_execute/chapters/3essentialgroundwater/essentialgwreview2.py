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
# 
# Insert notes on aquifer models (to support flownets below)

# [Well Hydraulics and Aquifer Tests](https://pubs.usgs.gov/wsp/wsp1536-E/pdf/wsp_1536-E.pdf)

# ## 

# ## 

# 

# ## Flownets (pp. 30-34)
# 
# A flow net is a graphical representation that depicts the flow of groundwater within an aquifer or through porous media. It consists of a network of flow lines and equipotential lines that together provide a clear visualization of the groundwater flow direction and hydraulic head distribution within a given geological formation. Flow lines represent the path that groundwater particles would take as they move through the aquifer, while equipotential lines represent lines of equal hydraulic head. These lines intersect orthogonally, forming a grid-like pattern, with the density of flow lines increasing where the groundwater flow is faster.
# 
# Flow nets are employed in various aspects of groundwater modeling:
# 
# 1. Delineating Flow Patterns: Flow nets are instrumental in identifying the direction and velocity of groundwater flow within an aquifer. By studying the flow lines and equipotential lines, hydrogeologists can determine the dominant flow pathways and areas of groundwater recharge and discharge.
# 
# 2. Designing Well Fields: When designing well fields for groundwater extraction, it is crucial to understand the local groundwater flow patterns. Flow nets help in optimizing the placement and pumping rates of wells, ensuring efficient water supply without causing adverse effects on nearby groundwater-dependent ecosystems.
# 
# 3. Contaminant Transport Modeling: Flow nets are an essential component of contaminant transport modeling. They provide the basis for predicting the movement of contaminants through the subsurface, allowing for the assessment of potential risks and the development of remediation strategies.
# 
# 4. Dam and Barrier Design: Engineers use flow nets to design dams, levees, and groundwater barriers. Understanding groundwater flow patterns is critical for ensuring the stability and effectiveness of these structures in controlling water flow.
# 
# 5. Land Use Planning: Flow nets also have applications in land use planning. By considering groundwater flow patterns, urban planners can make informed decisions about where to build infrastructure, manage stormwater, and protect sensitive areas from potential contamination.
# 
# Flownets provide a visual representation of groundwater flow patterns and hydraulic head distributions, aiding in various aspects of groundwater resource management, environmental protection, and engineering design. 
# 
# 
# [Cleveland, T.G. (2002) *Flownets* Notes to accompany "CIVE 7332 Flow and Transport Modeling for Environmental Engineering" at University of Houston](http://54.243.252.9/ce-5364-webroot/3-Readings/flownet_1.pdf)
# 
# Numerical generation of flownets can be accomplished using a spreadsheet, python script, or MODFLOW.  
# 
# A simple spreadsheet example is available from
# 
# [Cleveland, T.G. (1997) *Velocity Potential - Stream Function Ideal Flow Model (circa 1999) (Excel)*](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/5nonreactivetransport/VelocityPotential-StreamFunction-FDM.xls)
# 
# 
# 
# ### Example in Python
# 
# In steady aquifer flow, the flow is irrotational (or at least can be modeled as such). 
# There exists an orthogonal function called the stream function (it is the function that exists in the flow field when vorticity is zero).
# A really good explaination of stream functions (and streamlines) appears on pages 381--398 in Zheng(1995).
# 
# This function can be used to generate plots of streamlines for the same system.
# The principal changes are the material properties representation and the boundary conditions.  

# #### Velocity Potential
# 
# The velocity potential function is usually Darcy's law applied to the head distribution $\phi = \frac{T}{b}h$
# 
# If we start with a steady flow description of GW flow like:
# 
# $$
# 0= 
# \frac{\partial}{\partial x}({\frac{T_x}{b} \frac{\partial h}{\partial x}})
# +
# \frac{\partial}{\partial y}({\frac{T_y}{b} \frac{\partial h}{\partial y}})
# $$
# 
# the terms ${\frac{T_x}{b} \frac{\partial h}{\partial x}}$  and ${\frac{T_y}{b} \frac{\partial h}{\partial y}}$ can be replaced by $\frac{\partial \phi}{\partial x}$ or $\frac{\partial \phi}{\partial y}$ so the expression looks something like
# 
# $$
# 0= 
# \frac{\partial}{\partial x}({ \frac{\partial \phi}{\partial x}})
# +
# \frac{\partial}{\partial y}({ \frac{\partial \phi}{\partial y}})
# $$
# 
# Which is what we would call the velocity potential - although for flow nets we usually just solve for the head so we can compute pressures, using the formulation below:
# 
# $$
# 0= 
# \frac{\partial}{\partial x}({{T_x} \frac{\partial h}{\partial x}})
# +
# \frac{\partial}{\partial y}({{T_y} \frac{\partial h}{\partial y}})
# $$
# 
# The difference equation (pp. 349-357) on a regular grid is
# 
# $$
# \begin{matrix}
# 0= 
# [\frac{1}{\Delta x} T_{x} \frac{h_{i-1,j} - h_{i,j}}{\Delta x} +
#  \frac{1}{\Delta y} T_{y} \frac{h_{i,j-1} - h_{i,j}}{\Delta y}] - \\
# ~~~~~~~~~~\\
# ~~~~~~~~~~[ \frac{1}{\Delta x} T_{x}  \frac{h_{i,j} - h_{i+1,j}}{\Delta x} +
#   \frac{1}{\Delta y}  T_{y} \frac{h_{i,j} - h_{i,j+1}}{\Delta y} ]        
# \end{matrix}        
# $$
# 
# Typically one approximates the spatial variation of the material properties (transmissivity) as arithmetic mean values between two cells, so making the following definitions:
# 
# $$
# \begin{matrix}
# A_{i,j} = \frac{1}{2 \Delta x^2}(T_{x,(i-1,j)}+T_{x,(i,j)}) \\ ~~ \\
# B_{i,j} = \frac{1}{2 \Delta x^2}(T_{x,(i,j)}+T_{x,(i+1,j)})   \\ ~~ \\
# C_{i,j} = \frac{1}{2 \Delta y^2}(T_{y,(i,j-1)}+T_{y,(i,j)})   \\ ~~ \\
# D_{i,j} = \frac{1}{2 \Delta y^2}(T_{y,(i,j)}+T_{y,(i,j+1)})   \\ ~~ \\
# \end{matrix}
# $$
# 
# Substitution into the difference equation yields
# 
# $$
# 0 = A_{i,j}h_{i-1,j} + B_{i,j}h_{i+1,j} - (A_{i,j}+B_{i,j}+C_{i,j}+D_{i,j})h_{i,j} + C_{i,j}h_{i,j-1} + D_{i,j}h_{i,j+1}
# $$
# 
# As before we can explicitly write the cell equation for $h_{i,j}$ as
# 
# $$
# h_{i,j} = \frac{[A_{i,j}h_{i-1,j} + B_{i,j}h_{i+1,j} + C_{i,j}h_{i,j-1} + D_{i,j}h_{i,j+1}]}{[A_{i,j}+B_{i,j}+C_{i,j}+D_{i,j}]}
# $$
# 
# This difference equation represents an approximation to the governing flow equation, the accuracy depending on the cell
# size. Boundary conditions are applied directly into the analogs (another name for the difference equations) at appropriate
# locations on the computational grid. We can generate solutions either by iteration or solving the resulting linear system; iteration is really easy to program, so for exploratory work that's usually the approach.

# #### Stream Function
# 
# The stream function $\Psi$ is a function that is orthogonal to the velocity potential function and expressed as a partial differential equation is
# 
# $$
# 0= 
# \frac{\partial}{\partial x}({\frac{1}{T_y} \frac{\partial \Psi}{\partial x}})
# +
# \frac{\partial}{\partial y}({\frac{1}{T_x} \frac{\partial \Psi}{\partial y}})
# $$
# 
# Observe how the material property is inverted and changes directional identity, otherwise the equation is structurally identical to the groundwater flow equation (for steady flow).
# 
# The difference equation is practically the same as above:
# 
# The difference equation is also almost the same
# 
# $$
# \begin{matrix}
# 0= 
# [\frac{1}{\Delta x} \frac{1}{T_{y}} \frac{\Psi_{i-1,j} - \Psi_{i,j}}{\Delta x} +
#  \frac{1}{\Delta y} \frac{1}{T_{x}} \frac{\Psi_{i,j-1} - \Psi_{i,j}}{\Delta y}] - \\
# ~~~~~~~~~~\\
# ~~~~~~~~~~[ \frac{1}{\Delta x} \frac{1}{T_{y}}  \frac{\Psi_{i,j} - \Psi_{i+1,j}}{\Delta x} +
#   \frac{1}{\Delta y}  \frac{1}{T_{x}} \frac{\Psi_{i,j} - \Psi_{i,j+1}}{\Delta y} ]        
# \end{matrix}        
# $$
# 
# The substitutions are
# 
# $$
# \begin{matrix}
# A_{i,j} = \frac{1}{2 \Delta x^2}(T_{y,(i-1,j)}^{-1}+T_{y,(i,j)}^{-1}) \\ ~~ \\
# B_{i,j} = \frac{1}{2 \Delta x^2}(T_{y,(i,j)}^{-1}+T_{y,(i+1,j)}^{-1})   \\ ~~ \\
# C_{i,j} = \frac{1}{2 \Delta y^2}(T_{x,(i,j-1)}^{-1}+T_{x,(i,j)}^{-1})   \\ ~~ \\
# D_{i,j} = \frac{1}{2 \Delta y^2}(T_{x,(i,j)}^{-1}+T_{x,(i,j+1)}^{-1})   \\ ~~ \\
# \end{matrix}
# $$
# 
# Substitution into the difference equation yields
# 
# $$
# 0 = A_{i,j}\Psi_{i-1,j} + B_{i,j}\Psi_{i+1,j} - (A_{i,j}+B_{i,j}+C_{i,j}+D_{i,j})\Psi_{i,j} + C_{i,j}\Psi_{i,j-1} + D_{i,j}\Psi_{i,j+1}
# $$
# 
# As before we can explicitly write the cell equation for $h_{i,j}$ as
# 
# $$
# \Psi_{i,j} = \frac{[A_{i,j}\Psi_{i-1,j} + B_{i,j}\Psi_{i+1,j} + C_{i,j}\Psi_{i,j-1} + D_{i,j}\Psi_{i,j+1}]}{[A_{i,j}+B_{i,j}+C_{i,j}+D_{i,j}]}
# $$
# 
# So at this point we could literally use the same script, however boundary conditions also ``invert.''
# A no-flow head-domain boundary is a constant value stream function-domain boundary.
# A constant value head-domain boundary is a zero-gradient stream function-domain boundary.

# So a script that first solves for the head distribution, then the stream function could be used to create a flownet. 
# 
# ### Sheetpile under a dam flownet 
# 
# Compare to the example shown on pp. 30-34.
# 
# The figure below is a schematic of a dam built upon a permeable ground layer 80 meters thick (segment A to I).
# 
# ![](sheetpile1.png)
# 
# The dam has a base 60 meters long (segment B to F), with an upstream water depth of 10 meters. The downstream side of the dam is at 0 meters depth (otherwise its not a very good dam!). A sheetpile cutoff wall is installed beneath the dam (segment C to D to U to E). The ground layer has a hydraulic conductivity of K = 1 × 10−4 meters per second.
# 
# Important engineering questions are what is the pore water pressure under the dam, and is what is the total seepage under the dam? The pore water pressure can be found by solving for heads under the dam then subtracting the elevation of the computation location relative to a datum. The flow is found by Darcy’s law applied under the dam (shown as locations 1,2,3,4, and 5 in the sketch), which in turn requires computation of head under the dam. Thus the questions are answered by finding the head distribution under the dam.
# 
# The flow field (mathematically) extends an infinite distance upstream and downstream, but as a practical matter the contribution to seepage far upstream of the dam is negligible, and hence is approximated by the finite domain depicted.
# 
# Using the tools we have already we can simply build an input file, run our script and determine the head distribution (and thus compute the discharges under the dam. Then rerun with same script, but modify the boundary conditions and material properties to obtain the stream function - plot both solutions on the same contour map and viola we have a flownet.
# 
# The first is to represent the domain as shown, and make the following specifications in the boundary condition information, and we will treat the sheetpile cutoff wall as a low permeability inclusion (much like the the prior example). The boundary conditions are:
# 
# 1. The segment from A to B is a constant head boundary with value equal to 10.
# 2. The segment from B to F is a zero-flux boundary.
# 3. The segment from B to C to D to U to E to F should be treated as a zero-flux boundary, but our mask does not extend into the interior – however the sheetpile itself can be approximated by providing a very small permeability. Alternately we could (should) modify the code to handle interior boundaries – but that is outside the scope of this chapter.
# 4. The segment from F to G is a constant head boundary with value equal to 0.
# 5. The segment form G to H is a constant head boundary with value equal to 0.
# 6. The segment from H to I is a zero-flux boundary.
# 7. The segment from I to A is a constant head boundary with value equal to 10.
# 
# Here's the input file for the heads $\phi$ in the picture
# ```
# 10
# 10
# 1
# 9
# 31
# 1e-12
# 5000
# 0 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250 260 270 280 290 300
# 80 70 60 50 40 30 20 10 0
# 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.00010
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 

# In[1]:


def sse(matrix1,matrix2):
    sse=0.0
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    for ir in range(nr):
        for jc in range(nc):
            sse=sse+(matrix1[ir][jc]-matrix2[ir][jc])**2
    return(sse)

def update(matrix1,matrix2):
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    ##print(nr,nc)
    for ir in range(nr):
        for jc in range(nc):
            ##print(ir,jc)
            matrix2[ir][jc]=matrix1[ir][jc]
    return(matrix2)

def writearray(matrix):
    nr=len(matrix) # get row count
    nc=len(matrix[0]) # get column count
    import numpy as np
    new_list = list(np.around(np.array(matrix), 3))    
    for ir in range(nr):
        print(ir,new_list[ir][:])
    return()

localfile = open("PotentialFnSheetpile1.txt","r") # connect and read file for 2D gw model
deltax = float(localfile.readline())
deltay = float(localfile.readline())
deltaz = float(localfile.readline())
nrows = int(localfile.readline())
ncols = int(localfile.readline())
tolerance = float(localfile.readline())
maxiter = int(localfile.readline())
distancex = [] # empty list
distancex.append([float(n) for n in localfile.readline().strip().split()])
distancey = [] # empty list
distancey.append([float(n) for n in localfile.readline().strip().split()])
boundarytop = [] #empty list
boundarytop.append([float(n) for n in localfile.readline().strip().split()])
boundarybottom = [] #empty list
boundarybottom.append([int(n) for n in localfile.readline().strip().split()])
boundaryleft = [] #empty list
boundaryleft.append([int(n) for n in localfile.readline().strip().split()])
boundaryright = [] #empty list
boundaryright.append([int(n) for n in localfile.readline().strip().split()])
head =[] # empty list
for irow in range(nrows):
        head.append([float(n) for n in localfile.readline().strip().split()])
hydcondx = [] # empty list
for irow in range(nrows):
        hydcondx.append([float(n) for n in localfile.readline().strip().split()])
hydcondy = [] # empty list
for irow in range(nrows):
        hydcondy.append([float(n) for n in localfile.readline().strip().split()])
localfile.close() # Disconnect the file
##
amat = [[0 for j in range(ncols)] for i in range(nrows)]
bmat = [[0 for j in range(ncols)] for i in range(nrows)]
cmat = [[0 for j in range(ncols)] for i in range(nrows)]
dmat = [[0 for j in range(ncols)] for i in range(nrows)]
##
for irow in range(1,nrows-1):
    for jcol in range(1,ncols-1):
        amat[irow][jcol] = (( hydcondx[irow-1][jcol  ]+ hydcondx[irow  ][jcol  ]) * deltaz ) /(2.0*deltax**2)
        bmat[irow][jcol] = (( hydcondx[irow  ][jcol  ]+ hydcondx[irow+1][jcol  ]) * deltaz ) /(2.0*deltax**2)
        cmat[irow][jcol] = (( hydcondy[irow  ][jcol-1]+ hydcondy[irow  ][jcol  ]) * deltaz ) /(2.0*deltay**2)
        dmat[irow][jcol] = (( hydcondy[irow  ][jcol  ]+ hydcondy[irow  ][jcol+1]) * deltaz ) /(2.0*deltay**2)
##
headold = [[0 for jc in range(ncols)] for ir in range(nrows)] #force new matrix
headold = update(head,headold) # update
##writearray(head)
##print("----")
##writearray(headold)
##print("--------")
tolflag = False
for iter in range(maxiter):
##    print("begin iteration")
##    writearray(head)
##    print("----")
##    writearray(headold)
##    print("--------")

# Boundary Conditions

# first and last row special == no flow boundaries
    for jcol in range(ncols):
        if boundarytop[0][jcol] == 0: # no - flow at top
            head [0][jcol ] = head[1][jcol ]
        if boundarybottom[0][ jcol ] == 0: # no - flow at bottom
            head [nrows-1][jcol ] = head[nrows-2][jcol ]
# first and last column special == no flow boundaries     
    for irow in range(nrows): 
        if  boundaryleft[0][ irow ] == 0:
            head[irow][0] = head [irow][1] # no - flow at left
        if boundaryright[0][ irow ] == 0: 
            head [irow][ncols-1] = head[ irow ][ncols-2] # no - flow at right
# interior updates
    for irow in range(1,nrows-1):
        for jcol in range(1,ncols-1):
            head[irow][jcol]=( amat[irow][jcol]*head[irow-1][jcol  ] 
                              +bmat[irow][jcol]*head[irow+1][jcol  ] 
                              +cmat[irow][jcol]*head[irow  ][jcol-1] 
                              +dmat[irow][jcol]*head[irow  ][jcol+1])/(amat[ irow][jcol ]+ bmat[ irow][jcol ]+ cmat[ irow][jcol ]+ dmat[ irow][jcol ])
# test for stopping iterations
##    print("end iteration")
##    writearray(head)
##    print("----")
##    writearray(headold)
    percentdiff = sse(head,headold)
    if  percentdiff <= tolerance:
        print("Exit iterations in velocity potential because tolerance met ")
        print("Iterations =" , iter+1 ) ;
        tolflag = True
        break
    headold = update(head,headold)
print("End Calculations")
print("Iterations    = ",iter+1)
print("Closure Error = ",round(percentdiff,3))
print("Head Map")
print("----")
writearray(head)
print("----")
############# Contour Plot
my_xyz = [] # empty list
for irow in range(nrows):
    for jcol in range(ncols):
        my_xyz.append([distancex[0][jcol],distancey[0][irow],head[irow][jcol]])
import pandas
my_xyz = pandas.DataFrame(my_xyz) # convert into a data frame
#print(my_xyz) # activate to examine the dataframe
import numpy 
import matplotlib.pyplot
from scipy.interpolate import griddata
# extract lists from the dataframe
coord_x = my_xyz[0].values.tolist() # column 0 of dataframe
coord_y = my_xyz[1].values.tolist() # column 1 of dataframe
coord_z = my_xyz[2].values.tolist() # column 2 of dataframe
coord_xy = numpy.column_stack((coord_x, coord_y))
# Set plotting range in original data units
lon = numpy.linspace(min(coord_x), max(coord_x), 3000)
lat = numpy.linspace(min(coord_y), max(coord_y), 800)
X, Y = numpy.meshgrid(lon, lat)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z = griddata(numpy.array(coord_xy), numpy.array(coord_z), (X, Y), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(15, 4)
levels1 = [1,2,3,4,5,6,7,8,9,10]
CS = ax.contour(X, Y, Z, levels1)
ax.clabel(CS, inline=2, fontsize=16)
ax.set_title('Contour Plot of Heads from Sheetpile1 Input')


# Now we reuse the code, but change `head` to `stream` and modify the contour plot variable names as well as modify the input file to reflect the changed material properties and boundary conditions.
# 
# Here's the input file for the stream function
# 
# ```
# 10
# 10
# 1
# 9
# 31
# 1e-12
# 5000
# 0 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250 260 270 280 290 300
# 80 70 60 50 40 30 20 10 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 100000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# ```
# 
# In these examples the value of the stream function is arbitrarily set to range from $0$ to $100$.  One useful interpretation of stream function values is that their differences indicate the flow fraction (of total flow) that flows between the streamlines (contour lines of constant stream function value).

# In[390]:


def sse(matrix1,matrix2):
    sse=0.0
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    for ir in range(nr):
        for jc in range(nc):
            sse=sse+(matrix1[ir][jc]-matrix2[ir][jc])**2
    return(sse)

def update(matrix1,matrix2):
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    ##print(nr,nc)
    for ir in range(nr):
        for jc in range(nc):
            ##print(ir,jc)
            matrix2[ir][jc]=matrix1[ir][jc]
    return(matrix2)

def writearray(matrix):
    nr=len(matrix) # get row count
    nc=len(matrix[0]) # get column count
    import numpy as np
    new_list = list(np.around(np.array(matrix), 3))    
    for ir in range(nr):
        print(ir,new_list[ir][:])
    return()

localfile = open("StreamFnSheetpile1.txt","r") # connect and read file for 2D gw model
deltax = float(localfile.readline())
deltay = float(localfile.readline())
deltaz = float(localfile.readline())
nrows = int(localfile.readline())
ncols = int(localfile.readline())
tolerance = float(localfile.readline())
maxiter = int(localfile.readline())
distancex = [] # empty list
distancex.append([float(n) for n in localfile.readline().strip().split()])
distancey = [] # empty list
distancey.append([float(n) for n in localfile.readline().strip().split()])
boundarytop = [] #empty list
boundarytop.append([float(n) for n in localfile.readline().strip().split()])
boundarybottom = [] #empty list
boundarybottom.append([int(n) for n in localfile.readline().strip().split()])
boundaryleft = [] #empty list
boundaryleft.append([int(n) for n in localfile.readline().strip().split()])
boundaryright = [] #empty list
boundaryright.append([int(n) for n in localfile.readline().strip().split()])
stream =[] # empty list
for irow in range(nrows):
        stream.append([float(n) for n in localfile.readline().strip().split()])
hydcondx = [] # empty list
for irow in range(nrows):
        hydcondx.append([float(n) for n in localfile.readline().strip().split()])
hydcondy = [] # empty list
for irow in range(nrows):
        hydcondy.append([float(n) for n in localfile.readline().strip().split()])
localfile.close() # Disconnect the file
##
amat = [[0 for j in range(ncols)] for i in range(nrows)]
bmat = [[0 for j in range(ncols)] for i in range(nrows)]
cmat = [[0 for j in range(ncols)] for i in range(nrows)]
dmat = [[0 for j in range(ncols)] for i in range(nrows)]
##
for irow in range(1,nrows-1):
    for jcol in range(1,ncols-1):
        amat[irow][jcol] = (( hydcondx[irow-1][jcol  ]+ hydcondx[irow  ][jcol  ]) * deltaz ) /(2.0*deltax**2)
        bmat[irow][jcol] = (( hydcondx[irow  ][jcol  ]+ hydcondx[irow+1][jcol  ]) * deltaz ) /(2.0*deltax**2)
        cmat[irow][jcol] = (( hydcondy[irow  ][jcol-1]+ hydcondy[irow  ][jcol  ]) * deltaz ) /(2.0*deltay**2)
        dmat[irow][jcol] = (( hydcondy[irow  ][jcol  ]+ hydcondy[irow  ][jcol+1]) * deltaz ) /(2.0*deltay**2)
##
streamold = [[0 for jc in range(ncols)] for ir in range(nrows)] #force new matrix
streamold = update(stream,streamold) # update
##writearray(stream)
##print("----")
##writearray(streamold)
##print("--------")
tolflag = False
for iter in range(maxiter):
##    print("begin iteration")
##    writearray(stream)
##    print("----")
##    writearray(streamold)
##    print("--------")

# Boundary Conditions

# first and last row special == no flow boundaries
    for jcol in range(ncols):
        if boundarytop[0][jcol] == 0: # no - flow at top
            stream [0][jcol ] = stream[1][jcol ]
        if boundarybottom[0][ jcol ] == 0: # no - flow at bottom
            stream [nrows-1][jcol ] = stream[nrows-2][jcol ]
# first and last column special == no flow boundaries     
    for irow in range(nrows): 
        if  boundaryleft[0][ irow ] == 0:
            stream[irow][0] = stream [irow][1] # no - flow at left
        if boundaryright[0][ irow ] == 0: 
            stream [irow][ncols-1] = stream[ irow ][ncols-2] # no - flow at right
# interior updates
    for irow in range(1,nrows-1):
        for jcol in range(1,ncols-1):
            stream[irow][jcol]=( amat[irow][jcol]*stream[irow-1][jcol  ] 
                              +bmat[irow][jcol]*stream[irow+1][jcol  ] 
                              +cmat[irow][jcol]*stream[irow  ][jcol-1] 
                              +dmat[irow][jcol]*stream[irow  ][jcol+1])/(amat[ irow][jcol ]+ bmat[ irow][jcol ]+ cmat[ irow][jcol ]+ dmat[ irow][jcol ])
# test for stopping iterations
##    print("end iteration")
##    writearray(stream)
##    print("----")
##    writearray(streamold)
    percentdiff = sse(stream,streamold)
    if  percentdiff <= tolerance:
        print("Exit iterations in Stream Function because tolerance met ")
        print("Iterations =" , iter+1 ) ;
        tolflag = True
        break
    streamold = update(stream,streamold)
print("End Calculations")
print("Iterations    = ",iter+1)
print("Closure Error = ",round(percentdiff,3))
print("Stream Function Map")
print("----")
writearray(stream)
print("----")
####################### Contour Plot ###############
my_xyz2 = [] # empty list
for irow in range(nrows):
    for jcol in range(ncols):
        my_xyz2.append([distancex[0][jcol],distancey[0][irow],stream[irow][jcol]])
import pandas
my_xyz2 = pandas.DataFrame(my_xyz2) # convert into a data frame
#print(my_xyz) # activate to examine the dataframe
import numpy 
import matplotlib.pyplot
from scipy.interpolate import griddata
# extract lists from the dataframe
coord_x2 = my_xyz2[0].values.tolist() # column 0 of dataframe
coord_y2 = my_xyz2[1].values.tolist() # column 1 of dataframe
coord_z2 = my_xyz2[2].values.tolist() # column 2 of dataframe
coord_xy2 = numpy.column_stack((coord_x2, coord_y2))
# Set plotting range in original data units
lon = numpy.linspace(min(coord_x2), max(coord_x2), 3000)
lat = numpy.linspace(min(coord_y2), max(coord_y2), 800)
X2, Y2 = numpy.meshgrid(lon, lat)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z2 = griddata(numpy.array(coord_xy2), numpy.array(coord_z2), (X2, Y2), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(15, 4)
levels = [10,20,30,40,50,60,70,80,90,100]
CS2 = ax.contour(X2, Y2, Z2, levels )
ax.clabel(CS2, inline=2, fontsize=16)
ax.set_title('Contour Plot of Stream Function for Sheetpile1 Input')


# Now both plots on same canvass

# In[391]:


# Head (Velocity Potential Map)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z = griddata(numpy.array(coord_xy), numpy.array(coord_z), (X, Y), method='cubic')
Z2 = griddata(numpy.array(coord_xy2), numpy.array(coord_z2), (X2, Y2), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(15, 4)
levels1 = [1,2,3,4,5,6,7,8,9]
CS = ax.contour(X, Y, Z, levels1)
levels2 = [10,20,30,40,50,60,70,80,90]
CS2 = ax.contour(X2, Y2, Z2, levels2 )
ax.clabel(CS, inline=2, fontsize=12)
ax.clabel(CS2, inline=2, fontsize=12)
ax.set_title('Flownet for Sheetpile1 Input')


# <hr>
# <hr>
# 
# ### Flownet Example 2 : Pore Pressure under a Dam (Domain Decomposition approach)
# 
# The second way to solve this example, and perhaps better is to take advantage of
# the symmetry and cut the domain in half, as 
# 
# ![](sheetpile2.png)
# 
# In this method we can actually specify the sheetpile as a boundary, and we will obtain the about same results, but
# only need to supply half as much input data.
# 
# Here's the input file for the half-domain head calculations
# 
# ```
# 10
# 10
# 1
# 9
# 15
# 1e-16
# 5000
# 0 10 20 30 40 50 60 70 80 90 100 110 120 130 140
# 80 70 60 50 40 30 20 10 0
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1
# 0 0 0 0 1 1 1 1 1
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 5
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 5
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 5
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 5
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 5
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# ```

# In[398]:


def sse(matrix1,matrix2):
    sse=0.0
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    for ir in range(nr):
        for jc in range(nc):
            sse=sse+(matrix1[ir][jc]-matrix2[ir][jc])**2
    return(sse)

def update(matrix1,matrix2):
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    ##print(nr,nc)
    for ir in range(nr):
        for jc in range(nc):
            ##print(ir,jc)
            matrix2[ir][jc]=matrix1[ir][jc]
    return(matrix2)

def writearray(matrix):
    nr=len(matrix) # get row count
    nc=len(matrix[0]) # get column count
    import numpy as np
    new_list = list(np.around(np.array(matrix), 3))    
    for ir in range(nr):
        print(ir,new_list[ir][:])
    return()

localfile = open("PotentialFnSheetpile2.txt","r") # connect and read file for 2D gw model
deltax = float(localfile.readline())
deltay = float(localfile.readline())
deltaz = float(localfile.readline())
nrows = int(localfile.readline())
ncols = int(localfile.readline())
tolerance = float(localfile.readline())
maxiter = int(localfile.readline())
distancex = [] # empty list
distancex.append([float(n) for n in localfile.readline().strip().split()])
distancey = [] # empty list
distancey.append([float(n) for n in localfile.readline().strip().split()])
boundarytop = [] #empty list
boundarytop.append([float(n) for n in localfile.readline().strip().split()])
boundarybottom = [] #empty list
boundarybottom.append([int(n) for n in localfile.readline().strip().split()])
boundaryleft = [] #empty list
boundaryleft.append([int(n) for n in localfile.readline().strip().split()])
boundaryright = [] #empty list
boundaryright.append([int(n) for n in localfile.readline().strip().split()])
head =[] # empty list
for irow in range(nrows):
        head.append([float(n) for n in localfile.readline().strip().split()])
hydcondx = [] # empty list
for irow in range(nrows):
        hydcondx.append([float(n) for n in localfile.readline().strip().split()])
hydcondy = [] # empty list
for irow in range(nrows):
        hydcondy.append([float(n) for n in localfile.readline().strip().split()])
localfile.close() # Disconnect the file
##
amat = [[0 for j in range(ncols)] for i in range(nrows)]
bmat = [[0 for j in range(ncols)] for i in range(nrows)]
cmat = [[0 for j in range(ncols)] for i in range(nrows)]
dmat = [[0 for j in range(ncols)] for i in range(nrows)]
##
for irow in range(1,nrows-1):
    for jcol in range(1,ncols-1):
        amat[irow][jcol] = (( hydcondx[irow-1][jcol  ]+ hydcondx[irow  ][jcol  ]) * deltaz ) /(2.0*deltax**2)
        bmat[irow][jcol] = (( hydcondx[irow  ][jcol  ]+ hydcondx[irow+1][jcol  ]) * deltaz ) /(2.0*deltax**2)
        cmat[irow][jcol] = (( hydcondy[irow  ][jcol-1]+ hydcondy[irow  ][jcol  ]) * deltaz ) /(2.0*deltay**2)
        dmat[irow][jcol] = (( hydcondy[irow  ][jcol  ]+ hydcondy[irow  ][jcol+1]) * deltaz ) /(2.0*deltay**2)
##
headold = [[0 for jc in range(ncols)] for ir in range(nrows)] #force new matrix
headold = update(head,headold) # update
##writearray(head)
##print("----")
##writearray(headold)
##print("--------")
tolflag = False
for iter in range(maxiter):
##    print("begin iteration")
##    writearray(head)
##    print("----")
##    writearray(headold)
##    print("--------")

# Boundary Conditions

# first and last row special == no flow boundaries
    for jcol in range(ncols):
        if boundarytop[0][jcol] == 0: # no - flow at top
            head [0][jcol ] = head[1][jcol ]
        if boundarybottom[0][ jcol ] == 0: # no - flow at bottom
            head [nrows-1][jcol ] = head[nrows-2][jcol ]
# first and last column special == no flow boundaries     
    for irow in range(nrows): 
        if  boundaryleft[0][ irow ] == 0:
            head[irow][0] = head [irow][1] # no - flow at left
        if boundaryright[0][ irow ] == 0: 
            head [irow][ncols-1] = head[ irow ][ncols-2] # no - flow at right
# interior updates
    for irow in range(1,nrows-1):
        for jcol in range(1,ncols-1):
            head[irow][jcol]=( amat[irow][jcol]*head[irow-1][jcol  ] 
                              +bmat[irow][jcol]*head[irow+1][jcol  ] 
                              +cmat[irow][jcol]*head[irow  ][jcol-1] 
                              +dmat[irow][jcol]*head[irow  ][jcol+1])/(amat[ irow][jcol ]+ bmat[ irow][jcol ]+ cmat[ irow][jcol ]+ dmat[ irow][jcol ])
# test for stopping iterations
##    print("end iteration")
##    writearray(head)
##    print("----")
##    writearray(headold)
    percentdiff = sse(head,headold)
    if  percentdiff <= tolerance:
        print("Exit iterations in velocity potential because tolerance met ")
        print("Iterations =" , iter+1 ) ;
        tolflag = True
        break
    headold = update(head,headold)
print("End Calculations")
print("Iterations    = ",iter+1)
print("Closure Error = ",round(percentdiff,3))
print("Head Map")
print("----")
writearray(head)
print("----")
############# Contour Plot
my_xyz = [] # empty list
for irow in range(nrows):
    for jcol in range(ncols):
        my_xyz.append([distancex[0][jcol],distancey[0][irow],head[irow][jcol]])
import pandas
my_xyz = pandas.DataFrame(my_xyz) # convert into a data frame
#print(my_xyz) # activate to examine the dataframe
import numpy 
import matplotlib.pyplot
from scipy.interpolate import griddata
# extract lists from the dataframe
coord_x = my_xyz[0].values.tolist() # column 0 of dataframe
coord_y = my_xyz[1].values.tolist() # column 1 of dataframe
coord_z = my_xyz[2].values.tolist() # column 2 of dataframe
coord_xy = numpy.column_stack((coord_x, coord_y))
# Set plotting range in original data units
lon = numpy.linspace(min(coord_x), max(coord_x), 3000)
lat = numpy.linspace(min(coord_y), max(coord_y), 800)
X, Y = numpy.meshgrid(lon, lat)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z = griddata(numpy.array(coord_xy), numpy.array(coord_z), (X, Y), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(7.5, 4)
levels1 = [1,2,3,4,5,6,7,8,9,10]
CS = ax.contour(X, Y, Z, levels1)
ax.clabel(CS, inline=2, fontsize=16)
ax.set_title('Contour Plot of Heads from Sheetpile2 Input')


# :::{note}
# If you have to do this a lot, you could automate the "file rewrite" and have the program run the two instances back to back then make the contour plots
# :::
# 
# Here's the input file for the domain decomposition stream function calculations
# 
# ```
# 10
# 10
# 1
# 9
# 15
# 1e-16
# 5000
# 0 10 20 30 40 50 60 70 80 90 100 110 120 130 140
# 80 70 60 50 40 30 20 10 0
# 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 0 0 0 0 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# ```

# In[397]:


def sse(matrix1,matrix2):
    sse=0.0
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    for ir in range(nr):
        for jc in range(nc):
            sse=sse+(matrix1[ir][jc]-matrix2[ir][jc])**2
    return(sse)

def update(matrix1,matrix2):
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    ##print(nr,nc)
    for ir in range(nr):
        for jc in range(nc):
            ##print(ir,jc)
            matrix2[ir][jc]=matrix1[ir][jc]
    return(matrix2)

def writearray(matrix):
    nr=len(matrix) # get row count
    nc=len(matrix[0]) # get column count
    import numpy as np
    new_list = list(np.around(np.array(matrix), 3))    
    for ir in range(nr):
        print(ir,new_list[ir][:])
    return()

localfile = open("StreamFnSheetpile2.txt","r") # connect and read file for 2D gw model
deltax = float(localfile.readline())
deltay = float(localfile.readline())
deltaz = float(localfile.readline())
nrows = int(localfile.readline())
ncols = int(localfile.readline())
tolerance = float(localfile.readline())
maxiter = int(localfile.readline())
distancex = [] # empty list
distancex.append([float(n) for n in localfile.readline().strip().split()])
distancey = [] # empty list
distancey.append([float(n) for n in localfile.readline().strip().split()])
boundarytop = [] #empty list
boundarytop.append([float(n) for n in localfile.readline().strip().split()])
boundarybottom = [] #empty list
boundarybottom.append([int(n) for n in localfile.readline().strip().split()])
boundaryleft = [] #empty list
boundaryleft.append([int(n) for n in localfile.readline().strip().split()])
boundaryright = [] #empty list
boundaryright.append([int(n) for n in localfile.readline().strip().split()])
stream =[] # empty list
for irow in range(nrows):
        stream.append([float(n) for n in localfile.readline().strip().split()])
hydcondx = [] # empty list
for irow in range(nrows):
        hydcondx.append([float(n) for n in localfile.readline().strip().split()])
hydcondy = [] # empty list
for irow in range(nrows):
        hydcondy.append([float(n) for n in localfile.readline().strip().split()])
localfile.close() # Disconnect the file
##
amat = [[0 for j in range(ncols)] for i in range(nrows)]
bmat = [[0 for j in range(ncols)] for i in range(nrows)]
cmat = [[0 for j in range(ncols)] for i in range(nrows)]
dmat = [[0 for j in range(ncols)] for i in range(nrows)]
##
for irow in range(1,nrows-1):
    for jcol in range(1,ncols-1):
        amat[irow][jcol] = (( hydcondx[irow-1][jcol  ]+ hydcondx[irow  ][jcol  ]) * deltaz ) /(2.0*deltax**2)
        bmat[irow][jcol] = (( hydcondx[irow  ][jcol  ]+ hydcondx[irow+1][jcol  ]) * deltaz ) /(2.0*deltax**2)
        cmat[irow][jcol] = (( hydcondy[irow  ][jcol-1]+ hydcondy[irow  ][jcol  ]) * deltaz ) /(2.0*deltay**2)
        dmat[irow][jcol] = (( hydcondy[irow  ][jcol  ]+ hydcondy[irow  ][jcol+1]) * deltaz ) /(2.0*deltay**2)
##
streamold = [[0 for jc in range(ncols)] for ir in range(nrows)] #force new matrix
streamold = update(stream,streamold) # update
##writearray(stream)
##print("----")
##writearray(streamold)
##print("--------")
tolflag = False
for iter in range(maxiter):
##    print("begin iteration")
##    writearray(stream)
##    print("----")
##    writearray(streamold)
##    print("--------")

# Boundary Conditions

# first and last row special == no flow boundaries
    for jcol in range(ncols):
        if boundarytop[0][jcol] == 0: # no - flow at top
            stream [0][jcol ] = stream[1][jcol ]
        if boundarybottom[0][ jcol ] == 0: # no - flow at bottom
            stream [nrows-1][jcol ] = stream[nrows-2][jcol ]
# first and last column special == no flow boundaries     
    for irow in range(nrows): 
        if  boundaryleft[0][ irow ] == 0:
            stream[irow][0] = stream [irow][1] # no - flow at left
        if boundaryright[0][ irow ] == 0: 
            stream [irow][ncols-1] = stream[ irow ][ncols-2] # no - flow at right
# interior updates
    for irow in range(1,nrows-1):
        for jcol in range(1,ncols-1):
            stream[irow][jcol]=( amat[irow][jcol]*stream[irow-1][jcol  ] 
                              +bmat[irow][jcol]*stream[irow+1][jcol  ] 
                              +cmat[irow][jcol]*stream[irow  ][jcol-1] 
                              +dmat[irow][jcol]*stream[irow  ][jcol+1])/(amat[ irow][jcol ]+ bmat[ irow][jcol ]+ cmat[ irow][jcol ]+ dmat[ irow][jcol ])
# test for stopping iterations
##    print("end iteration")
##    writearray(stream)
##    print("----")
##    writearray(streamold)
    percentdiff = sse(stream,streamold)
    if  percentdiff <= tolerance:
        print("Exit iterations in Stream Function because tolerance met ")
        print("Iterations =" , iter+1 ) ;
        tolflag = True
        break
    streamold = update(stream,streamold)
print("End Calculations")
print("Iterations    = ",iter+1)
print("Closure Error = ",round(percentdiff,3))
print("Stream Function Map")
print("----")
writearray(stream)
print("----")
####################### Contour Plot ###############
my_xyz2 = [] # empty list
for irow in range(nrows):
    for jcol in range(ncols):
        my_xyz2.append([distancex[0][jcol],distancey[0][irow],stream[irow][jcol]])
import pandas
my_xyz2 = pandas.DataFrame(my_xyz2) # convert into a data frame
#print(my_xyz) # activate to examine the dataframe
import numpy 
import matplotlib.pyplot
from scipy.interpolate import griddata
# extract lists from the dataframe
coord_x2 = my_xyz2[0].values.tolist() # column 0 of dataframe
coord_y2 = my_xyz2[1].values.tolist() # column 1 of dataframe
coord_z2 = my_xyz2[2].values.tolist() # column 2 of dataframe
coord_xy2 = numpy.column_stack((coord_x2, coord_y2))
# Set plotting range in original data units
lon = numpy.linspace(min(coord_x2), max(coord_x2), 3000)
lat = numpy.linspace(min(coord_y2), max(coord_y2), 800)
X2, Y2 = numpy.meshgrid(lon, lat)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z2 = griddata(numpy.array(coord_xy2), numpy.array(coord_z2), (X2, Y2), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(7.5, 4)
levels = [5,20,30,40,50,60,70,80,90,100]
CS2 = ax.contour(X2, Y2, Z2, levels )
ax.clabel(CS2, inline=2, fontsize=16)
ax.set_title('Contour Plot of Stream Function for Sheetpile2 Input')


# Now try both contour plot same plot canvas

# In[396]:


# Head (Velocity Potential Map)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z = griddata(numpy.array(coord_xy), numpy.array(coord_z), (X, Y), method='cubic')
Z2 = griddata(numpy.array(coord_xy2), numpy.array(coord_z2), (X2, Y2), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(7.5, 4)
levels1 = [5,6,7,8,9,10]
CS = ax.contour(X, Y, Z, levels1)
levels2 = [10,20,30,40,50,60,70,80,90,100]
CS2 = ax.contour(X2, Y2, Z2, levels2 )
ax.clabel(CS, inline=2, fontsize=16)
ax.clabel(CS2, inline=2, fontsize=12)
ax.set_title('Flownet for Sheetpile2 Input')


# ## References
# 
# 1. [Cleveland, T.G. (1997) *Groundwater Review* Notes to accompany "CIVE 7332 Flow and Transport Modeling for Environmental Engineering" at University of Houston](http://54.243.252.9/ce-5364-webroot/3-Readings/GroundwaterReview.pdf)
# 1. [Zheng, C. and Bennett, G.D. (1995) pp. 3-23 *Applied Contaminant Transport Modeling* Van Nostrand Reinhold](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/3advection/Advection.PDF)
# 2. [Cleveland, T.G. (2002) *Flownets* Notes to accompany "CIVE 7332 Flow and Transport Modeling for Environmental Engineering" at University of Houston](http://54.243.252.9/ce-5364-webroot/3-Readings/flownet_1.pdf)
# 3. [Cleveland, T.G. (1997) *Velocity Potential - Stream Function Ideal Flow Model (circa 1999) (Excel)*](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/5nonreactivetransport/VelocityPotential-StreamFunction-FDM.xls)
# 4. [Cleveland, T.G. (2002) *Advection* Notes to accompany "CIVE 7332 Flow and Transport Modeling for Environmental Engineering" at University of Houston](http://54.243.252.9/ce-5364-webroot/3-Readings/AdvectionNotes.pdf)
# 4. [Bear, J. (1972) *Dynamics of Fluids in Porous Media* McGraw Hill (pp. 236-241)](https://d1wqtxts1xzle7.cloudfront.net/31171747/195055535-libre.pdf?1392371142=&response-content-disposition=inline%3B+filename%3DDynamics_of_fluids_in_porous_media.pdf&Expires=1695231543&Signature=fcj7Wef3HIA7wlTx~LJhmfFgQJIrRLnrwEgqd2KIjnsouiRrFZpLAgMw-gRJ7oxI1~h89bo-YpAQuhLHZc1vtNFq5d0QBrxwYRbAvr5jztdUDHWZrfjBPYBgujy5WCnrrtoN7GKrziCwbk7mDi1AUyBnC4RDidrKgBV-bMOpJR4ZR8~L6BTEPXhBAQJbLohdpWi8Ni6VUl33~rEQaum8NMcY11P6okNvXbXKft3vdYwjEK5NXezeVe6dQpYIiBcyPVqkFahRD9CFLXLHZsxXryzDT~x9pszx86ka0kXYN9y1Y7RzyAgZQaB5YWD8XZhK4w2PoIEVgIvGeuCxxt099Q__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
# <!--(http://54.243.252.9/ce-5364-webroot/3-Readings/DFPM-Flownets.pdf)-->
