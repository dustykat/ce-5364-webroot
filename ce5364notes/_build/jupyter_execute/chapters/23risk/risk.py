#!/usr/bin/env python
# coding: utf-8

# # Risk Assessment
# 
# Risk = (Likliehood of outcome) $\times$ (Consequence)
# 
# If we observe or predict a concentration at a point in an aquifer how bad is it? Do we have to clean it up to **zero**?
# 
# Usually cannot afford to! So we assess risk to establish a technologically achievable target.
# 
# The concept of a technology-based target is incorporated into the [Clean Air Act](https://www.epa.gov/clean-air-act-overview/setting-emissions-standards-based-technology-performance) and under the Clean Wasser Act, under Sections 301, 302, 304, and 306, the EPA issues [technology-based effluent guidelines](https://www.ecfr.gov/current/title-40/chapter-I/subchapter-D/part-125) that establish discharge standards based on treatment technologies that are available and economically achievable. Each EPA Region issues permits that meet or exceed the guidelines and standards.
# 
# A similar concept applies in groundwater contaminantion and restoration.  All these concept rely on risk as the arbiter of target values.
# 
# :::{note}
# Here is an interesting review of [risks of technology-based standards](https://scholarship.law.duke.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1096&context=delpf); its written from a litigation lawyer point of view - but nonetheless interesting!  A similar law article is [The Triumph of Technology-Based Standards](https://heinonline.org/HOL/Page?handle=hein.journals/unilllr2000&div=11&g_sent=1&casa_token=&collection=journals)
# :::
# 
# 

# ![](hazard2risk.png)

# ## Hazard ID
# 
# - Sample collection & analytical data
#  - presence/absence; locations
#  - non-detects: how are these included in statistics?<br> < DL, or <PQL, or 1/2 DL, or zero? <br> A whole science of censored data is needed to be considered.

# ## Exposure Assessment
# - Pathways: inhale, ingest, absorb (through skin)
# - Medium: Air, water, soil
# - Receptor: Worker, resident, adult (70kg), child (16kg), infant (3kg)
# - Exposure:  
# 
# $EXP\frac{mg}{kg \cdot d} = IF(\frac{amount of medium}{d})\times C(\frac{mg}{medium}) \times EDF \times CF$ <br>  IF == intake factor; EDF == exposure duration factor; CF == conversion factor <br> concentrations are compared to MCLs if available <br> derived from animal or human exposure
# 
# [Asante-Duah, K. (1993) Hazardous Waste Risk Assessment](http://54.243.252.9/ce-5364-webroot/3-Readings/HazardousWasteRiskAssessmentbyAsante-Duah.pdf)
# 
# ![](intakedose.png)

# General AT guidelines:
# 
# Carcinogen: AT == Lifetime (70 $\times$ 365 days)<br>
# Non-Carcinogen: AT == Approximate exposure time
# 
# Long-term: 
# - CDI == chronic daily intake over 70 years<br>
# - C == reasonably maximum exposure (time)
# 
# Short-term:
# - SDI == subchronic daily intake
# 
# LADD == lifetime average daily dose (cancer) <br>
# ADD ==  average daily dose (non-cancer)<br>
# MDD = maximum daily dose (short-term acute)<br>
#             

# ## Toxicity Assessment
# 
# Type of adverse effects.  Relates exposure magnitude to amount of effect.
# 
# An example:
# 
# Total body exposure of 100 roentgens/rad or 1 Gray unit (Gy) causes radiation sickness. Total body exposure of 400 roentgens/rad (or 4 Gy) causes radiation sickness and death in half of the individuals who are exposed.
# 
# :::{note}
# There is a missing component above - 4 Gy kills 1/2 exposed in some prescribed time interval (I recall its 30 days).  This whole concept of LD50 implicitly includes some response time window.  
# :::
# 
# [Radiation health effects](https://www.epa.gov/radiation/radiation-health-effects) are phenomenally well studied and much toxicity understanding is directly sourced from radition behavoir.  
# 
# **Data Sources**
# - [US EPA IRIS](https://www.epa.gov/iris) 
# Has browsable database for example part of [Agent Orange](https://iris.epa.gov/ChemicalLanding/&substance_nmbr=150)
# - Scientific literature
# - Health literature [VA Agent Orange](https://www.publichealth.va.gov/exposures/agentorange/#:~:text=Agent%20Orange%20was%20a%20tactical,herbicides%20during%20the%20Vietnam%20War.)
# - Conspiracy literature (probably less reliable) [YouTube Agent Orange](https://www.youtube.com/watch?v=BHcd-srsSBY)
# 
# 
# All based to some extent on:
# - Case clusters
# - [Theoretical toxicology](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5837539/)
# - Short-term laboratory studies
# - [Long-term animal model studies](https://www.sciencedirect.com/science/article/pii/S2452302X1930316X)
# - [Human (epidemiological) studies](https://www.ncbi.nlm.nih.gov/books/NBK219116/)
# - [Unethical human experiments](https://en.wikipedia.org/wiki/Unethical_human_experimentation) ![](wasteOfFood.png) Although wrong, should we use the data? 

# ## References
# 
# 1. [Asante-Duah, K. (1993) Hazardous Waste Risk Assessment](http://54.243.252.9/ce-5364-webroot/3-Readings/HazardousWasteRiskAssessmentbyAsante-Duah.pdf)
# 2. [Hazard Ranking System Guidance Manual](http://54.243.252.9/ce-5364-webroot/3-Readings/HRSmanual.pdf)
# 3. [EPA Risk Communication Seminar (1990)](http://54.243.252.9/ce-5364-webroot/3-Readings/EPARiskCommunicationSeminar.pdf)

# In[ ]:





# In[ ]:




