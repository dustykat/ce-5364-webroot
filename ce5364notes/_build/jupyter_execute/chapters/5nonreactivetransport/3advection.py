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
# 1D Examples are in the textbook; 1D is not too difficult as the direction hence the path is known.  
# 
# Higher spatial dimensions (2D, 3D) use either a particle tracking approach (DPRW, MOC, MT3D, ...) or flux-limited Reynolds-averaged Navier-Stokes (FLUENT, SUTRA, HST3D, ....)
# 
# ## Particle Tracking
# Later on we will use USGS-MOC, so will illustrate particle tracking.
# 
# - Particle or front tracking is typically performed using special software.
# - It can be performed using a spreadsheet.
# - The spreadsheet exercise is useful to illustrate the principles involved in particle tracking calculations.
# - Particle tracking with reactions is very computationally intensive and is beyond practical application in a spreadsheet; such computations are used to design space shuttles, helicopters and other things where the knowledge gained justifies the costs
# 
# The first step is to compute the velocity field (if it is steady even better, if not then every time increment it is recomputed)
# 
# - If analytical functions are available for the velocity field then tracking is relatively easy.
# - Usually the velocity field is determined numerically at discrete points in space, and this is the situation of interest.
# - The interpolation schemes in common use are simple; simple, simple-linear, and multi-linear schemes.
# - Only the simple-linear scheme preserves cell-by-cell mass balances.
# 
# The figure below illustrates simple linear interpolation.
# 
# ![](particle_track_interpolation.png)
# 
# - Typical computational grid for heads.
# - Arrows are the interfacial fluxes. 
# - The simple scheme assigns the top and left flux to $(x_1,y_1)$.
# - The simple scheme assgins the right and bottom flux to $(x_2,y_2)$.

# The particle velocity is determined by position of the particle relative to the velocity grid.
# 
# ![](pt_find_particle.png)
# 
# Uses the same grid as the head scheme.
# Velocity is the distance weighted average of the cell that the particle occupies.

# ![](pt_get_velo.png)
# 
# From the above figure, the particle's velocities (x- and y- directions) are:
# 
# - $u_p = \frac{1-\delta x}{\Delta x}u(x_1,y_1)+\frac{\delta x}{\Delta x}u(x_2,y_2)$
# 
# - $v_p = \frac{1-\delta y}{\Delta y}v(x_1,y_1)+\frac{\delta y}{\Delta y}v(x_2,y_2)$

# ### Multi-Linear Interpolation
# 
# Higher order schemes produce smoother velocity fields at the expense of cell mass balances and computational ease. The USGS-MOC model uses a bi-linear scheme where the velocities at the four corners of the occupied cell are used. When transient flow fields occur, averaging in time is also used. The differences in the schemes are hard to detect when the grid spacing is small and the flow field is smoothly varying.

# ### Spreadsheet Approach
# 
# To illustrate particle tracking the simple velocity scheme is used.  
# Extension to higher order schemes is straight forward.
# 
# Illustrate with simple scheme. Consider:
# 
# ![](ss_fig1.png)
# 
# - Large rectangles represent the velocity grid.
# - Circles represent the geometric location where velocity is known.
# - Small rectangle represents the particle that we wish to track.
# 
# **Cell Indexing**
# 
# ![](ss_fig2.png)
# 
# - Each cell represents a grid location in the velocity field.  Thus each cell has a unique row and column index.
# - Each cell centroid also has a unique geomteric (x,y) location.
# - The particle in the figure is located in cell named: Col_1,Row_2.
# - The cell is located at position: (X_1,Y_2).
# - The particle position is (XP,YP).

# **Locating the Particle**
# 
# - At the start of a time-step:
#  - particle position is known.
#  - cell positions are known.
#  - cell that the particle occupies is unknown.
# - Construct a distance table
#  - The distance from each cell to the particle is calculated and stored in a table.
# - Search the table,find the cell nearest the particle.
#  - The cell coordinates of the smallest distance in the table is determined
#  
# **Locating in Excel**
# - The spreadsheet function that finds the value in an array (rectangular area of cells), given the position in the array to search is the function `INDEX(array,row_index,column_index)`
# - The spreadsheet function that can find the position in an array where a particular value appears is the function `MATCH(value,array,type)`
# 
# **INDEX Function**
# - `INDEX(array,row_index,column_index)`
# array is the location of the rectangular area of cells to search (eg. A3:C6).
# row_index is number of rows down from the starting row to search.
# column_index is the number of columns across from the starting column to search.
# 
# **MATCH Function**
# - `MATCH(value,array,type)`
# value is the numerical value to search for in the array.
# array is the location of the rectangular area of cells to search (eg. A3:C6).
# type is the type of match to use.  type=0 means exact matching.
# 
# **Using the Functions**
# - The `INDEX` function allows us to select the correct values of velocity if we know which cell the particle resides in.
# - The `MATCH` function allows us to compare values in an array and determine the position in the array that these values are found.  
# Thus the `MATCH` function lets us search a distance table, find the cell center nearest the particle, and then use the index to find the correct velocity.
# 
# **Moving the Particle**
# 
# Once the cell containing the particle is identified, the particle is assigned the velocity values for that cell.
# The particle is then “moved” by the simple kinematic calculation:
# 
# - $x_p(t+\Delta t)=x_p(t)+u_p(t)\Delta t$
# - $y_p(t+\Delta t)=y_p(t)+v_p(t)\Delta t$

# **Illustrative Example**
# 
# An example with 3 particles is shown below - the spreadsheet is kind of big because iterative computations are intentionally avoided.
# 
# ![](pt_seg0.png)
# 
# Closer view for particle 1:
# 
# ![](pt_seg1.png)
# 
# Closer view for particle 2:
# 
# ![](pt_seg2.png)
# 
# Closer view for particle 3:
# 
# ![](pt_seg3.png)

# **Summary**
# 
# - Particle tracking is a tool to determine the position of a fluid particle in a flow field.
# - A two-step approach is required:
#  - Determine particle velocity
#    - Locate the particle relative to known velocity locations.
#    - Assign the velocity to the particle based on an interpolation scheme.
#  - Move the particle.
# - All particle tracking programs use this type of two-step logic.
# 
# 
# 
# ## Spreadsheets
# 1. [Cleveland, T.G. (1997) *Particle Tracking Spreadsheet (10X10) (Excel)*](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/5nonreactivetransport/PartTrack_10.xls)
# 2. [Cleveland, T.G. (1997) *Particle Tracking Spreadsheet (20X20) (Excel)*](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/5nonreactivetransport/PartTrack_20.xls)
# 3. [Cleveland, T.G. (1997) *Particle Tracking Spreadsheet (5X5 same as example above) (Excel)*](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/5nonreactivetransport/PartTrack.xls)
# 
# Performing the calculations in a python script is illustrated in the next section.
# 
# :::{note}
# You will see that the python script is simpler to construct than the spreadsheet (in terms of weird functions), but takes a shit-ton more code!
# :::

# ## Example of Particle Tracking 
# 
# Here we illustrate using particle tracking to address the problem from the homework.
# 
# <hr><hr>
# 
# ### Problem 2 (Problem 2-8, pg. 578)
# 
# The figure below shows a piezometric map for a shallow sand aquifer.  The hydraulic conductivtiy is estimated to be $1.5 \times 10^{-2}~\frac{cm}{s}$, the saturated thickness is 40 feet, and the effective porosity is 0.3.
# 
# ![](http://54.243.252.9/ce-5364-webroot/2-Exercises/ES1/Fig5.18.png)
# 
# Determine:
# 
# 1. Which well is expected to be the most contaminated.
# 2. The groundwater velocity and seepage velocity across the plume.
# 3. The duration that the source has been contaminating the aquifer (neglect dispersion, diffusiom, and adsorption).
# 4. The flow rate across the plume.
# 5. An explaination for contamination upgradient of the source zone.

# ### Step 1. Need to Digitize the Head Map
# Use [G3DATA](https://alternativeto.net/software/g3data/?platform=windows) or something similar to digitize the head map.
# 
# Using `G3DATA` we will need a coordinate system, so thats superimposed on
# 
# ![](Fig5.18-Coordinates.png)
# 
# Next you need to open an instance of `G3DATA`. If using Windows the system should give you a windows manager, if using linux you need an X-window desktop.
# 
# #### Open G3DATA
# 
# Observe that I get the RandR warning (Resize and rotate) - this is assocated with my VNC server window, and the software still is working.  Given I am running on a Raspberry Pi over the internet, ill live with the warning.
# 
# ![](openG3.png)
# 
# Also notice in the program call the `-scale 0.1` this is a trial-and-error to rescale the image so I can see what I am doing, so open and close a few times until you get the view window into a workable size.
# 
# ![](G3running.png)
# 
# 
# #### Set View == Zoom
# 
# Next we will need to set the view window to Zoom area.  This is needed to write the level set files that we are building.
# 
# ![](viewZoom.png)
# 
# #### Set Filename
# 
# Here we set the file name for each level set.  We will digitize each contour line and save its coordinates to a file, then we conactenate these files after adding the Z coordinate into a single file for gridding and plotting.
# 
# ![](setFileName.png)
# 
# #### Set XY Coordinates
# 
# Here we must set the X and Y coordinates of the lower left,lower right (X) and lower left upper left (Y) to establish how we will be measuring things.
# 
# ![](setXY.png)
# 
# #### Digitize the Contours
# 
# Now we digitize a contour line
# 
# ![](digitizeLS.png)
# 
# when done, we write the points to a file.  Here is what is in the tile.
# 
# ![](LSfile.png)
# 
# Then clear the points (in the G3DATA program), change the file name and digitize the next line. Repeat until all the lines are complete.
# 
# Then open each file and add the Z-coordinate.  Lastly join each file into a single file for further processing.
# 
# Here is what my version looks like, the file is `Fig5.18-LevelSets.png.dat` its an ASCII file that I can read and make a contour plot, but more importantly I can grid the data to estimate x- and y- components of velocity from the given value of hydraulic conductivity.
# 
# ```
# X-Easting	Y-Northing	Z-Elevation
# -0.365791375238  0.00426936718372 5.5
# 7.44799110264  34.0524726574 5.5
# 30.6624750375  65.7872126049 5.5
# ...
# many lines
# ...
# 353.704129652  725.957058705 5.5
# 186.509893725  0.312464310759 5.75
# 195.371098732  37.1933927273 5.75
# 202.181166327  65.9190293167 5.75
# 206.765265923  96.4487403766 5.75
# ...
# many lines
# ...
# 486.889653936  722.268859129 5.75
# 362.749010841  -18.4586090188 6.0
# 367.376818083  9.58126046662 6.0
# ...
# many lines
# ...
# 595.939191403  718.506746134 6.0
# 502.803399911  -17.6039350757 6.25
# 512.271308678  26.3822876764 6.25
# 520.432150683  61.4932965599 6.25
# 525.047470026  90.2445493523 6.25
# ...
# many lines
# ...
# 708.769440297  624.373336948 6.25
# 637.755441575  -17.7565649526 6.50
# 649.674100524  11.6206838032 6.50
# ...
# many lines
# ...
# 885.881149356  618.394355043 6.50
# 901.700715759  -11.9467567219 6.75
# 909.60191353  17.1217634194 6.75
# ...
# many lines
# ...
# 976.769639356  628.357723872 6.75
# ```

# ### Step 2 Check the Digitization Results
# 
# Here we will now produce a contour map from the digitized map, adjust sizes and overlay on the original map to get an idea of how good we did.
# 
# Also will use trial-and-error to find a useable hull within the contour plot where we can capture heads and use for a particle tracking effort - we have to find a rectangle with non-null interpolation values; easiest way (my opinion) is to try indices until can find a reasonable rectangle then sample from that rectangle.  The process is documented below.
# 
# :::{note}
# The interpolation algorithm does not estimate vales outside the convex hull defined by the observation data.  So the box below is by trial-and-error to stay within the convex hull; the interpolator in this region produces useable estimates for computing the heads and velocities from just the mapped information>
# :::

# In[1]:


# CCMR from ENGR-1330:
# http://54.243.252.9/engr-1330-webroot/8-Labs/Lab07/Lab07.html
# https://clouds.eos.ubc.ca/~phil/docs/problem_solving/06-Plotting-with-Matplotlib/06.14-Contour-Plots.html
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.griddata.html
# https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
# https://stackoverflow.com/questions/18730044/converting-two-lists-into-a-matrix
# https://stackoverflow.com/questions/3242382/interpolation-over-an-irregular-grid
# https://stackoverflow.com/questions/33919875/interpolate-irregular-3d-data-from-a-xyz-file-to-a-regular-grid
import pandas
my_xyz = pandas.read_csv('Fig5.18-LevelSets.png.dat',sep='\t') # read an ascii file already prepared, delimiter is tabs
#my_xyz = pandas.read_csv('XYZSomewhereUSA.txt',sep=' ') # read an ascii file already prepared, delimiter is tabs
my_xyz = pandas.DataFrame(my_xyz) # convert into a data frame
#print(my_xyz) #examine the dataframe
import numpy 
import matplotlib.pyplot
from scipy.interpolate import griddata
# extract lists from the dataframe
coord_x = my_xyz['X-Easting'].values.tolist()
coord_y = my_xyz['Y-Northing'].values.tolist()
coord_z = my_xyz['Z-Elevation'].values.tolist()
coord_xy = numpy.column_stack((coord_x, coord_y))
# Set plotting range in original data units
lon = numpy.linspace(min(coord_x), max(coord_x), 100)
lat = numpy.linspace(min(coord_y), max(coord_y), 100)
X, Y = numpy.meshgrid(lon, lat)
# Grid the data; use cubic spline interpolation (other choices are nearest and linear)
Z = griddata(numpy.array(coord_xy), numpy.array(coord_z), (X, Y), method='cubic', fill_value = 'nan')
# Build the map
print("Indices of black box on overlay below:")
ixl = 9
ixh = 90
iyl = 27
iyh = 62
print("xyz lower left corner ",X[iyl][ixl],Y[iyl][ixl],Z[iyl][ixl])
print("xyz lower right corner",X[iyl][ixh],Y[iyl][ixh],Z[iyl][ixh])
print("xyz upper left corner ",X[iyh][ixl],Y[iyh][ixl],Z[iyh][ixl])
print("xyz upper right corner ",X[iyh][ixh],Y[iyh][ixh],Z[iyh][ixh])
xxl = X[iyl][ixl]
xxh = X[iyh][ixh]
yyl = Y[iyl][ixl]
yyh = Y[iyh][ixh]
flag=True
if flag:
    matplotlib.pyplot.rcParams["figure.figsize"] = [10.00, 8.00]
    matplotlib.pyplot.rcParams["figure.autolayout"] = True
    im = matplotlib.pyplot.imread("Fig5.18-Coordinates.png") # base image
fig, ax = matplotlib.pyplot.subplots()
if flag: 
    im = ax.imshow(im, extent=[-25, 1000, -125, 800])# sets X and Y plot window of basemap
#fig.set_size_inches(14, 7)
levels=[5.50,5.75,6.00,6.25,6.50,6.75]
CS = ax.contour(X, Y, Z, levels, linewidths=3)
ax.clabel(CS, inline=2, fontsize=12)
ax.set_title('Contour Plot from Gridded Data File')
ax.set_xlim([0,1000])
ax.set_ylim([0,800])
ax.plot([xxl,xxh],[yyl,yyl],color="black")
ax.plot([xxl,xxh],[yyh,yyh],color="black")
ax.plot([xxl,xxl],[yyl,yyh],color="black")
ax.plot([xxh,xxh],[yyl,yyh],color="black");


# This is acceptable.  Now we will extract velocities from the gridded data files - using the "box".  Recall to use the spreadsheet version of the particle tracker we need the $U$ and $V$ fields from the head distribution.
# 
# We will use the supplied hydraulic conductivity and porosity
# 
# - $K~\approx~ 1.5 \times 10^{-2}~\frac{cm}{s} \cdot \frac{1~in}{2.54~cm} \cdot \frac{1~ft}{12~in} \cdot \frac{86400~s}{1~day} = 42.52~\frac{ft}{day}$
# - $n~\approx~ 0.30 $
# 
# And apply Darcy's law as
# 
# - $\textbf{u(x,y)} = -\frac{K}{n}\cdot \frac{\Delta h}{\Delta x}$
# 
# - $\textbf{v(x,y)} = -\frac{K}{n}\cdot \frac{\Delta h}{\Delta y}$
# 

# In[2]:


Conductivity = 42.52 # feet/day
Porosity = 0.30 # voids/bulk
nrows = iyh - iyl
ncols = ixh - ixl
#Zero vectors for the velocity fields
U = [[0 for j in range(ncols)] for i in range(nrows)]
V = [[0 for j in range(ncols)] for i in range(nrows)]
#Zero vectors for realinged mesh grid
XG = [[0 for j in range(ncols)] for i in range(nrows)]
YG = [[0 for j in range(ncols)] for i in range(nrows)]
for j in range(ncols):
    for i in range(nrows): #range(nrows)
        U[i][j] = -1.0*(Conductivity/Porosity)*(Z[iyl+i][ixl+j]-Z[iyl+i][ixl+j-1])/(X[iyl+i][ixl+j]-X[iyl+i][ixl+j-1]) #- K dh/dx
        V[i][j] = -1.0*(Conductivity/Porosity)*(Z[iyl+i][ixl+j]-Z[iyl+i-1][ixl+j])/(Y[iyl+i][ixl+j]-Y[iyl+i-1][ixl+j]) #- K dh/dy
        XG[i][j] = X[iyl+i][ixl+j]
        YG[i][j] = Y[iyl+i][ixl+j]


# Suppose we want a plot of the vector field just to check our work, a nice tool is `quiver` and/or `streamplot` which are demonstrated below

# In[3]:


# convert to numpy arrays
UU = numpy.asarray(U)
VV = numpy.asarray(V)
XX = numpy.asarray(XG)
YY = numpy.asarray(YG)


# In[4]:


UU[30][30]


# Now a cool "quiver" plot

# In[5]:


if flag:
    matplotlib.pyplot.rcParams["figure.figsize"] = [10.00, 8.00]
    matplotlib.pyplot.rcParams["figure.autolayout"] = True
    im = matplotlib.pyplot.imread("Fig5.18-Coordinates.png") # base image
fig, ax = matplotlib.pyplot.subplots()
if flag: 
    im = ax.imshow(im, extent=[-25, 1000, -125, 800])# sets X and Y plot window of basemap
#fig.set_size_inches(14, 7)
levels=[5.50,5.75,6.00,6.25,6.50,6.75]
CS = ax.quiver(XX[::6, ::6], YY[::6, ::6], UU[::6, ::6], VV[::6, ::6], units='width')
#ax.clabel(CS, inline=2, fontsize=12)
ax.set_title('Vector Plot from Gridded Data File')
ax.set_xlim([0,1000])
ax.set_ylim([0,800]);
ax.plot([xxl,xxh],[yyl,yyl],color="black")
ax.plot([xxl,xxh],[yyh,yyh],color="black")
ax.plot([xxl,xxl],[yyl,yyh],color="black")
ax.plot([xxh,xxh],[yyl,yyh],color="black");

#matplotlib.pyplot.quiver(XX[::6, ::6], YY[::6, ::6], UU[::6, ::6], VV[::6, ::6], units='width')
#matplotlib.pyplot.streamplot(XX, YY, UU, VV, density=0.5, linewidth=2, color=None)


# In[6]:


if flag:
    matplotlib.pyplot.rcParams["figure.figsize"] = [10.00, 8.00]
    matplotlib.pyplot.rcParams["figure.autolayout"] = True
    im = matplotlib.pyplot.imread("Fig5.18-Coordinates.png") # base image
fig, ax = matplotlib.pyplot.subplots()
if flag: 
    im = ax.imshow(im, extent=[0, 1000, -125, 800])# sets X and Y plot window of basemap
#fig.set_size_inches(14, 7)
levels=[5.50,5.75,6.00,6.25,6.50,6.75]
CS = ax.streamplot(XX, YY, UU, VV,  density=0.5, linewidth=1, color=None, arrowsize=3)
#ax.clabel(CS, inline=2, fontsize=12)
ax.set_title('Vector Plot from Gridded Data File')
ax.set_xlim([0,1000])
ax.set_ylim([0,800]);
ax.plot([xxl,xxh],[yyl,yyl],color="black")
ax.plot([xxl,xxh],[yyh,yyh],color="black")
ax.plot([xxl,xxl],[yyl,yyh],color="black")
ax.plot([xxh,xxh],[yyl,yyh],color="black");


# Now we can implement a particle tracking script.  Using the spreadsheet as a guide we can write it in python, and access the cool graphics.  
# 
# Here is the basic script, one simply has to wrap it into a time-stepping loop to produce a trajectory.  Multiple particles can be managed 

# In[7]:


# U array x-velocity at XG,YG
# V array y-velocity at XG,YG
# XG array X-value of cell center
# YG array Y-value of cell center
# XP X-value of particle position 
# YP Y-value of particle position
# UP x-velocity of particle 
# VP y-velocity of particle
# TX x-component particle trajectory
# TY y-component particle trajectory

import math
verbose=False
terse=False
deltaT = 100
etime = 0
numTime = 42
XP = []
YP = []
UP = []
VP = []
TX = [] #trajectory vector
TY = []
np = 1 # Total particles 
XP.append(900)
YP.append(290)
UP.append(0)
VP.append(0)
ip=np-1 
print("                   Initial Particle Position",round(XP[ip],2),round(YP[ip],2),round(UP[ip],2),round(VP[ip],2),round(etime,2))

# move particles this time step
for it in range(numTime):
    for ip in range(np):
    # Build Particle Distance Table
        dist = []
        index = []
        count = 0
        for j in range(ncols):
            for i in range(nrows): #range(nrows)
                dist.append(math.sqrt((XX[i][j]-XP[ip])**2 + (YY[i][j]-YP[ip])**2))
                index.append([count,i,j]) # use to find i,j for a given index
                count = count +1
    # find closest cell
        for i in range(count):
            if dist[i] <= min(dist):
                #print(index[i],dist[i])
                ixx=index[i][1]
                jyy=index[i][2]
    # use nearest cell assignment - aka simple scheme
                UP[ip] = UU[ixx][jyy]
                VP[ip] = VV[ixx][jyy]
                if verbose: print("Particle Position and Velocities Before Move",round(XP[ip],2),round(YP[ip],2),round(UP[ip],2),round(VP[ip],2),round(etime,2))
                break #exits the loop - we stop at the first nearest cell encountered
    # move the particle
        XP[ip]=XP[ip]+UP[ip]*deltaT
        YP[ip]=YP[ip]+VP[ip]*deltaT
        etime=etime+deltaT
        if terse: print(" Particle Position and Velocities After Move",round(XP[ip],2),round(YP[ip],2),round(UP[ip],2),round(VP[ip],2),round(etime,2))
        TX.append([ip,XP[ip],etime])
        TY.append([ip,YP[ip],etime])


# In[8]:


if flag:
    matplotlib.pyplot.rcParams["figure.figsize"] = [10.00, 8.00]
    matplotlib.pyplot.rcParams["figure.autolayout"] = True
    im = matplotlib.pyplot.imread("Fig5.18-Coordinates.png") # base image
fig, ax = matplotlib.pyplot.subplots()
if flag: 
    im = ax.imshow(im, extent=[0, 1000, -125, 800])# sets X and Y plot window of basemap
#fig.set_size_inches(14, 7)
levels=[5.50,5.75,6.00,6.25,6.50,6.75]
CS = ax.streamplot(XX, YY, UU, VV,  density=0.5, linewidth=1, color=None, arrowsize=3)
#ax.clabel(CS, inline=2, fontsize=12)
ax.set_title('Vector Plot from Gridded Data File\n' +            'Each Marker is ' + str(deltaT) + ' days\n' +            'Total Time is ' + str(etime) + ' days')
ax.set_xlim([0,1000])
ax.set_ylim([0,800]);
ax.plot([xxl,xxh],[yyl,yyl],color="black")
ax.plot([xxl,xxh],[yyh,yyh],color="black")
ax.plot([xxl,xxl],[yyl,yyh],color="black")
ax.plot([xxh,xxh],[yyl,yyh],color="black")
xtrajectory = [sublist[1] for sublist in TX]
ytrajectory = [sublist[1] for sublist in TY]
ax.plot(xtrajectory[0],ytrajectory[0],marker="o",color="blue",markersize=24)
ax.plot(xtrajectory,ytrajectory,marker="o",color="red")
("")


# In[9]:


(43/.3)*(1.25/700)


# In[10]:


700/.25


# A useful exercise is to modify the script(s) above for multiple particles to inform the plume age (assuming I have the velocities correctly computed).
# 
# ## Flownets (pp. 30-34)
# 
# A related concept is flownets as outlined in [Cleveland, T.G. (2002) *Flownets* Notes to accompany "CIVE 7332 Flow and Transport Modeling for Environmental Engineering" at University of Houston](http://54.243.252.9/ce-5364-webroot/3-Readings/flownet_1.pdf)
# 
# Numerical generation of flownets can be accomplished using a spreadsheet, python script, or MODFLOW.  
# 
# A simple spreadsheet example is available from
# 
# [Cleveland, T.G. (1997) *Velocity Potential - Stream Function Ideal Flow Model (circa 1999) (Excel)*](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/5nonreactivetransport/VelocityPotential-StreamFunction-FDM.xls)
# 
# ### Theory (in progress)
# 
# A flow net is a coutour plot of $\phi$ and $\Psi$.
# 
# ### Example in Python
# 
# In steady aquifer flow, the flow is irrotational (or at least can be modeled as such). 
# There exists an orthogonal function called the stream function (it is the function that exists in the flow field when vorticity is zero).
# A really good explaination of stream functions (and streamlines) appears on pages 381--398 in Zheng(1995).
# 
# This function can be used to generate plots of streamlines for the same system.
# The principal changes are the material properties representation and the boundary conditions.  

# #### Velocity Potential
# 
# The velocity potential function is usually Darcy's law applied to the head distribution $\phi = \frac{T}{b}h$
# 
# If we start with a steady flow description of GW flow like:
# 
# $$
# 0= 
# \frac{\partial}{\partial x}({\frac{T_x}{b} \frac{\partial h}{\partial x}})
# +
# \frac{\partial}{\partial y}({\frac{T_y}{b} \frac{\partial h}{\partial y}})
# $$
# 
# the terms ${\frac{T_x}{b} \frac{\partial h}{\partial x}}$  and ${\frac{T_y}{b} \frac{\partial h}{\partial y}}$ can be replaced by $\frac{\partial \phi}{\partial x}$ or $\frac{\partial \phi}{\partial y}$ so the expression looks something like
# 
# $$
# 0= 
# \frac{\partial}{\partial x}({ \frac{\partial \phi}{\partial x}})
# +
# \frac{\partial}{\partial y}({ \frac{\partial \phi}{\partial y}})
# $$
# 
# Which is what we would call the velocity potential - although for flow nets we usually just solve for the head so we can compute pressures, using the formulation below:
# 
# $$
# 0= 
# \frac{\partial}{\partial x}({{T_x} \frac{\partial h}{\partial x}})
# +
# \frac{\partial}{\partial y}({{T_y} \frac{\partial h}{\partial y}})
# $$
# 
# The difference equation (pp. 349-357) on a regular grid is
# 
# $$
# \begin{matrix}
# 0= 
# [\frac{1}{\Delta x} T_{x} \frac{h_{i-1,j} - h_{i,j}}{\Delta x} +
#  \frac{1}{\Delta y} T_{y} \frac{h_{i,j-1} - h_{i,j}}{\Delta y}] - \\
# ~~~~~~~~~~\\
# ~~~~~~~~~~[ \frac{1}{\Delta x} T_{x}  \frac{h_{i,j} - h_{i+1,j}}{\Delta x} +
#   \frac{1}{\Delta y}  T_{y} \frac{h_{i,j} - h_{i,j+1}}{\Delta y} ]        
# \end{matrix}        
# $$
# 
# Typically one approximates the spatial variation of the material properties (transmissivity) as arithmetic mean values between two cells, so making the following definitions:
# 
# $$
# \begin{matrix}
# A_{i,j} = \frac{1}{2 \Delta x^2}(T_{x,(i-1,j)}+T_{x,(i,j)}) \\ ~~ \\
# B_{i,j} = \frac{1}{2 \Delta x^2}(T_{x,(i,j)}+T_{x,(i+1,j)})   \\ ~~ \\
# C_{i,j} = \frac{1}{2 \Delta y^2}(T_{y,(i,j-1)}+T_{y,(i,j)})   \\ ~~ \\
# D_{i,j} = \frac{1}{2 \Delta y^2}(T_{y,(i,j)}+T_{y,(i,j+1)})   \\ ~~ \\
# \end{matrix}
# $$
# 
# Substitution into the difference equation yields
# 
# $$
# 0 = A_{i,j}h_{i-1,j} + B_{i,j}h_{i+1,j} - (A_{i,j}+B_{i,j}+C_{i,j}+D_{i,j})h_{i,j} + C_{i,j}h_{i,j-1} + D_{i,j}h_{i,j+1}
# $$
# 
# As before we can explicitly write the cell equation for $h_{i,j}$ as
# 
# $$
# h_{i,j} = \frac{[A_{i,j}h_{i-1,j} + B_{i,j}h_{i+1,j} + C_{i,j}h_{i,j-1} + D_{i,j}h_{i,j+1}]}{[A_{i,j}+B_{i,j}+C_{i,j}+D_{i,j}]}
# $$
# 
# This difference equation represents an approximation to the governing flow equation, the accuracy depending on the cell
# size. Boundary conditions are applied directly into the analogs (another name for the difference equations) at appropriate
# locations on the computational grid. We can generate solutions either by iteration or solving the resulting linear system; iteration is really easy to program, so for exploratory work that's usually the approach.

# #### Stream Function
# 
# The stream function $\Psi$ is a function that is orthogonal to the velocity potential function and expressed as a partial differential equation is
# 
# $$
# 0= 
# \frac{\partial}{\partial x}({\frac{1}{T_y} \frac{\partial \Psi}{\partial x}})
# +
# \frac{\partial}{\partial y}({\frac{1}{T_x} \frac{\partial \Psi}{\partial y}})
# $$
# 
# Observe how the material property is inverted and changes directional identity, otherwise the equation is structurally identical to the groundwater flow equation (for steady flow).
# 
# The difference equation is practically the same as above:
# 
# The difference equation is also almost the same
# 
# $$
# \begin{matrix}
# 0= 
# [\frac{1}{\Delta x} \frac{1}{T_{y}} \frac{\Psi_{i-1,j} - \Psi_{i,j}}{\Delta x} +
#  \frac{1}{\Delta y} \frac{1}{T_{x}} \frac{\Psi_{i,j-1} - \Psi_{i,j}}{\Delta y}] - \\
# ~~~~~~~~~~\\
# ~~~~~~~~~~[ \frac{1}{\Delta x} \frac{1}{T_{y}}  \frac{\Psi_{i,j} - \Psi_{i+1,j}}{\Delta x} +
#   \frac{1}{\Delta y}  \frac{1}{T_{x}} \frac{\Psi_{i,j} - \Psi_{i,j+1}}{\Delta y} ]        
# \end{matrix}        
# $$
# 
# The substitutions are
# 
# $$
# \begin{matrix}
# A_{i,j} = \frac{1}{2 \Delta x^2}(T_{y,(i-1,j)}^{-1}+T_{y,(i,j)}^{-1}) \\ ~~ \\
# B_{i,j} = \frac{1}{2 \Delta x^2}(T_{y,(i,j)}^{-1}+T_{y,(i+1,j)}^{-1})   \\ ~~ \\
# C_{i,j} = \frac{1}{2 \Delta y^2}(T_{x,(i,j-1)}^{-1}+T_{x,(i,j)}^{-1})   \\ ~~ \\
# D_{i,j} = \frac{1}{2 \Delta y^2}(T_{x,(i,j)}^{-1}+T_{x,(i,j+1)}^{-1})   \\ ~~ \\
# \end{matrix}
# $$
# 
# Substitution into the difference equation yields
# 
# $$
# 0 = A_{i,j}\Psi_{i-1,j} + B_{i,j}\Psi_{i+1,j} - (A_{i,j}+B_{i,j}+C_{i,j}+D_{i,j})\Psi_{i,j} + C_{i,j}\Psi_{i,j-1} + D_{i,j}\Psi_{i,j+1}
# $$
# 
# As before we can explicitly write the cell equation for $h_{i,j}$ as
# 
# $$
# \Psi_{i,j} = \frac{[A_{i,j}\Psi_{i-1,j} + B_{i,j}\Psi_{i+1,j} + C_{i,j}\Psi_{i,j-1} + D_{i,j}\Psi_{i,j+1}]}{[A_{i,j}+B_{i,j}+C_{i,j}+D_{i,j}]}
# $$
# 
# So at this point we could literally use the same script, however boundary conditions also ``invert.''
# A no-flow head-domain boundary is a constant value stream function-domain boundary.
# A constant value head-domain boundary is a zero-gradient stream function-domain boundary.

# So a script that first solves for the head distribution, then the stream function could be used to create a flownet. 
# 
# ### Sheetpile under a dam flownet 
# 
# Compare to the example shown on pp. 30-34.
# 
# The figure below is a schematic of a dam built upon a permeable ground layer 80 meters thick (segment A to I).
# 
# ![](sheetpile1.png)
# 
# The dam has a base 60 meters long (segment B to F), with an upstream water depth of 10 meters. The downstream side of the dam is at 0 meters depth (otherwise its not a very good dam!). A sheetpile cutoff wall is installed beneath the dam (segment C to D to U to E). The ground layer has a hydraulic conductivity of K = 1 × 10−4 meters per second.
# 
# Important engineering questions are what is the pore water pressure under the dam, and is what is the total seepage under the dam? The pore water pressure can be found by solving for heads under the dam then subtracting the elevation of the computation location relative to a datum. The flow is found by Darcy’s law applied under the dam (shown as locations 1,2,3,4, and 5 in the sketch), which in turn requires computation of head under the dam. Thus the questions are answered by finding the head distribution under the dam.
# 
# The flow field (mathematically) extends an infinite distance upstream and downstream, but as a practical matter the contribution to seepage far upstream of the dam is negligible, and hence is approximated by the finite domain depicted.
# 
# Using the tools we have already we can simply build an input file, run our script and determine the head distribution (and thus compute the discharges under the dam. Then rerun with same script, but modify the boundary conditions and material properties to obtain the stream function - plot both solutions on the same contour map and viola we have a flownet.
# 
# The first is to represent the domain as shown, and make the following specifications in the boundary condition information, and we will treat the sheetpile cutoff wall as a low permeability inclusion (much like the the prior example). The boundary conditions are:
# 
# 1. The segment from A to B is a constant head boundary with value equal to 10.
# 2. The segment from B to F is a zero-flux boundary.
# 3. The segment from B to C to D to U to E to F should be treated as a zero-flux boundary, but our mask does not extend into the interior – however the sheetpile itself can be approximated by providing a very small permeability. Alternately we could (should) modify the code to handle interior boundaries – but that is outside the scope of this chapter.
# 4. The segment from F to G is a constant head boundary with value equal to 0.
# 5. The segment form G to H is a constant head boundary with value equal to 0.
# 6. The segment from H to I is a zero-flux boundary.
# 7. The segment from I to A is a constant head boundary with value equal to 10.
# 
# Here's the input file for the heads $\phi$ in the picture
# ```
# 10
# 10
# 1
# 9
# 31
# 1e-12
# 5000
# 0 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250 260 270 280 290 300
# 80 70 60 50 40 30 20 10 0
# 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.00010
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0000001 0.0000001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 

# In[11]:


def sse(matrix1,matrix2):
    sse=0.0
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    for ir in range(nr):
        for jc in range(nc):
            sse=sse+(matrix1[ir][jc]-matrix2[ir][jc])**2
    return(sse)

def update(matrix1,matrix2):
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    ##print(nr,nc)
    for ir in range(nr):
        for jc in range(nc):
            ##print(ir,jc)
            matrix2[ir][jc]=matrix1[ir][jc]
    return(matrix2)

def writearray(matrix):
    nr=len(matrix) # get row count
    nc=len(matrix[0]) # get column count
    import numpy as np
    new_list = list(np.around(np.array(matrix), 3))    
    for ir in range(nr):
        print(ir,new_list[ir][:])
    return()

localfile = open("PotentialFnSheetpile1.txt","r") # connect and read file for 2D gw model
deltax = float(localfile.readline())
deltay = float(localfile.readline())
deltaz = float(localfile.readline())
nrows = int(localfile.readline())
ncols = int(localfile.readline())
tolerance = float(localfile.readline())
maxiter = int(localfile.readline())
distancex = [] # empty list
distancex.append([float(n) for n in localfile.readline().strip().split()])
distancey = [] # empty list
distancey.append([float(n) for n in localfile.readline().strip().split()])
boundarytop = [] #empty list
boundarytop.append([float(n) for n in localfile.readline().strip().split()])
boundarybottom = [] #empty list
boundarybottom.append([int(n) for n in localfile.readline().strip().split()])
boundaryleft = [] #empty list
boundaryleft.append([int(n) for n in localfile.readline().strip().split()])
boundaryright = [] #empty list
boundaryright.append([int(n) for n in localfile.readline().strip().split()])
head =[] # empty list
for irow in range(nrows):
        head.append([float(n) for n in localfile.readline().strip().split()])
hydcondx = [] # empty list
for irow in range(nrows):
        hydcondx.append([float(n) for n in localfile.readline().strip().split()])
hydcondy = [] # empty list
for irow in range(nrows):
        hydcondy.append([float(n) for n in localfile.readline().strip().split()])
localfile.close() # Disconnect the file
##
amat = [[0 for j in range(ncols)] for i in range(nrows)]
bmat = [[0 for j in range(ncols)] for i in range(nrows)]
cmat = [[0 for j in range(ncols)] for i in range(nrows)]
dmat = [[0 for j in range(ncols)] for i in range(nrows)]
##
for irow in range(1,nrows-1):
    for jcol in range(1,ncols-1):
        amat[irow][jcol] = (( hydcondx[irow-1][jcol  ]+ hydcondx[irow  ][jcol  ]) * deltaz ) /(2.0*deltax**2)
        bmat[irow][jcol] = (( hydcondx[irow  ][jcol  ]+ hydcondx[irow+1][jcol  ]) * deltaz ) /(2.0*deltax**2)
        cmat[irow][jcol] = (( hydcondy[irow  ][jcol-1]+ hydcondy[irow  ][jcol  ]) * deltaz ) /(2.0*deltay**2)
        dmat[irow][jcol] = (( hydcondy[irow  ][jcol  ]+ hydcondy[irow  ][jcol+1]) * deltaz ) /(2.0*deltay**2)
##
headold = [[0 for jc in range(ncols)] for ir in range(nrows)] #force new matrix
headold = update(head,headold) # update
##writearray(head)
##print("----")
##writearray(headold)
##print("--------")
tolflag = False
for iter in range(maxiter):
##    print("begin iteration")
##    writearray(head)
##    print("----")
##    writearray(headold)
##    print("--------")

# Boundary Conditions

# first and last row special == no flow boundaries
    for jcol in range(ncols):
        if boundarytop[0][jcol] == 0: # no - flow at top
            head [0][jcol ] = head[1][jcol ]
        if boundarybottom[0][ jcol ] == 0: # no - flow at bottom
            head [nrows-1][jcol ] = head[nrows-2][jcol ]
# first and last column special == no flow boundaries     
    for irow in range(nrows): 
        if  boundaryleft[0][ irow ] == 0:
            head[irow][0] = head [irow][1] # no - flow at left
        if boundaryright[0][ irow ] == 0: 
            head [irow][ncols-1] = head[ irow ][ncols-2] # no - flow at right
# interior updates
    for irow in range(1,nrows-1):
        for jcol in range(1,ncols-1):
            head[irow][jcol]=( amat[irow][jcol]*head[irow-1][jcol  ] 
                              +bmat[irow][jcol]*head[irow+1][jcol  ] 
                              +cmat[irow][jcol]*head[irow  ][jcol-1] 
                              +dmat[irow][jcol]*head[irow  ][jcol+1])/(amat[ irow][jcol ]+ bmat[ irow][jcol ]+ cmat[ irow][jcol ]+ dmat[ irow][jcol ])
# test for stopping iterations
##    print("end iteration")
##    writearray(head)
##    print("----")
##    writearray(headold)
    percentdiff = sse(head,headold)
    if  percentdiff <= tolerance:
        print("Exit iterations in velocity potential because tolerance met ")
        print("Iterations =" , iter+1 ) ;
        tolflag = True
        break
    headold = update(head,headold)
print("End Calculations")
print("Iterations    = ",iter+1)
print("Closure Error = ",round(percentdiff,3))
print("Head Map")
print("----")
writearray(head)
print("----")
############# Contour Plot
my_xyz = [] # empty list
for irow in range(nrows):
    for jcol in range(ncols):
        my_xyz.append([distancex[0][jcol],distancey[0][irow],head[irow][jcol]])
import pandas
my_xyz = pandas.DataFrame(my_xyz) # convert into a data frame
#print(my_xyz) # activate to examine the dataframe
import numpy 
import matplotlib.pyplot
from scipy.interpolate import griddata
# extract lists from the dataframe
coord_x = my_xyz[0].values.tolist() # column 0 of dataframe
coord_y = my_xyz[1].values.tolist() # column 1 of dataframe
coord_z = my_xyz[2].values.tolist() # column 2 of dataframe
coord_xy = numpy.column_stack((coord_x, coord_y))
# Set plotting range in original data units
lon = numpy.linspace(min(coord_x), max(coord_x), 3000)
lat = numpy.linspace(min(coord_y), max(coord_y), 800)
X, Y = numpy.meshgrid(lon, lat)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z = griddata(numpy.array(coord_xy), numpy.array(coord_z), (X, Y), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(15, 4)
levels1 = [1,2,3,4,5,6,7,8,9,10]
CS = ax.contour(X, Y, Z, levels1)
ax.clabel(CS, inline=2, fontsize=16)
ax.set_title('Contour Plot of Heads from Sheetpile1 Input')


# Now we reuse the code, but change `head` to `stream` and modify the contour plot variable names as well as modify the input file to reflect the changed material properties and boundary conditions.
# 
# Here's the input file for the stream function
# 
# ```
# 10
# 10
# 1
# 9
# 31
# 1e-12
# 5000
# 0 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250 260 270 280 290 300
# 80 70 60 50 40 30 20 10 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100
# 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 100000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000000 10000000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000 10000
# ```
# 
# In these examples the value of the stream function is arbitrarily set to range from $0$ to $100$.  One useful interpretation of stream function values is that their differences indicate the flow fraction (of total flow) that flows between the streamlines (contour lines of constant stream function value).

# In[12]:


def sse(matrix1,matrix2):
    sse=0.0
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    for ir in range(nr):
        for jc in range(nc):
            sse=sse+(matrix1[ir][jc]-matrix2[ir][jc])**2
    return(sse)

def update(matrix1,matrix2):
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    ##print(nr,nc)
    for ir in range(nr):
        for jc in range(nc):
            ##print(ir,jc)
            matrix2[ir][jc]=matrix1[ir][jc]
    return(matrix2)

def writearray(matrix):
    nr=len(matrix) # get row count
    nc=len(matrix[0]) # get column count
    import numpy as np
    new_list = list(np.around(np.array(matrix), 3))    
    for ir in range(nr):
        print(ir,new_list[ir][:])
    return()

localfile = open("StreamFnSheetpile1.txt","r") # connect and read file for 2D gw model
deltax = float(localfile.readline())
deltay = float(localfile.readline())
deltaz = float(localfile.readline())
nrows = int(localfile.readline())
ncols = int(localfile.readline())
tolerance = float(localfile.readline())
maxiter = int(localfile.readline())
distancex = [] # empty list
distancex.append([float(n) for n in localfile.readline().strip().split()])
distancey = [] # empty list
distancey.append([float(n) for n in localfile.readline().strip().split()])
boundarytop = [] #empty list
boundarytop.append([float(n) for n in localfile.readline().strip().split()])
boundarybottom = [] #empty list
boundarybottom.append([int(n) for n in localfile.readline().strip().split()])
boundaryleft = [] #empty list
boundaryleft.append([int(n) for n in localfile.readline().strip().split()])
boundaryright = [] #empty list
boundaryright.append([int(n) for n in localfile.readline().strip().split()])
stream =[] # empty list
for irow in range(nrows):
        stream.append([float(n) for n in localfile.readline().strip().split()])
hydcondx = [] # empty list
for irow in range(nrows):
        hydcondx.append([float(n) for n in localfile.readline().strip().split()])
hydcondy = [] # empty list
for irow in range(nrows):
        hydcondy.append([float(n) for n in localfile.readline().strip().split()])
localfile.close() # Disconnect the file
##
amat = [[0 for j in range(ncols)] for i in range(nrows)]
bmat = [[0 for j in range(ncols)] for i in range(nrows)]
cmat = [[0 for j in range(ncols)] for i in range(nrows)]
dmat = [[0 for j in range(ncols)] for i in range(nrows)]
##
for irow in range(1,nrows-1):
    for jcol in range(1,ncols-1):
        amat[irow][jcol] = (( hydcondx[irow-1][jcol  ]+ hydcondx[irow  ][jcol  ]) * deltaz ) /(2.0*deltax**2)
        bmat[irow][jcol] = (( hydcondx[irow  ][jcol  ]+ hydcondx[irow+1][jcol  ]) * deltaz ) /(2.0*deltax**2)
        cmat[irow][jcol] = (( hydcondy[irow  ][jcol-1]+ hydcondy[irow  ][jcol  ]) * deltaz ) /(2.0*deltay**2)
        dmat[irow][jcol] = (( hydcondy[irow  ][jcol  ]+ hydcondy[irow  ][jcol+1]) * deltaz ) /(2.0*deltay**2)
##
streamold = [[0 for jc in range(ncols)] for ir in range(nrows)] #force new matrix
streamold = update(stream,streamold) # update
##writearray(stream)
##print("----")
##writearray(streamold)
##print("--------")
tolflag = False
for iter in range(maxiter):
##    print("begin iteration")
##    writearray(stream)
##    print("----")
##    writearray(streamold)
##    print("--------")

# Boundary Conditions

# first and last row special == no flow boundaries
    for jcol in range(ncols):
        if boundarytop[0][jcol] == 0: # no - flow at top
            stream [0][jcol ] = stream[1][jcol ]
        if boundarybottom[0][ jcol ] == 0: # no - flow at bottom
            stream [nrows-1][jcol ] = stream[nrows-2][jcol ]
# first and last column special == no flow boundaries     
    for irow in range(nrows): 
        if  boundaryleft[0][ irow ] == 0:
            stream[irow][0] = stream [irow][1] # no - flow at left
        if boundaryright[0][ irow ] == 0: 
            stream [irow][ncols-1] = stream[ irow ][ncols-2] # no - flow at right
# interior updates
    for irow in range(1,nrows-1):
        for jcol in range(1,ncols-1):
            stream[irow][jcol]=( amat[irow][jcol]*stream[irow-1][jcol  ] 
                              +bmat[irow][jcol]*stream[irow+1][jcol  ] 
                              +cmat[irow][jcol]*stream[irow  ][jcol-1] 
                              +dmat[irow][jcol]*stream[irow  ][jcol+1])/(amat[ irow][jcol ]+ bmat[ irow][jcol ]+ cmat[ irow][jcol ]+ dmat[ irow][jcol ])
# test for stopping iterations
##    print("end iteration")
##    writearray(stream)
##    print("----")
##    writearray(streamold)
    percentdiff = sse(stream,streamold)
    if  percentdiff <= tolerance:
        print("Exit iterations in Stream Function because tolerance met ")
        print("Iterations =" , iter+1 ) ;
        tolflag = True
        break
    streamold = update(stream,streamold)
print("End Calculations")
print("Iterations    = ",iter+1)
print("Closure Error = ",round(percentdiff,3))
print("Stream Function Map")
print("----")
writearray(stream)
print("----")
####################### Contour Plot ###############
my_xyz2 = [] # empty list
for irow in range(nrows):
    for jcol in range(ncols):
        my_xyz2.append([distancex[0][jcol],distancey[0][irow],stream[irow][jcol]])
import pandas
my_xyz2 = pandas.DataFrame(my_xyz2) # convert into a data frame
#print(my_xyz) # activate to examine the dataframe
import numpy 
import matplotlib.pyplot
from scipy.interpolate import griddata
# extract lists from the dataframe
coord_x2 = my_xyz2[0].values.tolist() # column 0 of dataframe
coord_y2 = my_xyz2[1].values.tolist() # column 1 of dataframe
coord_z2 = my_xyz2[2].values.tolist() # column 2 of dataframe
coord_xy2 = numpy.column_stack((coord_x2, coord_y2))
# Set plotting range in original data units
lon = numpy.linspace(min(coord_x2), max(coord_x2), 3000)
lat = numpy.linspace(min(coord_y2), max(coord_y2), 800)
X2, Y2 = numpy.meshgrid(lon, lat)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z2 = griddata(numpy.array(coord_xy2), numpy.array(coord_z2), (X2, Y2), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(15, 4)
levels = [10,20,30,40,50,60,70,80,90,100]
CS2 = ax.contour(X2, Y2, Z2, levels )
ax.clabel(CS2, inline=2, fontsize=16)
ax.set_title('Contour Plot of Stream Function for Sheetpile1 Input')


# Now both plots on same canvass

# In[13]:


# Head (Velocity Potential Map)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z = griddata(numpy.array(coord_xy), numpy.array(coord_z), (X, Y), method='cubic')
Z2 = griddata(numpy.array(coord_xy2), numpy.array(coord_z2), (X2, Y2), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(15, 4)
levels1 = [1,2,3,4,5,6,7,8,9]
CS = ax.contour(X, Y, Z, levels1)
levels2 = [10,20,30,40,50,60,70,80,90]
CS2 = ax.contour(X2, Y2, Z2, levels2 )
ax.clabel(CS, inline=2, fontsize=12)
ax.clabel(CS2, inline=2, fontsize=12)
ax.set_title('Flownet for Sheetpile1 Input')


# <hr>
# <hr>
# 
# ### Flownet Example 2 : Pore Pressure under a Dam (Domain Decomposition approach)
# 
# The second way to solve this example, and perhaps better is to take advantage of
# the symmetry and cut the domain in half, as 
# 
# ![](sheetpile2.png)
# 
# In this method we can actually specify the sheetpile as a boundary, and we will obtain the about same results, but
# only need to supply half as much input data.
# 
# Here's the input file for the half-domain head calculations
# 
# ```
# 10
# 10
# 1
# 9
# 15
# 1e-16
# 5000
# 0 10 20 30 40 50 60 70 80 90 100 110 120 130 140
# 80 70 60 50 40 30 20 10 0
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1
# 0 0 0 0 1 1 1 1 1
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 5
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 5
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 5
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 5
# 10 10 10 10 10 10 10 10 10 10 10 10 10 10 5
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001 0.0001
# ```

# In[14]:


def sse(matrix1,matrix2):
    sse=0.0
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    for ir in range(nr):
        for jc in range(nc):
            sse=sse+(matrix1[ir][jc]-matrix2[ir][jc])**2
    return(sse)

def update(matrix1,matrix2):
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    ##print(nr,nc)
    for ir in range(nr):
        for jc in range(nc):
            ##print(ir,jc)
            matrix2[ir][jc]=matrix1[ir][jc]
    return(matrix2)

def writearray(matrix):
    nr=len(matrix) # get row count
    nc=len(matrix[0]) # get column count
    import numpy as np
    new_list = list(np.around(np.array(matrix), 3))    
    for ir in range(nr):
        print(ir,new_list[ir][:])
    return()

localfile = open("PotentialFnSheetpile2.txt","r") # connect and read file for 2D gw model
deltax = float(localfile.readline())
deltay = float(localfile.readline())
deltaz = float(localfile.readline())
nrows = int(localfile.readline())
ncols = int(localfile.readline())
tolerance = float(localfile.readline())
maxiter = int(localfile.readline())
distancex = [] # empty list
distancex.append([float(n) for n in localfile.readline().strip().split()])
distancey = [] # empty list
distancey.append([float(n) for n in localfile.readline().strip().split()])
boundarytop = [] #empty list
boundarytop.append([float(n) for n in localfile.readline().strip().split()])
boundarybottom = [] #empty list
boundarybottom.append([int(n) for n in localfile.readline().strip().split()])
boundaryleft = [] #empty list
boundaryleft.append([int(n) for n in localfile.readline().strip().split()])
boundaryright = [] #empty list
boundaryright.append([int(n) for n in localfile.readline().strip().split()])
head =[] # empty list
for irow in range(nrows):
        head.append([float(n) for n in localfile.readline().strip().split()])
hydcondx = [] # empty list
for irow in range(nrows):
        hydcondx.append([float(n) for n in localfile.readline().strip().split()])
hydcondy = [] # empty list
for irow in range(nrows):
        hydcondy.append([float(n) for n in localfile.readline().strip().split()])
localfile.close() # Disconnect the file
##
amat = [[0 for j in range(ncols)] for i in range(nrows)]
bmat = [[0 for j in range(ncols)] for i in range(nrows)]
cmat = [[0 for j in range(ncols)] for i in range(nrows)]
dmat = [[0 for j in range(ncols)] for i in range(nrows)]
##
for irow in range(1,nrows-1):
    for jcol in range(1,ncols-1):
        amat[irow][jcol] = (( hydcondx[irow-1][jcol  ]+ hydcondx[irow  ][jcol  ]) * deltaz ) /(2.0*deltax**2)
        bmat[irow][jcol] = (( hydcondx[irow  ][jcol  ]+ hydcondx[irow+1][jcol  ]) * deltaz ) /(2.0*deltax**2)
        cmat[irow][jcol] = (( hydcondy[irow  ][jcol-1]+ hydcondy[irow  ][jcol  ]) * deltaz ) /(2.0*deltay**2)
        dmat[irow][jcol] = (( hydcondy[irow  ][jcol  ]+ hydcondy[irow  ][jcol+1]) * deltaz ) /(2.0*deltay**2)
##
headold = [[0 for jc in range(ncols)] for ir in range(nrows)] #force new matrix
headold = update(head,headold) # update
##writearray(head)
##print("----")
##writearray(headold)
##print("--------")
tolflag = False
for iter in range(maxiter):
##    print("begin iteration")
##    writearray(head)
##    print("----")
##    writearray(headold)
##    print("--------")

# Boundary Conditions

# first and last row special == no flow boundaries
    for jcol in range(ncols):
        if boundarytop[0][jcol] == 0: # no - flow at top
            head [0][jcol ] = head[1][jcol ]
        if boundarybottom[0][ jcol ] == 0: # no - flow at bottom
            head [nrows-1][jcol ] = head[nrows-2][jcol ]
# first and last column special == no flow boundaries     
    for irow in range(nrows): 
        if  boundaryleft[0][ irow ] == 0:
            head[irow][0] = head [irow][1] # no - flow at left
        if boundaryright[0][ irow ] == 0: 
            head [irow][ncols-1] = head[ irow ][ncols-2] # no - flow at right
# interior updates
    for irow in range(1,nrows-1):
        for jcol in range(1,ncols-1):
            head[irow][jcol]=( amat[irow][jcol]*head[irow-1][jcol  ] 
                              +bmat[irow][jcol]*head[irow+1][jcol  ] 
                              +cmat[irow][jcol]*head[irow  ][jcol-1] 
                              +dmat[irow][jcol]*head[irow  ][jcol+1])/(amat[ irow][jcol ]+ bmat[ irow][jcol ]+ cmat[ irow][jcol ]+ dmat[ irow][jcol ])
# test for stopping iterations
##    print("end iteration")
##    writearray(head)
##    print("----")
##    writearray(headold)
    percentdiff = sse(head,headold)
    if  percentdiff <= tolerance:
        print("Exit iterations in velocity potential because tolerance met ")
        print("Iterations =" , iter+1 ) ;
        tolflag = True
        break
    headold = update(head,headold)
print("End Calculations")
print("Iterations    = ",iter+1)
print("Closure Error = ",round(percentdiff,3))
print("Head Map")
print("----")
writearray(head)
print("----")
############# Contour Plot
my_xyz = [] # empty list
for irow in range(nrows):
    for jcol in range(ncols):
        my_xyz.append([distancex[0][jcol],distancey[0][irow],head[irow][jcol]])
import pandas
my_xyz = pandas.DataFrame(my_xyz) # convert into a data frame
#print(my_xyz) # activate to examine the dataframe
import numpy 
import matplotlib.pyplot
from scipy.interpolate import griddata
# extract lists from the dataframe
coord_x = my_xyz[0].values.tolist() # column 0 of dataframe
coord_y = my_xyz[1].values.tolist() # column 1 of dataframe
coord_z = my_xyz[2].values.tolist() # column 2 of dataframe
coord_xy = numpy.column_stack((coord_x, coord_y))
# Set plotting range in original data units
lon = numpy.linspace(min(coord_x), max(coord_x), 3000)
lat = numpy.linspace(min(coord_y), max(coord_y), 800)
X, Y = numpy.meshgrid(lon, lat)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z = griddata(numpy.array(coord_xy), numpy.array(coord_z), (X, Y), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(7.5, 4)
levels1 = [1,2,3,4,5,6,7,8,9,10]
CS = ax.contour(X, Y, Z, levels1)
ax.clabel(CS, inline=2, fontsize=16)
ax.set_title('Contour Plot of Heads from Sheetpile2 Input')


# :::{note}
# If you have to do this a lot, you could automate the "file rewrite" and have the program run the two instances back to back then make the contour plots
# :::
# 
# Here's the input file for the domain decomposition stream function calculations
# 
# ```
# 10
# 10
# 1
# 9
# 15
# 1e-16
# 5000
# 0 10 20 30 40 50 60 70 80 90 100 110 120 130 140
# 80 70 60 50 40 30 20 10 0
# 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 0 0 0 0 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 5 5 5 5 5 5 5 5 5 5 5 5 5 0
# 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
# ```

# In[15]:


def sse(matrix1,matrix2):
    sse=0.0
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    for ir in range(nr):
        for jc in range(nc):
            sse=sse+(matrix1[ir][jc]-matrix2[ir][jc])**2
    return(sse)

def update(matrix1,matrix2):
    nr=len(matrix1) # get row count
    nc=len(matrix1[0]) # get column count
    ##print(nr,nc)
    for ir in range(nr):
        for jc in range(nc):
            ##print(ir,jc)
            matrix2[ir][jc]=matrix1[ir][jc]
    return(matrix2)

def writearray(matrix):
    nr=len(matrix) # get row count
    nc=len(matrix[0]) # get column count
    import numpy as np
    new_list = list(np.around(np.array(matrix), 3))    
    for ir in range(nr):
        print(ir,new_list[ir][:])
    return()

localfile = open("StreamFnSheetpile2.txt","r") # connect and read file for 2D gw model
deltax = float(localfile.readline())
deltay = float(localfile.readline())
deltaz = float(localfile.readline())
nrows = int(localfile.readline())
ncols = int(localfile.readline())
tolerance = float(localfile.readline())
maxiter = int(localfile.readline())
distancex = [] # empty list
distancex.append([float(n) for n in localfile.readline().strip().split()])
distancey = [] # empty list
distancey.append([float(n) for n in localfile.readline().strip().split()])
boundarytop = [] #empty list
boundarytop.append([float(n) for n in localfile.readline().strip().split()])
boundarybottom = [] #empty list
boundarybottom.append([int(n) for n in localfile.readline().strip().split()])
boundaryleft = [] #empty list
boundaryleft.append([int(n) for n in localfile.readline().strip().split()])
boundaryright = [] #empty list
boundaryright.append([int(n) for n in localfile.readline().strip().split()])
stream =[] # empty list
for irow in range(nrows):
        stream.append([float(n) for n in localfile.readline().strip().split()])
hydcondx = [] # empty list
for irow in range(nrows):
        hydcondx.append([float(n) for n in localfile.readline().strip().split()])
hydcondy = [] # empty list
for irow in range(nrows):
        hydcondy.append([float(n) for n in localfile.readline().strip().split()])
localfile.close() # Disconnect the file
##
amat = [[0 for j in range(ncols)] for i in range(nrows)]
bmat = [[0 for j in range(ncols)] for i in range(nrows)]
cmat = [[0 for j in range(ncols)] for i in range(nrows)]
dmat = [[0 for j in range(ncols)] for i in range(nrows)]
##
for irow in range(1,nrows-1):
    for jcol in range(1,ncols-1):
        amat[irow][jcol] = (( hydcondx[irow-1][jcol  ]+ hydcondx[irow  ][jcol  ]) * deltaz ) /(2.0*deltax**2)
        bmat[irow][jcol] = (( hydcondx[irow  ][jcol  ]+ hydcondx[irow+1][jcol  ]) * deltaz ) /(2.0*deltax**2)
        cmat[irow][jcol] = (( hydcondy[irow  ][jcol-1]+ hydcondy[irow  ][jcol  ]) * deltaz ) /(2.0*deltay**2)
        dmat[irow][jcol] = (( hydcondy[irow  ][jcol  ]+ hydcondy[irow  ][jcol+1]) * deltaz ) /(2.0*deltay**2)
##
streamold = [[0 for jc in range(ncols)] for ir in range(nrows)] #force new matrix
streamold = update(stream,streamold) # update
##writearray(stream)
##print("----")
##writearray(streamold)
##print("--------")
tolflag = False
for iter in range(maxiter):
##    print("begin iteration")
##    writearray(stream)
##    print("----")
##    writearray(streamold)
##    print("--------")

# Boundary Conditions

# first and last row special == no flow boundaries
    for jcol in range(ncols):
        if boundarytop[0][jcol] == 0: # no - flow at top
            stream [0][jcol ] = stream[1][jcol ]
        if boundarybottom[0][ jcol ] == 0: # no - flow at bottom
            stream [nrows-1][jcol ] = stream[nrows-2][jcol ]
# first and last column special == no flow boundaries     
    for irow in range(nrows): 
        if  boundaryleft[0][ irow ] == 0:
            stream[irow][0] = stream [irow][1] # no - flow at left
        if boundaryright[0][ irow ] == 0: 
            stream [irow][ncols-1] = stream[ irow ][ncols-2] # no - flow at right
# interior updates
    for irow in range(1,nrows-1):
        for jcol in range(1,ncols-1):
            stream[irow][jcol]=( amat[irow][jcol]*stream[irow-1][jcol  ] 
                              +bmat[irow][jcol]*stream[irow+1][jcol  ] 
                              +cmat[irow][jcol]*stream[irow  ][jcol-1] 
                              +dmat[irow][jcol]*stream[irow  ][jcol+1])/(amat[ irow][jcol ]+ bmat[ irow][jcol ]+ cmat[ irow][jcol ]+ dmat[ irow][jcol ])
# test for stopping iterations
##    print("end iteration")
##    writearray(stream)
##    print("----")
##    writearray(streamold)
    percentdiff = sse(stream,streamold)
    if  percentdiff <= tolerance:
        print("Exit iterations in Stream Function because tolerance met ")
        print("Iterations =" , iter+1 ) ;
        tolflag = True
        break
    streamold = update(stream,streamold)
print("End Calculations")
print("Iterations    = ",iter+1)
print("Closure Error = ",round(percentdiff,3))
print("Stream Function Map")
print("----")
writearray(stream)
print("----")
####################### Contour Plot ###############
my_xyz2 = [] # empty list
for irow in range(nrows):
    for jcol in range(ncols):
        my_xyz2.append([distancex[0][jcol],distancey[0][irow],stream[irow][jcol]])
import pandas
my_xyz2 = pandas.DataFrame(my_xyz2) # convert into a data frame
#print(my_xyz) # activate to examine the dataframe
import numpy 
import matplotlib.pyplot
from scipy.interpolate import griddata
# extract lists from the dataframe
coord_x2 = my_xyz2[0].values.tolist() # column 0 of dataframe
coord_y2 = my_xyz2[1].values.tolist() # column 1 of dataframe
coord_z2 = my_xyz2[2].values.tolist() # column 2 of dataframe
coord_xy2 = numpy.column_stack((coord_x2, coord_y2))
# Set plotting range in original data units
lon = numpy.linspace(min(coord_x2), max(coord_x2), 3000)
lat = numpy.linspace(min(coord_y2), max(coord_y2), 800)
X2, Y2 = numpy.meshgrid(lon, lat)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z2 = griddata(numpy.array(coord_xy2), numpy.array(coord_z2), (X2, Y2), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(7.5, 4)
levels = [5,20,30,40,50,60,70,80,90,100]
CS2 = ax.contour(X2, Y2, Z2, levels )
ax.clabel(CS2, inline=2, fontsize=16)
ax.set_title('Contour Plot of Stream Function for Sheetpile2 Input')


# Now try both contour plot same plot canvas

# In[16]:


# Head (Velocity Potential Map)
# Grid the data; use linear interpolation (choices are nearest, linear, cubic)
Z = griddata(numpy.array(coord_xy), numpy.array(coord_z), (X, Y), method='cubic')
Z2 = griddata(numpy.array(coord_xy2), numpy.array(coord_z2), (X2, Y2), method='cubic')
# Build the map
fig, ax = matplotlib.pyplot.subplots()
fig.set_size_inches(7.5, 4)
levels1 = [5,6,7,8,9,10]
CS = ax.contour(X, Y, Z, levels1)
levels2 = [10,20,30,40,50,60,70,80,90,100]
CS2 = ax.contour(X2, Y2, Z2, levels2 )
ax.clabel(CS, inline=2, fontsize=16)
ax.clabel(CS2, inline=2, fontsize=12)
ax.set_title('Flownet for Sheetpile2 Input')


# In[ ]:





# ## References
# 
# 1. [Zheng, C. and Bennett, G.D. (1995) pp. 3-23 *Applied Contaminant Transport Modeling* Van Nostrand Reinhold](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/3advection/Advection.PDF)
# 2. [Cleveland, T.G. (2002) *Advection* Notes to accompany *"CIVE 7332 Flow and Transport Modeling for Environmental Engineering" at University of Houston*](http://54.243.252.9/ce-5364-webroot/3-Readings/AdvectionNotes.pdf)
# 3. [Cleveland, T.G. (2002) *Particle Tracking in a Spreadsheet* Notes to accompany "CIVE 7332 Flow and Transport Modeling for Environmental Engineering" at University of Houston](http://54.243.252.9/ce-5364-webroot/3-Readings/parttrack_1.pdf)
