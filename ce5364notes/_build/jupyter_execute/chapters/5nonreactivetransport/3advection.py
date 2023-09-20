#!/usr/bin/env python
# coding: utf-8

# # Advection
# 
# Advection (convection) is the transport of dissolved or suspended material by motion of the host fluid. The prediction of the direction and amount of material transported requires knowledge of the fluid velocity field (the velocity of a fluid particle).  
# 
# ![](labeledparcel.png)
# 
# The figure depicts the flow of a labeled fluid in a tube.  One can use the sketch to define various useful properties of the labeled fluid portion as listed.
# 
# |Property|Expression|
# |---|---|
# |Mass of labeled fluid|$m=\rho A\Delta L$ |
# |Mass of tracer|$m=C A\Delta L$|
# |Distance traveled by leading (trailing edge)|$x=\Delta L$|
# |Time required to travel distance|$time = \Delta t$|
# |Velocity of leading edge|$u = \frac{x}{time} = \frac{\Delta L}{\Delta t}$|
# |Mass through circular frame/unit time|$m=\frac{\rho A\Delta L}{\Delta t}$|
# |Tracer through circular frame/unit time|$m=\frac{C A\Delta L}{\Delta t}$|
# |Fluid mass flux|$J=\rho\frac{UA}{A}=\rho\frac{Q}{A}=\rho U$|
# |Tracer mass flux|$J=C\frac{UA}{A}=C\frac{Q}{A}=C U$|
# 
# The advective flux is the product of the quantity of interest (in this case mass of either host fluid or tracer) and the velocity term.  Typically the mean section velocity is used (pipe flow, open channel flow) because fine scale resolution of the velocity field is impossible.  In porous media, the pore velocity or average linear velocity is used.
# Advection calculations usually use mean section velocity based on discharge measurements.
# 

# ## Modeling Advection 
# 
# To build models, we simply apply the Reynolds Transport Theorem to the advective flux component something like:
# 
# ![](advectivefrux.png)
# 
# ## Modeling Tools
# 
# Moved to Modeling Advection
# 

# ## Flownets (pp. 30-34)
# 
# Moved to Essential Groundwater Review
# 
# A related concept is flownets as outlined in [Cleveland, T.G. (2002) *Flownets* Notes to accompany "CIVE 7332 Flow and Transport Modeling for Environmental Engineering" at University of Houston](http://54.243.252.9/ce-5364-webroot/3-Readings/flownet_1.pdf)
# 
# Numerical generation of flownets can be accomplished using a spreadsheet, python script, or MODFLOW.  
# 
# A simple spreadsheet example is available from
# 
# [Cleveland, T.G. (1997) *Velocity Potential - Stream Function Ideal Flow Model (circa 1999) (Excel)*](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/5nonreactivetransport/VelocityPotential-StreamFunction-FDM.xls)
# 
# 

# ## References
# 
# 1. [Zheng, C. and Bennett, G.D. (1995) pp. 3-23 *Applied Contaminant Transport Modeling* Van Nostrand Reinhold](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/3advection/Advection.PDF)
# 2. [Cleveland, T.G. (2002) *Advection* Notes to accompany *"CIVE 7332 Flow and Transport Modeling for Environmental Engineering" at University of Houston*](http://54.243.252.9/ce-5364-webroot/3-Readings/AdvectionNotes.pdf)
# 3. [Cleveland, T.G. (2002) *Particle Tracking in a Spreadsheet* Notes to accompany "CIVE 7332 Flow and Transport Modeling for Environmental Engineering" at University of Houston](http://54.243.252.9/ce-5364-webroot/3-Readings/parttrack_1.pdf)
# 4. [Bear, J. (1972) *Dynamics of Fluids in Porous Media* McGraw Hill (pp. 236-241)](https://d1wqtxts1xzle7.cloudfront.net/31171747/195055535-libre.pdf?1392371142=&response-content-disposition=inline%3B+filename%3DDynamics_of_fluids_in_porous_media.pdf&Expires=1695231543&Signature=fcj7Wef3HIA7wlTx~LJhmfFgQJIrRLnrwEgqd2KIjnsouiRrFZpLAgMw-gRJ7oxI1~h89bo-YpAQuhLHZc1vtNFq5d0QBrxwYRbAvr5jztdUDHWZrfjBPYBgujy5WCnrrtoN7GKrziCwbk7mDi1AUyBnC4RDidrKgBV-bMOpJR4ZR8~L6BTEPXhBAQJbLohdpWi8Ni6VUl33~rEQaum8NMcY11P6okNvXbXKft3vdYwjEK5NXezeVe6dQpYIiBcyPVqkFahRD9CFLXLHZsxXryzDT~x9pszx86ka0kXYN9y1Y7RzyAgZQaB5YWD8XZhK4w2PoIEVgIvGeuCxxt099Q__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
# <!--(http://54.243.252.9/ce-5364-webroot/3-Readings/DFPM-Flownets.pdf)-->

# In[ ]:




