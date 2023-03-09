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
# |Property|Expression||
# |---|---||
# |Mass of labeled fluid|$m=\rho A\Delta L$ ||
# |Mass of tracer|$m=C A\Delta L$||
# |Distance traveled by leading (trailing edge)|$x=\Delta L$||
# |Time required to travel distance|$time = \Delta t$||
# |Velocity of leading edge|$u = \frac{x}{time} = \frac{\Delta L}{\Delta t}$||
# |Mass through circular frame/unit time|$m=\frac{\rho A\Delta L}{\Delta t}$||
# |Tracer through circular frame/unit time|$m=\frac{C A\Delta L}{\Delta t}$||
# |Fluid mass flux|$$J=\rho\frac{UA}{A}=\rho\frac{Q}{A}=\rho U$$|
# |Tracer mass flux|$$J=C\frac{UA}{A}=C\frac{Q}{A}=C U$$|
# 
# The advective flux is the product of the quantity of interest (in this case mass of either host fluid or tracer) and the velocity term.  Typically the mean section velocity is used (pipe flow, open channel flow) because fine scale resolution of the velocity field is impossible.  In porous media, the pore velocity or average linear velocity is used.
# Advection calculations usually use mean section velocity based on discharge measurements.
# 

# In[ ]:




