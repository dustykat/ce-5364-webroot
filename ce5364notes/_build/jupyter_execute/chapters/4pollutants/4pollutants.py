#!/usr/bin/env python
# coding: utf-8

# # Pollutants

# ## Concentrations
# 
# Solvent phase (soil, air, water) is the phase that contains the solute (constituient) phase. The amount of solute contained in the solvent is usually expressed as some kind of concentration either massic(mass/mass) or volumetric(mass/volume).
# 
# Concentrations are expressed in a variety of units:
# 
# |Type|Meaning|Symbol|
# |---|---|---|
# |Volumetric|mass/volume|$\frac{mg}{L}$|
# |Massic|mass/mass|$ppm$|
# |Molarity|moles/volume|$M=\frac{mol}{L}$|
# |Molality|moles/mass|$m=\frac{mol}{kg}$|
# |Mole Fraction (also partial pressures)|moles/moles|$X_{species}$|
# |Equivalents|moles$\times$valence/volume|$Eq$|
# |Activity|disintegrations/second/volume|$\frac{Bq}{L}$ - a contrived unit|
# 
# The most common in environmental flow and transport models are volumetric and massic.  
# 
# There are cases where multiple phases are present (multi-phase transport) and multiple components in a solute mixture (multi-component).
# 
# Emulsions are a special kind of two-(or more)phase system where the emulsion behaves as a single phase with respect to motion.  Oil-in-water, water-in-oil, biosolids-in-water (technically a slurry), coal-in-water (a slurry) are examples of common emulsions.
# 
# I use the terms constituients and pollutants more or less interchangeably; however a pollutant is a value judgement - if the particular constituient is **undesirable**, for example methyl-ethyl death in water - then its a pollutant, otherwise its just a lowly *constituient*.  The distinction is irrelevant unless lawyers, judges, and money are involved - then be careful; someone goes to jail, and someone loses their doublewide if you get your mords wixed!

# ## Types
# 
# Lots of types of pollutants, their classification below is somewhat arbitrary but useful in assessing impacts and remediation methods.
# 
# >**Pathogens**
# Bacteria, protozoa, virus, prions that can cause disease and death. Usually associated
# with waste from human activities.<br>
# >**Oxygen Demanding Materials**
# Usually organic chemicals associated with human activities. Often will degrade naturally
# of sufficient time and O2 are available.<br>
# >**Inorganic Materials**
# Cations and anions that pose a threat to health or economic use of air, soil, or water.
# Metals that are problematic, but not toxic (see hazardous chemicals).<br>
# >**Hazardous Chemicals**
# This category is further defined by [listed versus characteristic](https://www.epa.gov/hw/defining-hazardous-waste-listed-characteristic-and-mixed-radiological-wastes) versus hazardous materials.  Listed means the material is on a list; characteristic means it could exhibit behavior from:
# >- **Ignitability**-Materials that pose a fire hazard during routine handling (e.g.[gasoline](https://about.usps.com/posters/pos138/pos138_hazard_004.htm))
# >- **Corrosivity**-Materials that require special containers because they corrode standard containers. (e.g. [hydrogen fluoride](https://emergency.cdc.gov/agent/hydrofluoricacid/basics/facts.asp)
# >- **Reactivity**-Materials that react spontaneously with air or water, are unstable to shock or heat, generate toxic gases, or explode during routine handling. (e.g. [white phosphorous](https://www.epa.gov/sites/default/files/2016-09/documents/phosphorus.pdf))
# >- **Toxicity**-Materials that release toxicants in quantities that pose a threat to human or environmental health when improperly handled. (e.g. [Organophosphate pesticides](https://emergency.cdc.gov/agent/nerve/tsd.asp))<br><br>
# >Many compounds exhibit multiple characteristics - but one is enough to earn a spot on the pollutant show.

# ## Sources
# 
# 1. By design.  Septic tanks, injection wells, land application.
# 2. Storage systems (failure). Leaks from landfills, tanks.
# 3. Transmission system (failure). Pipelines, trucks, trains.
# 4. Non-point sources. Irrigation,urban runoff,mining drainage
# 5. Wells, excavations.
# 6. Natural.  Salt waters
# 
# A nice [EPA Fact Sheet](https://www.epa.gov/sites/default/files/2015-08/documents/mgwc-gwc1.pdf) discusses sources in some detail.
# 
# A typical priority list (circa 1990s) is:
# 
# - Inorganics
# - Organics
# - Hydrocarbons
# - Solvents
# - Chlorinated hydrocarbons
# - Metals
# - Emerging contaminants
# 
# which pretty much covers everything!  The category overlaps are intentional.

# ## Exposure Sources and Effects
# A subset of sources, probably more useful in the overall context of transport are exposure sources:
# > **Biological cycles**: Uptake and decay of animal and plant life, excretion of materials, etc.<br>
# > **Domestic waste**: Discharges of raw and treated wastewater. <br>
# > **Industrial waste**:Discharges of raw and treated wastewater, discharges of raw and treated off-gases. <br>
# > **Nonpoint source**: Landfill leachate, stormwater runoff. As a rule of thumb, a nonpoint source is any source
# that you cannot “point” to. (Although humorous, this definition is quite practical) <br>
# 
# Effects (of exposure) are classified as:
# >**Acute** effects imply some immediate damage; effect is noticed quickly<br>
# >**Chronic** effects imply long term damage; it may be many years until effect is noticed.
# 
# ### Exposure and Risk
# Fundamental question is what are the risks associated with assimilation of a certain compound at a certain concentration over short (acute) and long (chronic) term?
# 
# ### Risk Assessment Tools
# Toxic response analysis, Exposure Concentration, Cost-benefit analysis, Revealed and expressed preference analysis
# 
# ### Exposure Concentration
# - **Source of compound, production rates, and release rates to environment.**
# - **Characteristics of compound relevant to its ability to travel and react in the natural environment.**
# - Data to estimate the population at risk. Occupation. Medical surveillance.
# - Socioeconomic use habits. The source and compound characteristics can be incorporated into models. 
# 
# The actual risk analysis is a second step.
# 
# ## Dose/Response Concepts
# 
# For response to a contaminant the material must be toxic and the receptor must be exposed. 
# A highly toxic material with no exposure is not much of a hazard. 
# A mildly toxic material with high exposure could be very hazardous. 
# 
# Environmental toxicology typically assumes that for dilute pollutants, toxicity is proportional to concentration and duration. The longer the contact time, the greater the probability of toxic effects. Amount of toxicant initially absorbed is gradually decreased by metabolic activity and excretion with other bodily wastes.
# 
# The figure below is a conceptual retention curve for some pollutant
# 
# ![](retentioncurve.png)
# 
# Time integral of the retention curve is called the *retention dose*.
# The lifetime retention dose is called the *dose commitment*.
# A typical formula for estimating retention dose is: 
# 
# $$R=C \times U \times D$$
# 
# where $R$ is the retention dose, $C$ is the exposure concentration, $U$ is the uptake rate, and $D$ is the exposure duration.  
# :::{note}
# Obviously units are not supplied, we are in the realm of toxicology - outside scope of this document, but some background is needed, hence the overly simplified discussion herein.
# :::
# 
# ### Threshold Concept
# In drug therapy there exist threshold doses where response to the drug changes. Typically
# two thresholds in drugs exist, a lower bound where no therapeutic effect is observed, and
# an upper threshold where damage (usually death) occurs. 
# 
# Similarly toxicants are thought to also have thresholds. A practice used is that one-percent of the threshold dose for
# animals is acceptable for humans (normalized by body weight).
# 
# ### Latency Concept
# In support of the threshold hypothesis it has been observed that the period between exposure and response (tumors) for carcinogen increases as dose decreases. Generally it is accepted that the product of dose and latent time raised to some power is a constant.
# 
# ## Estimating Fate of Pollutants
# The fundamental tool used to predict concentrations in the environment is the mathematical model, supported by data, laboratory experiments, and judgement. 
# 
# Models are used in many disciplines such as:
# - Economics: predict market activity, occurrence or recessions or periods of productivity.
# - Meteorology: short-term weather conditions, long-term climatological conditions. 
# - Engineering: predict performance of engineered systems. **Predict transport and fate of pollutants.**
# 
# Keeping this in mind, much of these notes is aimed at building useful models to support engineering decisions regarding groundwater quality.
# 

# ## Response
# 
# - Health effects
# - Economic effects
# - Legal effects

# ## References
# 
# 1. [Becquerel (radioactivity unit)](https://en.wikipedia.org/wiki/Becquerel)
# 2. [Toxicity (Cleveland notes circa 2001)]()
