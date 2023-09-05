#!/usr/bin/env python
# coding: utf-8

# # Pollutants
# 
# Pollutants in groundwater refer to contaminating substances that have migrated into the underground water reservoirs, known as aquifers. These pollutants can include a wide range of chemicals, heavy metals, pesticides, fertilizers, industrial waste, and even naturally occurring substances like minerals and salts when they exceed desired levels. Contaminated groundwater poses a serious environmental and health risk, as it can affect drinking water quality and harm ecosystems when it reaches surface waters. Preventing and remedying groundwater pollution is crucial for safeguarding both human health and the environment.
# 
# >**Why we care** Globally, the reliance on groundwater for human settlement sustainment is a critical aspect of our water supply infrastructure. Groundwater, which is stored in underground aquifers, serves as a lifeline for countless communities around the world. It plays a pivotal role in sustaining human settlements by providing a consistent and often more reliable source of freshwater.
# >
# >Groundwater is utilized for various essential purposes, including drinking water supply, irrigation for agriculture, industrial processes, and even supporting ecosystems. Its importance becomes especially pronounced in regions where surface water sources such as rivers and lakes are scarce, unreliable, or subject to pollution and contamination.
# >
# >The sustainability of groundwater resources, however, faces significant challenges. Over-extraction, driven by population growth and increasing water demands, can lead to the depletion of aquifers. This unsustainable use can result in land subsidence, seawater intrusion into coastal aquifers, and the long-term degradation of water quality.
# >
# >Balancing the reliance on groundwater with sustainable management practices is crucial for the continued well-being of human settlements. Monitoring, conservation, and the implementation of responsible water management strategies are essential steps toward ensuring that groundwater remains a dependable resource for communities worldwide. This includes promoting water conservation, recharge of aquifers, and careful regulation of extraction to preserve this invaluable source of freshwater for generations to come.
# 

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
# From our textbook:
# 
# 1. By design.  Septic tanks, injection wells, land application.
# 2. Storage systems (failure). Leaks from landfills, tanks.
# 3. Transmission system (failure). Pipelines, trucks, trains.
# 4. Non-point sources. Irrigation,urban runoff,mining drainage
# 5. Wells, excavations.
# 6. Natural.  Salt waters.
# 
# >From ([www.springwellwater.com](https://www.springwellwater.com/10-potential-sources-of-groundwater-pollution/)):
# >
# >1. **Natural Sources.** Groundwater contamination won’t always be a result of human activity. Some substances found naturally in rocks and soils, such as arsenic, iron, chlorides, sulfates, fluoride, or radionuclides, can become dissolved in groundwater. Other naturally-occurring substances, such as decaying organic matter, can move in groundwater as particles. Some of these contaminants may accumulate in excess quantities, posing a health threat if consumed. Others may produce an unpleasant odor, taste, or color. Groundwater containing these materials needs to be treated before it is used for domestic uses.
# >2. **Pesticide and Fertilizer Use.** Agriculture is a huge source of groundwater pollution. The spreading of slurry, fertilizers, pesticides, fungicides, insecticides, herbicides, and animal waste on the land can result in pollutants, such as nitrates and bacteria, seeping into underground water sources. These pollutants can have severe adverse effects on plants, animals, and people who rely on these water sources. Some of them can even stay in the ground for many months to many years. Atrazine, a common weed killer, is linked to congenital disabilities, cancer, and low sperm counts in humans.
# >3. **Waste from Sewers and Other Pipelines.** Sewer pipes carrying wastes sometimes leak fluids into the surrounding soil and groundwater. Sewage consists of organic matter, heavy metals, inorganic salts, bacteria, viruses, and nitrogen. Similarly, improperly designed, located, constructed, or maintained septic systems could leak bacteria, viruses, household chemicals, and other contaminants into the groundwater, causing severe problems. Pipelines carrying industrial chemicals and oil brine have also been known to leak, especially when the materials transported through the pipes are corrosive.
# >4. **Improper Disposal of Hazardous Waste.** Many of us don’t realize that the way we dispose of waste can impact the quality of the same groundwater we rely on. When we improperly dispose of materials such as cooking and motor oils, lawn and garden chemicals, paints and paint thinners, medicines, disinfectants, etc., they usually end up in groundwater wells. Besides, many substances used in the industrial process should not be disposed of in drains at the workplace because they could contaminate a drinking water source. Pouring the wrong chemicals down the drain or neglecting to discard medication properly can harm your groundwater sources and, ultimately, your health and possibly that of the people living in your household.
# >5. **Natural Gas Drilling.** Hydraulic fracturing, or “fracking” is a process used to drill for natural gas. A mixture of chemicals is combined with water and forced deep into cracks in the ground, opening them to gain more access to the gas. EPA scientists are still investigating whether natural gas drilling is contaminating groundwater sources in some Western States. But many homeowners have abandoned their houses after methane seeped into the water, and at least one house exploded in 2003, killing three people inside.
# >6. **Mining and Quarrying.** Mining and quarrying can release pollutants previously trapped in rocks into surrounding underground water sources. Precipitation causes these soluble chemicals to leach into the groundwater below. These wastes often include acid, iron, sulfates, and aluminum. Furthermore, toxins such as lead and arsenic were used in 19th-century mining, and often persist in today’s abandoned mine shafts.
# >7. **Saltwater Contamination.** When aquifers near the coast are over-pumped, there’s a risk of creating a vacuum that can quickly be filled with salty seawater. Saltwater is undrinkable and useless for irrigation, decreasing the availability of the already scarce freshwater. Saltwater contamination is a major concern for many coastal communities that depend on wells for drinking water.
# >8. **Landfills.** Landfills are areas where our garbage is taken to be buried. They are supposed to have a protective bottom layer to prevent contaminants from leaching into groundwater. However, if there’s no layer or the layer is cracked, contaminants from the landfill (paint, acid, car batteries, household cleaners, etc.) can make their way down into groundwater. These contaminants can pose serious health risks to humans and animals. Most landfill permits require some kind of monitoring for example [TCEQ Groundwater Detection Monitoring Report Format ](https://www.tceq.texas.gov/downloads/permitting/waste-permits/ihw/docs/gwdm-report-template.pdf)
# >9. **Military Bases.** Military sites are home to some of the most dangerous contaminants, including trichloroethylene (TCE) and per- and poly-fluoroalkyl substances (PFAS). Even today, some US military facilities are plagued by contamination. Worse, some contaminants found in and around those facilities have drifted into some groundwater supplies. TCE is believed to damage the nervous system, lungs, and liver and cause abnormal heartbeat, coma, or even death. It’s also believed to cause cancer in humans. PFAS may lead to problems like thyroid disease, damage to the liver and kidneys, elevated cholesterol, and effects on fertility and low birth weight. And similar to TCE, it is a possible cancer-causing agent.
# >10.  **Atmospheric Contamination.** Ever heard the saying, “What goes up must come down?” Well, that principle also applies to pollutants released into the atmosphere. These contaminants eventually return to Earth in rain, snow, and other forms of precipitation. Surface water then leaches these pollutants into groundwater. Moreover, nitrates and sulfates emitted from power plants and factories can cause acid rain, which streams through the soil and acidifies groundwater supplies.
# 
# A nice [EPA Fact Sheet](https://www.epa.gov/sites/default/files/2015-08/documents/mgwc-gwc1.pdf) discusses sources in some detail.
# 
# A typical priority list (circa 1990s) for the pollutants themselves is:
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
# 2. [Toxicity (Cleveland notes circa 2001)](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/4pollutants/Toxicity.PDF)
# 3. [Dose-Response (Wikipedia)](https://en.wikipedia.org/wiki/Dose%E2%80%93response_relationship)
# 4. [Threshold Concept](https://www.toxmsdt.com/22-dose-response.html)
# 5. [Risk Assessment Concepts (Cleveland notes)](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/4pollutants/CIVE3331_Lecture_018.PDF)
# 5. [Risk Assessment Concepts (TNRCC guidelines)](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/4pollutants/CIVE3331_Readings_018_copy.pdf)
# 5. [Risk Assessment Homework (Old Cleveland notes)](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/4pollutants/Exercise021.PDF)
# 5. [Risk Assessment Solutions (Old Cleveland notes)](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/4pollutants/Solution021.PDF)
