#!/usr/bin/env python
# coding: utf-8

# # ARM7/AARCH 64 Build
# 
# Get source code from
# 
# 1. [MOC for ARM (modified from USGS source)](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/12usgsmocmodel/armmoc/src)
# 2. [MOC Source Code from USGS](https://water.usgs.gov/nrp/gwsoftware/moc/moc.html)
# 
# If you choose the USGS source you will need to make minor modifications to the code to get a compile.
# 
# Put the sources into a location for compiling then run the makefile (below or downloaded)
# 
# ```
# GFORTRAN=gfortran
# FFLAGS=
# PROG=USGSMOC
# VERSION=0.1
# SOURCES=USGSMOC.FOR GENPT.FOR ITERAT.FOR MOVE.FOR PARLOD.FOR UTIL.FOR VELO.FOR
# OBJS=${SOURCES:.f=.o}
# 
# all: USGSMOC
# 
# USGSMOC: ${SOURCES}
# 	${GFORTRAN} ${FFLAGS} -o usgsmoc.exe ${SOURCES}
# 
# dist:
# 	@mkdir ${PROG}-${VERSION}
# 	@cp ${SOURCES} ${PROG}-${VERSION}
# 	@cp Makefile ${PROG}-${VERSION}
# 	@tar cvfz ${PROG}-${VERSION}.tar.gz ${PROG}-${VERSION} 
# 	@rm -rf ${PROG}-${VERSION}
# 
# clean:
# 	@rm -f ${PROG} ${OBJS} core
# ```
# 
# Once the build is complete (no errors; warnings to be expected)
# 
# Move the binary to somewhere meaningful; on my machine the directory structure looks like
# 
# ![](directorysturc.png)
# 
# The executible is located in `bin`
# 
# Next build a supervisory file in a directory with an input file like
# 
# ![](example1.png)
# 
# The contents of the supervisory file `moc01.sup` are literally the input file name, and an output file name.
# 
# ```
# MOC01.INP
# JUNK.OUT
# ```
# 
# The contents of the input file `MOC01.INP` are.
# 
# ```
# Example 1 From Notes -- Zero Dispersion Simulation 
# 1,1,9,9,3200,1,7,1,100,0,9,2,10,1,0,0,0,0   
# 2.0,0.001,0.30,0.0,0.0,0.0,0.0,900.0,900.0,0.30,0.49,1.0
# 5,5                        Observation Well
# 0  0.1                     Transmissivity
# 0  20.0                    Thickness
# 0  0.0                     Recharge
# 1  1.0                     Boundary and I/C array
# 0 0 0 0 0 0 0 0 0              
# 0 0 0 0 0 1 1 1 0 
# 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 
# 0 2 2 2 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 
# 1,1.00,0.00,0.00,0        Leakance terms at special nodes
# 2,1.00,0.00,0.00,0
# 1  100.0       initial head
# 0  0  0  0  0  0  0  0  0
# 0  0  0  0  0  1  1  1  0
# 0  0  0  0  0  0  0  0  0
# 0  0  0  0  0  0  0  0  0
# 0  0  0  0  0  0  0  0  0 
# 0  0  0  0  0  0  0  0  0
# 0  0  0  0  0  0  0  0  0
# 0 .8 .8 .8  0  0  0  0  0
# 0  0  0  0  0  0  0  0  0
# 1  100.0       initial concentration
# 0  0  0  0  0  0  0  0  0
# 0  0  0  0  0  0  0  0  0
# 0  0  0  0  1  1  1  1  0
# 0  0  0  0  0  0  0  0  0
# 0  0  0  0  0  0  0  0  0 
# 0  0  0  0  0  0  0  0  0
# 0  0  0  0  0  0  0  0  0
# 0  0  0  0  0  0  0  0  0
# 0  0  0  0  0  0  0  0  0
# 
# ```
# 
# To run the model, navigate a terminal window to the example directory and execute the model like:
# 
# ![](commandline.png)
# 
# Or (which is way cool) just execute from Jupyter as shown below:
# 
# Get enough of the path

# In[1]:


get_ipython().system(' pwd')


# Copy the application into local directory

# In[2]:


get_ipython().system(' cp ./armmoc/bin/usgsmoc.exe ./')


# Copy the input file and supervisory file, and then run the application

# In[3]:


get_ipython().system(' cp ./armmoc/example1/MOC01.INP ./')
get_ipython().system(' cp ./armmoc/example1/moc01.sup ./')
get_ipython().system(' ./usgsmoc.exe < moc01.sup')


# Display the output (which we will need to postprocess to make pretty pictures).  Generally we can either modify the FORTRAN code to control output, or parse the output file below.  Writing a parser is usually easier, if you are a spreadsheeter, you will grab and plot various arrays from the file below.

# In[4]:


get_ipython().system(' cat JUNK.OUT')


# In[ ]:




