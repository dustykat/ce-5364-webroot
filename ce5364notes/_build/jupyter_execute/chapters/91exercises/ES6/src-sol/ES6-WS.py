#!/usr/bin/env python
# coding: utf-8

# <!--# <font color=darkblue>CE 5364 Groundwater Transport Phenemona <br> Fall 2023 Exercise Set 6</font>-->
# 
# # F23 ES6 Solution Sketch
# 
# **LAST NAME, FIRST NAME**
# 
# **R00000000**
# 
# <hr>
# 
# ## Purpose : 
# Apply selected risk assessment methods
#  
# ## Assessment Criteria : 
# Completion, results plausible, format correct, example calculations shown.  
# 

# <hr>
# 
# ## Problem 1 
# 
# Improper waste disposal practices at an industrial site resulted in contamination of the soil on site by cadmium, a known carcinogen with a slope factor of 6.10 $(\frac{mg}{kg d})^{-1}$. We will consider the risk to off-site residents due to inhalation of airborne soil particles that include the cadmium.  Based on monitoring data, the concentration of cadmium in the air off site is $5.4 \times 10^{-4}~\frac{mg}{m^3}$.
# 
# Determine:
# 
# 1. CInh for residents that are children 1-6 years of age and adults.
# 2. The cancer risk due to these CInh values for the children and adults. 
# 
# Show all calculations and identify all parameter values used.
# 
# 
# 

# In[1]:


# Enter your solution below, or attach separate sheet(s) with your solution.
# Given
CA=5.4e-04 # mg/m^3
SF=6.10 #(mg/kgd)^-1
# use formula for CInh from readings

def CInh(CA,IR,RR,ABSs,ET,EF,ED,BW,AT):
    CInh = (CA*IR*RR*ABSs*ET*EF*ED)/(BW*AT*365)
    return(CInh)

# populate values Child 1-6
IR= 0.25 #m^3/hr
RR=100/100 #x/100% 
ABSs=100/100 #x/100%
ET= 12 #hr/d
EF= 365 #d/yr
ED= 5 #yr
BW= 16 #kg, child
AT= 70 #yr

childCInh=CInh(CA,IR,RR,ABSs,ET,EF,ED,BW,AT)
print("CInh for Child 1-6 y.o.",round(childCInh,9))

# populate values Adult 19-70y.o.
CA=5.4e-04 # mg/m^3
IR= 0.83 #m^3/hr
RR=100/100 #x/100% 
ABSs=100/100 #x/100%
ET= 12 #hr/d
EF= 365 #d/yr
ED= 58 #yr
BW= 70 #kg, adolt
AT= 70 #yr

adoltCInh=CInh(CA,IR,RR,ABSs,ET,EF,ED,BW,AT)
print("CInh for Adolt ",round(adoltCInh,9))

# use formula for CR from readings

def CR(SF,Cinh):
    CR=SF*Cinh
    return(CR)

childCR=CR(SF,childCInh)
adoltCR=CR(SF,adoltCInh)
print("CR for Child ",round(childCR,9))
print("CR for Adolt ",round(adoltCR,9))


# <hr>
# 
# ## Problem 2 
# 
# The same site also caused off-site lead concentrations that can cause non-cancer effects on the residents. The RfD for lead is 6.90x10-4 $(\frac{mg}{kg d})^{-1}$.  We will consider dermal exposures in this problem, with a lead concentration of $260~\frac{mg}{kg}$ in the soil, and an absorption factor of 10 percent for the young children and 5 percent for adults. 
# 
# Determine:
# 
# 1. The NCDEX for residents that are children 1-6 years of age and adults. 
# 2. The hazard quotients due to these NCDEX values for the children and adults.
# 
# Show all calculations and identify all parameter values used. 

# In[2]:


# Enter your solution below, or attach separate sheet(s) with your solution.
# given
RfD = 6.9e-04 #mg/kgd
CS = 260 #mg/kg in soil

# use formula for NCDEX from readings
def NCDEX(CS,CF,SA,AF,ABSs,SM,EF,ED,BW,AT,AvT):
    NCDEX = (CS*CF*SA*AF*AT*ABSs*SM*EF*ED)/(BW*AvT*365)
    return(NCDEX)

# Look up inputs
CF = 1e-06 #kg/mg
SA = 6980 #cm^2/d
AT = 20/100 #%-child
AF = 0.75 #mg/cm^2
ABSs = 10/100 #%-child
SM = 0.15
EF = 330 #d/yr
ED = 5 #yr child
BW = 16 #kg child
AvT = 5 #yr child

childNCDEX= NCDEX(CS,CF,SA,AF,ABSs,SM,EF,ED,BW,AT,AvT)
print("NCEDX child",round(childNCDEX,6))

# repeat fro adult

SA = 18150 #cm^2/d
AT = 10/100 #%-adult
ABSs = 5/100 #%-adult
ED = 58 #yr DULT
BW = 70 #kg adult
AvT = 58 #yr adult

adultNCDEX= NCDEX(CS,CF,SA,AF,ABSs,SM,EF,ED,BW,AT,AvT)
print("NCEDX adolt",round(adultNCDEX,6))

# use hazard quotiet formula

def HQ(E,RfD):
    HQ = E/RfD
    return(HQ)

childHQ = HQ(childNCDEX,RfD)
adultHQ = HQ(adultNCDEX,RfD)

print("HQ child",round(childHQ,3))
print("HQ adult",round(adultHQ,3))


# <hr>
# 
# ## Problem 3 
# 
# A contaminated groundwater that is a potential drinking water source has a manganese concentration of $0.36~\frac{mg}{L}$. The RfD for manganese is $0.10~\frac{mg}{kg \cdot d}$. We will consider effects on children 6-12 (drinking 1 L/d) and adults (2 L/d). 
# 
# Determine:
# 1. The NCIng for children 6-12 and adults drinking this water. 
# 2. The hazard quotients due to these NCIng values for the children and adults. 
# 
# Show all calculations and identify all parameter values used. 

# In[3]:


# Enter your solution below, or attach separate sheet(s) with your solution.
# given
CW = 0.36 #mg/L
RfD = 0.10 #mg/kgd
IRc = 1 #L/d
IRa = 2 #L/d

# use formula for NCing from readings
def NCing(CW,IR,FI,ABSs,EF,ED,BW,AT):
    NCing=(CW*IR*FI*ABSs*EF*ED)/(BW*AT*365)
    return(NCing)

# populate input values
FI = 100/100 #x/100 %
ABSs = 100/100 #x/100 %
EF = 365 #d/yr
EDc = 6 #yr
EDa = 58 #yr
BWc = 29 #kg
BWa = 70 #kg
ATc = 6 #yr
ATa = 58 #yr

childNCing=NCing(CW,IRc,FI,ABSs,EF,EDc,BWc,ATc)
adultNCing=NCing(CW,IRa,FI,ABSs,EF,EDa,BWa,ATa)
childHQ = HQ(childNCing,RfD)
adultHQ = HQ(adultNCing,RfD)

print("NCing child",round(childNCing,6))
print("NCing adolt",round(adultNCing,6))
print("HQ child",round(childHQ,3))
print("HQ adult",round(adultHQ,3))


# <hr>
# 
# ## Problem 4 
# 
# An animal exposure study was performed to determine an acceptable drinking water concentration for a chemical that causes liver disease in rats and is assumed to have a nonzero threshold. The following results were obtained. 
# 
# **Control Group**
# Comparison to historical records: no evidence of premature deaths 
# Time of sacrifice: all surviving rats were sacrificed at 18 months 
# Initial number: 100 
# Number of rats with liver disease: 3 
# 
# **Test Group** 
# Exposure conditions (lowest observed effect): 140 mg/L, 30 mL/d for a median of 12 months 
# Time of sacrifice: all surviving rats were sacrificed at 18 months 
# Comparison of weight and survival curves: no differences between test and control rats 
# Median adult weight: 0.4 kg 
# Initial number exposed: 100 
# Number of rats with liver disease: 12 
# 
# Determine:
# 
# 1. The LOAEL for the rats based on this study.
# 2. The RfD for humans by adjusting for uncertainty. This result is subchronic animal data with no human exposure data available. 
# 3. Convert the RfD to an acceptable drinking water concentration. 
# 
# 

# In[4]:


# Enter your solution below, or attach separate sheet(s) with your solution.

#1.The LOAEL for the rats based on this study:
CW=140 # mg/l
IR=0.030 # L/d
FI=1
ABSs=1
EF=365 # d/yr
ED= 1 # yr
BW=0.4 # kg
AT= 1 # yr
NCIng_Rat=(CW*IR*FI*ABSs*EF*ED)/(BW*AT*365)
print("The LOAEL for the rats = %0.3f mg/(kgd)" %NCIng_Rat) 


# In[5]:


#2.The RfD for humans by adjusting for uncertainty:
UF=10**(4) # UF=10H*10A*10S*10L=10^4
MF=1
RfD=NCIng_Rat/(UF*MF)
print(" RfD for humans by adjusting for uncertainty = %0.7f mg/(kgd)" %RfD)


# In[6]:


#3.Converting the RfD to an acceptable drinking water concentration:
BW=70 # kg
IR=2 # L/d
DWEL=(RfD*BW)/IR
print(" RfD to an acceptable drinking water concentration = %0.7f mg/l" %DWEL)


# <hr>
# 
# ## Problem 5 
# 
# Visit the EPA’s IRIS system website (http://www.epa.gov/iriswebp/iris/index.html)
# 
# Determine:
# 1. Your favorite toxic or carcinogenic substance and print (or screen capture) the Quick View page for your choice.
# 
# 

# In[ ]:




