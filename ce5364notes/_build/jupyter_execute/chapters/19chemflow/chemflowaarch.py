#!/usr/bin/env python
# coding: utf-8

# # ARM7/AARCH Install
# 
# This section shows the install process on an ARM7 device (a Raspberry Pi 4, running Ubuntu OS).  Its mostly here because the server that hosts these Jupyter books is the same Raspberry Pi 
# 
# ## Install the Java Development Kit (JDK) which will be needed by the software; in my case
# 
# `sudo apt install default-jdk` was sufficient (but no telling what I broke to enable the JDK)
# 
# ## Navigate to `CHEMFLO 2000` at the EPA site
# 
# ![](NavigateToCF.png) <br>
# 
# ## Scroll down to the actual program (a .zip archive) and download the file.
# 
# ![](ChooseZip.png) <br>
# 
# ## Upon complete download examine archive contents
# 
# ![](DownloadDone.png)
# 
# ## Extract the archive
# 
# ![](ExtractTheProgram.png)
# 
# In my case I put the program into the directory `/home/sensei/ce-5364-webroot/ce5364notes/chapters/19chemflow/chemflo2000/`
# 

# ## Running the Program
# 
# To run the program, open a desktop (on my server I use XFCE as the desktop, and serve it via TightVNC server)  windows users have desktop manager by default so they can NBR this step.
# 
# ## Starting a vncserver (to get to a GUI)
# 
# ```
# Wed Sep 27 16:52:49 UTC 2023
# sensei@atomickitty:~$ vncserver :1
# 
# New 'X' desktop is atomickitty:1
# 
# Starting applications specified in /home/sensei/.vnc/xstartup
# Log file is /home/sensei/.vnc/atomickitty:1.log
# ```

# ## Starting the program
# 
# Open a terminal window in XFCE navigate to directory where the program is stored.
# 
# ![](XFCEterminal.png) 
# 
# Then launch the program using the command `java -jar chemflow.jar`
# 
# ![](startinXFCE.png)
# 
# A little time elapses then the program loads.
# 
# ![](chemfloOnRASPI.png)

# 

# In[ ]:




