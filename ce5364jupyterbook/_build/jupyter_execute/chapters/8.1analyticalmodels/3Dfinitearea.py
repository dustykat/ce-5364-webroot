#!/usr/bin/env python
# coding: utf-8

# # 3D - Advection-Dispersion, Finite-Area, Constant Production (Injection) Source 
# 
# The sketch depicts a planar source zone Y units wide and Z units tall, centered at (0,0,0). 
# 
# ![](3Dgeom2.png)
# 
# The analytical model (Domenico and Robbins, 1985) is obtained by convolution of instantaneous sources (described in detail in Yuan, 1995):
# 
# $$ C(x,y,t) = \frac{C_0}{8} \cdot \textit{erfc}[\frac{(x - v t) }{ (2 \sqrt{D_x t))}}] \cdot [\textit{erf}(\frac{(y + \frac{Y}{2}) }{ (2 \sqrt{\frac{D_y}{v} x))}}) - \textit{erf} (\frac{(y - \frac{Y}{2}) }{ (2 \sqrt{\frac{D_y}{v} x))}})] \cdot [\textit{erf}(\frac{(z + \frac{Z}{2}) }{ (2 \sqrt{\frac{D_z}{v} x))}}) - \textit{erf} (\frac{(z - \frac{Z}{2}) }{ (2 \sqrt{\frac{D_z}{v} x))}})]$$
# 
# :::{note}
# This solution is identical to Equation 6.33, with $\lambda = 0$, $R = 1$.  
# :::
# 
# A prototype function is
# 

# In[1]:


def c3dad(conc0, distx, disty, distz, lenX, lenY, lenZ, dispx, dispy, dispz, velocity, etime):
    import math
    from scipy.special import erf, erfc # scipy needs to already be loaded into the kernel
    # Constant of integration
    term1 = conc0 / 8.0

    # Centerline axis solution
    arg1 = (distx - velocity*etime) / (2*math.sqrt(dispx*velocity*etime)) #dispx is dispersivity
    term2 = erfc(arg1)

    # Off-axis solution, Y direction
#    arg2 = 2.0 * math.sqrt(dispy*distx / velocity)
    arg2 = 2.0 * math.sqrt(dispy*distx) #dispy is dispersivity
    arg3 = disty + 0.5*lenY
    arg4 = disty - 0.5*lenY
    term3 = erf(arg3 / arg2) - erf(arg4 / arg2)

    # Off-axis solution, Z direction
#    arg5 = 2.0 * math.sqrt(dispz*distx / velocity)
    arg5 = 2.0 * math.sqrt(dispz*distx) #dispz is dispersivity
    arg6 = distz + 0.5*lenZ
    arg7 = distz - 0.5*lenZ
    term4 = erf(arg6 / arg5) - erf(arg7 / arg5)

    # Convolve the solutions
    c3dad = term1 * term2 * term3 * term4
    return c3dad


# :::{note}
# This is 3D part is incomplete. Needs
# - An example
# - Script to render an xyz density plot 
# :::

# ## References
# 
# 1. [Domenico, P.A. and Robbins, G.A. (1985), A New Method of Contaminant Plume Analysis. Groundwater, 23: 476-485. https://doi.org/10.1111/j.1745-6584.1985.tb01497.x](https://ngwa.onlinelibrary.wiley.com/doi/10.1111/j.1745-6584.1985.tb01497.x)
# 2. [Paladino, O. , Moranda, A.,  Massabó, M., and  Robbins, G. (2017). Analytical Solutions of Three-Dimensional Contaminant Transport Models with Exponential Source Decay. Groundwater. 56. 10.1111/gwat.12564. ](http://54.243.252.9/ce-5364-webroot/3-Readings/gwatnorev.pdf)
# 2. [**SSANTS2.xlsm** (Excel Macro Sheet(s)) - Choose Tabsheet **?????**](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/7analyticalmodels/SSANTS2.xlsm)
# 3. [Yuan, D, (1995)  *Accurate approximations for one-, two-, and three-dimensional groundwater mass transport from an exponentially decaying contaminant source.* MS Thesis, Department of Civil and Environmental Engineering, University of Houston. ](http://54.243.252.9/about-me-webroot/about-me/MyWebPapers/thesis/yuan_thesis/Groundwater_transport.pdf)
# 4. [Chuang, Lu-Chia, (1998) *A guidance system for choosing analytical contaminant transport models.* Doctoral Dissertation, Department of Civil and Environmental Engineering, University of Houston, Houston, Texas. 222p.](http://54.243.252.9/about-me-webroot/about-me/MyWebPapers/thesis/ants_dissertation/Luke_Chuang.pdf)
# 5. [Analytical solutions for one-, two-, and three-dimensional solute transport in ground-water systems with uniform flow
# Open-File Report 89-56](https://pubs.usgs.gov/publication/ofr8956)
# 6. [Analytical solutions for one-, two-, and three-dimensional solute transport in ground-water systems with uniform flow
# Techniques of Water-Resources Investigations 03-B7 (supercedes above reference)](https://pubs.usgs.gov/publication/twri03B7)
