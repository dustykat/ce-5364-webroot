#!/usr/bin/env python
# coding: utf-8

# 

# # Windows Install
# 
# This section shows the install process on a Windows device (an Atomic Pi).  
# 
# ## Install the Java Development Kit (JDK) which will be needed by the software
# 
# The program needs a current JDK installed - its free until 2026.  It was to be free eternally, but the creator [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems) ceased to exist in 2010
# 
# ### Navigate to EPA Webster
# 
# ![](CF2Kpage.png)
# 
# ### Take Link to Java SDK pages
# 
# ![](LinkToJAVA.png)
# 
# ### Navigate to Winders Downloads
# 
# ![](JDK-choices.png)
# 
# Download the SDK, I highlighted bestest choice although the MSI option is fine too.  Then run the executible on your computer; heres my file system
# 
# ![](windozeInstaller.png)
# 
# When you run the installer you get something like
# 
# ![](JDKinstaller.png)
# 
# Just accept defaults and wait it out.
# 
# ### Navigate back to EPA Webster
# 
# Now download the actual software.
# 
# ![](LinkToCF2K.png)
# 
# Download the file (.zip) then extract where you want it to run.
# 
# ![](CF2Kzip.png)
# 
# For example, if extract into Downloads (kind of dumb, but we can move as needed)
# 
# ![](extracted.png)

# ## Running the Program
# 
# To run the program, navigate into the extracted directory and double click the file `CHEMFLO.BAT`.  Wait a short time and you should get the interface.
# 
# ![](CF2KRunning.png)
# 
# 

# ## VNC Demonstration
# 
# On WCOE hardware end users are forbidden to install useful tools; hence here I use a hack to access a remote desktop. The remote desktop is used to access the software remotely. 
# 
# [VNC-Viewer Windoze (portable) 32-bit](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/19chemflow/VNCportable/VNC-Viewer-7.7.0-Windows-32bit.exe)
# 
# [VNC-viewer Winders (portable) 64-bit](http://54.243.252.9/ce-5364-webroot/ce5364notes/chapters/19chemflow/VNCportable/VNC-Viewer-7.7.0-Windows-64bit.exe)
# 
# The actual remote desktop is a Raspberry Pi computer running an XFCE desktop.  Its CHEMFLOW configuration is described in the next section.

# In[ ]:




