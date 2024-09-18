#!/usr/bin/env python
# coding: utf-8

# # MODFLOW6 and Python
# 
# In this chapter, we explore the simulation of contaminant transport in groundwater systems using MODFLOW 6 and its Python interface. MODFLOW 6, the industry-standard tool for groundwater modeling, allows for the integration of complex transport processes with hydraulic flow simulations. Through practical examples, we will demonstrate how to model contaminant migration, interface with Python for enhanced data manipulation, and analyze the impact of environmental variables on transport dynamics.
# 
# :::{note}
# Under construction - using a different layout than the rest of the notes.  Some of the generic narrative was written using responses from OpenAI. (2024). ChatGPT (GPT-4). Retrieved [17 SEP 24 ], from [https://chat.openai.com](https://chat.openai.com).
# :::

# :::{admonition} Course Website
# [Link to Course Website](http://54.243.252.9/ce-5364-webroot/)
# :::
# 

# ---
# ## Readings
# 
# 1. [Bear and Cheng](http://54.243.252.9/ce-5364-webroot/3-Readings/BearCheng2010/978-1-4020-6682-5.pdf)
# 
# 2. [Bedient etal.](http://54.243.252.9/ce-5364-webroot/3-Readings/Bedient_et_al/Bedient_et_al._Complete%20reduced.pdf)
# 
# 3. [Bear, J. (1972) *Dynamics of Fluids in Porous Media* McGraw Hill (pp. 628-629)](https://www.amazon.com/Dynamics-Fluids-Porous-Mechanical-Engineering/dp/0486656756)
# 
# 4. [Groundwater Modeling Exercise (used in ModelMUSE video)](http://54.243.252.9/ce-4363-webroot/3-Readings/Groundwater_modelling_exercise.pdf)
# 
# 2. [MODFLOW Notes (Cleveland circa 1992)](http://54.243.252.9/ce-4363-webroot/3-Readings/modflowNotes01.pdf)  The Obleo Aquifer simulation in the MODFLOW88 video is described in these notes.
# 
# 3. [MODFLOW Manual (US EPA)](http://54.243.252.9/ce-4363-webroot/3-Readings/modflmn.pdf) An EPA training document on the use of MODFLOW
# 
# 
# 4. [Zheng, C. and Wang, P.P. (1999) *MT3DMS: A Modular Three-Dimensional Multispecies Transport Model for Simulation of Advection, Dispersion, and Chemical Reactions of Contaminants in Groundwater Systems; Documentation and User's Guide* Strategic Environmental Research and Development Program, Final Report SERDP-99-1](http://54.243.252.9/ce-5364-webroot/3-Readings/MT3DMS/MT3DMS-1999-Report.pdf)
# 
# 5. [Zheng, C. and Bennett, G.D. (1995) *Applied Contaminant Transport Modeling* Van Nostrand Reinhold](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/3advection/Advection.PDF)
# 
# 6. [FloPy: Python Package for Creating, Running, and Post-Processing MODFLOW-Based Models ](https://www.usgs.gov/software/flopy-python-package-creating-running-and-post-processing-modflow-based-models)
# 
# 7. [MT3DMS Problem 9 (On-line documentation for MT3D)](https://modflow6-examples.readthedocs.io/en/master/_notebooks/ex-gwt-mt3dms-p09.html)

# ## Videos
# 
# 

# ## Outline
# - Introduction 
# - Installation and Configuration of MODFLOW 6

# ## Introduction
# 
# ### Overview of MODFLOW 6 and Python's role in contaminant transport modeling.
# 
# MODFLOW 6 is a powerful and flexible software for simulating groundwater flow, supporting modular approaches to incorporate various physical processes, including contaminant transport. When combined with Python, particularly using libraries like flopy, the process of setting up, running, and analyzing MODFLOW models becomes more efficient and customizable. Python’s role extends beyond automation, enabling seamless integration of transport modeling, advanced data handling, and real-time visualization of contaminant movement within groundwater systems.
# 
# ### Importance of Leveraging Python for Automation and Customization in Groundwater Modeling
# 
# Python has become an essential tool in groundwater modeling due to its flexibility, ease of use, and ability to streamline complex workflows. When working with models like MODFLOW 6, creating and managing input files manually can be a tedious and error-prone process, particularly for large or multi-scenario simulations. Python allows us to automate these repetitive tasks efficiently. For instance, using libraries like `flopy`, we can automate the generation, manipulation, and validation of input files, significantly reducing the time required to set up models.
# 
# Beyond automation, Python also enables a high degree of customization. Groundwater models often require unique configurations tailored to specific environmental conditions or project objectives. With Python, we can write custom scripts to modify model parameters, handle boundary conditions dynamically, or integrate external datasets, such as real-time hydrological data or geospatial information. This customization not only saves time but also enhances the accuracy and flexibility of the model, making it easier to adapt to changing project needs.
# 
# Moreover, Python’s vast ecosystem of libraries (like `numpy`, `pandas`, and `matplotlib`) supports advanced data analysis and visualization, allowing engineers and scientists to interpret simulation results more effectively. Instead of manually reviewing raw output files, Python can be used to automate the extraction of key metrics, generate plots, and even create animated visualizations of flow and contaminant transport. This capacity for automation and customization makes Python an invaluable tool for modern groundwater modeling, enabling professionals to focus more on the science and decision-making, rather than the intricacies of file management and data processing.

# ## Installation and Configuration of MODFLOW 6
# 
# <!-- ## MODFLOW 6 and ModelMUSE (a GUI)
# 
# This is a common way to use MODFLOW, with a GUI.  The install is not that hard, but also not point and click.  A video showing an installation is available for viewing at:
# 
# - [Installing ModelMuse and MODFLOW 6 on a local computer](https://www.youtube.com/watch?v=x_D_rvsQ-tI&feature=youtu.be)
# 
# The installation process is:
# 
# 1. GOOGLE "modflow 6"  and/or select: [https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model](https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model) Download the MODFLOW 6 program (choose windows installer)
# 
# 2. GOOGLE "ModelMuse" and/or select: [https://www.usgs.gov/software/modelmuse-a-graphical-user-interface-groundwater-models](https://www.usgs.gov/software/modelmuse-a-graphical-user-interface-groundwater-models)  Download the interface program (installer for 32/64 bit.  When you get a real job, have an IT professional do the install and testing - they can set environment variables in the OS correctly.
# 
# 3. Create C:/WRDAPP folder to house modflow binaries - note the folder attaches at C:/  any other path will probably mess things up later on.
# 
# 4. Install ModelMuse using installer (double click, accept defaults)
# 
# 5. Move the modflow package into C:/WRDAPP folder, extract package, put into folder root.
# 
# 6. Start ModelMuse
#   - create MODFLOW
#   - next
#   - next
#   - Model/MODFLOW Program Locations
#   - set the directory path (may need to edit names a bit)
#   
# 7. Restart ModelMuse and run tutorial.
#   - Pray for smiley faces!
#   - Yay! Install complete. -->
#   
# :::{warning}
# My notes use MODFLOW6 and FloPy to create, run, and interpret simulations.  I can barely get ModelMUSE to work at all, GW Vistas is another option.  If you use Groundwater Vistas, use their tutorials - the key point is MODFLOW 6 is supposed to have a transport model already internalized.  
# :::
# 
# <!-- - Overview of Installation Requirements
# - System requirements for MODFLOW 6 and Python.
# - Key dependencies for different operating systems (Windows, MacOS, and Linux).
# - Installation on Various Architectures
# - Windows and MacOS Installation
#   - Step-by-step installation on Windows and MacOS using pre-compiled binaries.
# - Ubuntu 20+ Linux Installation
#   - Focus on server setup.
#   - Installing MODFLOW 6 and the Python interface using apt-get, conda, or compiling from source.
#   - Troubleshooting common issues on Ubuntu.
# - Configuration and Environment Setup
#   - Setting up the environment for MODFLOW and Python integration.
#   - Installing necessary Python packages (e.g., flopy).
#   - Creating and configuring virtual environments for Python workflows.
#   - Server-side considerations for multi-user or remote-access applications.
# -->

# <!--## Installation and Configuration of MODFLOW 6-->
# A way to access MODFLOW using Python and Jupyter Notebooks is avaliable at 
# 
# [FloPy: Python Package for Creating, Running, and Post-Processing MODFLOW-Based Models ](https://www.usgs.gov/software/flopy-python-package-creating-running-and-post-processing-modflow-based-models)
# 
# The PDF link below shows the installation and an example run on the AWS server.
# 
# [MODFLOW on a Jupyter Server - notes](http://54.243.252.9/ce-4363-webroot/ce4363notes/lessons/groundwatermodels/installing.pdf)
# 
# On my development server which is `aarch64` ARM chipset, I had to compile the modflow binary into a directory, and have chosen to supply explicit paths to the binaries.  Its a clunky approach, but manageable if I port to `amd/intel x86-64` chipset.
# 
# What follows are:
# - Groundwater flow (only) models:
#   1. Steady flow, Single layer aquifer
#   2. Transient flow, Single layer aquifer
#   3. Transient flow, Multiple layer aquifer
# - Groundwater flow and transport model.
#   1. Transient flow, Single layer aquifer, Conservative Tracer (Example 9 MT3DMS)

# In[ ]:




