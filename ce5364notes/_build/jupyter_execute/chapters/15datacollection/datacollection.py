#!/usr/bin/env python
# coding: utf-8

# # Data Collection and Analysis
# 
# The textbook (pp. 113-158) has a decent description of how to perform a site investigation.
# 
# A short background follows:
# 

# ## Demonstrating Trend(s) 
# 
# Demonstration of trends will typically employ both plotting (visual cues) and some kind of trend analysis.  The methods suggested in the textbook are variations of non-parametric statistical hypothesis tests.  (pp. 456-462)
# 
# **Mann-Kendall Trend Test** is used to determine whether or not a trend exists in time series (ordered) data. It is a non-parametric test, meaning there is no underlying assumption made about the normality of the data.
# 
# The textbook presents a tabular approach for small data sets as one would expect on a remediation site - here we present a scripting approach using python packages.
# 
# >Mann-Kendall Trend Test using `mk.original_test()` function <br><br>In this approach, the `mk.original_test()` function with required parameters from the **pymannkendall** library to conduct the Mann-Kendall Trend test on the given data in the python programming language. To install the pymannkendall library for mk.original_test() function employ `pip` or `conda` like:<br><br> ::: root@atomickitty:/home/sensei# sudo -H /opt/jupyterhub/bin/python3 -m pip install pymannkendall :::
# 
# An example from [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-perform-a-mann-kendall-trend-test-in-python/) below is used to check the install

# In[1]:


import numpy as np
import pandas as pd
import pymannkendall as mk
import matplotlib.pyplot as plt
import statsmodels.api as sm
get_ipython().run_line_magic('matplotlib', 'inline')
 
gfg_data = [54, 52, 53, 59, 56, 57, 51, 52, 50, 53]

# perform Mann-Kendall Trend Test
result=mk.original_test(gfg_data,alpha=0.1)
print(result.trend)
trend_line = np.arange(len(gfg_data))*result.slope + result.intercept

#data plot 
plt.plot(gfg_data)
plt.plot(trend_line)
plt.ylim(0,100)
# autocorrelation plot
#fig, ax = plt.subplots(figsize=(12, 8))
#sm.graphics.tsa.plot_acf(gfg_data, lags=7, ax=ax);


# Now we have a tool, lets repeat the example on page 461 of the textbook

# In[2]:


import numpy as np
import pandas as pd
import pymannkendall as mk
import matplotlib.pyplot as plt
import statsmodels.api as sm
get_ipython().run_line_magic('matplotlib', 'inline')
gfg_data = [3.18,3.455,3.022,4.876,1.635,2.561,2.329,0.95]
 
# perform Mann-Kendall Trend Test
result=mk.original_test(gfg_data,alpha=0.1)
print("Trend type: ",result.trend)
trend_line = np.arange(len(gfg_data))*result.slope + result.intercept

#data plot 
plt.figure(figsize=(7,7))
plt.plot(gfg_data,marker='o',linewidth=0)
plt.plot(trend_line)
plt.xlabel("Sample Number")
plt.ylabel("Conc. (ppm) ")
plt.ylim(0,5);
# autocorrelation plot
#fig, ax = plt.subplots(figsize=(12, 8))
#sm.graphics.tsa.plot_acf(gfg_data, lags=7, ax=ax);


# ## References
# 
# 1. [U.S. Environmental Protection Agency, National Nonpoint Source Monitoring Program, Tech Notes #6](https://www.epa.gov/sites/default/files/2016-05/documents/tech_notes_6_dec2013_trend.pdf)
# 
# 2. [U.S. Environmental Protection Agency, Office of Solid Waste. (1986) RCRA ground-water monitoring technical enforcement guidance document. OSWER-9950.1](https://www.epa.gov/sites/default/files/documents/rcragwguiddoc-rpt_0.pdf)
# 
# 
# 
# 
