#!/usr/bin/env python
# coding: utf-8

# # Decay
# 
# Exponential decay of constituents in groundwater describes the gradual reduction in the concentration of dissolved substances in groundwater over time due to natural attenuation processes such as radioactive decay, biodegredation, and hydrolysis. Typically, as groundwater flows through an aquifer, constituents such as contaminants or dissolved solutes may undergo degradation, or other reactive processes. These processes may follow exponential decay kinetics, where the rate of decrease in concentration is proportional to the remaining concentration. As a result, the concentration of constituents diminishes rapidly initially and then gradually approaches a stable, lower level over time. Understanding exponential decay in groundwater is critical for assessing the long-term behavior of contaminants, designing effective groundwater remediation strategies, and safeguarding the quality of groundwater resources.
# 
# ## 1-st Order Decay
# 
# First-order decay is a mathematical model used to describe the exponential decrease in the concentration of a substance over time. It is commonly applied in various fields, including chemistry, physics, biology, and environmental science, to represent processes such as radioactive decay, chemical reactions, and the natural attenuation of contaminants. The mathematics of first-order decay is defined by the following equation:
# 
# $$C(t)=C_0 \cdot e^{-\lambda t}$$
# 
# Where:
# 
# - $C(t)$ represents the concentration of the substance at time $t$.
# - $C_0$ is the initial concentration of the substance at $t=0$.
# - $\lambda$ is the first-order rate constant, which determines the rate of decay.
# 
# Key points about first-order decay:
# 
# - Exponential Decrease: The concentration C(t)C(t) decreases exponentially over time. This means that the rate of decrease is proportional to the current concentration, resulting in a continuous, smooth curve that approaches zero but never reaches it completely.
# 
# - Rate Constant ($\lambda$): The rate constant $\lambda$ is a positive constant that characterizes the speed of the decay process. It is unique to each specific decay or reaction and is often expressed in units of reciprocal time (e.g., per day, per year). A larger $\lambda$ value indicates a faster decay rate.
# 
# - Half-Life: The half-life ($t_{1/2}$) is a valuable parameter associated with first-order decay. It represents the time it takes for the concentration to decrease to half of its initial value ($\frac{C_0}{2}$). The relationship between the rate constant and half-life is given by $t_{1/2}=0.693 \lambda$.
# 
# - Independence of Concentration: The rate of decay is independent of the initial concentration $C_0$. This means that substances undergoing first-order decay will always decrease by the same proportion in a given time interval, regardless of their initial concentrations.
# 
# ## Hydrolysis
# 
# Hydrolysis is a chemical reaction in the fate and transport of contaminants in groundwater. It involves the breakdown of certain chemical compounds when they come into contact with water molecules. In the context of groundwater contaminants, hydrolysis can transform hazardous substances into less harmful or more easily degradable forms. This reaction can alter the chemical composition and reactivity of contaminants, affecting their persistence in the subsurface environment. Understanding the occurrence and rate of hydrolysis reactions is crucial for predicting the behavior and potential risks associated with groundwater contaminants, especially for compounds like pesticides and industrial chemicals that are prone to hydrolytic degradation. Contaminant hydrolysis can be a key factor in groundwater remediation strategies and in the assessment of long-term environmental impacts.
# 
# While temperature sensitive hydrolysis is typically described using a first-order decay model 
# 
# ## Electron Transfer
# 
# Electron transfer, often referred to as oxidation-reduction (redox) reactions, plays a pivotal role in the fate and transformation of contaminants in groundwater. These reactions involve the exchange of electrons between different chemical species, leading to changes in the oxidation states of the participating compounds. In the context of groundwater contaminants, redox reactions can either facilitate the degradation or transformation of pollutants or, conversely, promote their persistence and mobility. For instance, certain contaminants may undergo reduction reactions, gaining electrons and becoming less toxic or mobile. Conversely, oxidation reactions can render contaminants more mobile or transform them into more harmful forms. Understanding the redox chemistry of groundwater contaminants is crucial for assessing the potential risks, remediation strategies, and long-term behavior of these substances in the subsurface environment. It is a complex yet fundamental aspect of contaminant fate in groundwater systems.
# 
# Like hydrolysis electron transfer processes are typically modeled using a first-order decay model.
# 
# 
# ## Incorporation into ADE
# 
# 1-st order decay is incorporated into the transport equation as another source/sink term:
# 
# $$\frac{\partial C}{\partial t}  =  \frac{\partial}{\partial x} D_x \frac{\partial C}{\partial x} - v_x \frac{\partial C}{\partial x} - \lambda C$$
# 
# :::{note}
# Obviously other reactions can be included - they simply appear as a source/sink term.  Whether they manifest as simply as the terms herein depends on the nature of the process.  
# :::

# ## References
# 
# 1. [Cleveland, T.G. (1998) *Adsorbtion-2* Notes to accompany *"CIVE 7332 Flow and Transport Modeling for Environmental Engineering" at University of Houston*](http://54.243.252.9/ce-5364-webroot/3-Readings/adsorb_2.pdf)

# In[ ]:




