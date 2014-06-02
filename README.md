UVCH264Capture
==============


Linux only.

Dependencies:

- python
- GTK bindings (come with gstreamer bindings)
- gstreamer1.0 bindings

In ubuntu, you can get all these with:

- download anaconda (optional): http://continuum.io/downloads
- download gstreamer (http://askubuntu.com/a/279516):

 sudo add-apt-repository ppa:gstreamer-developers/ppa
 sudo apt-get update
 sudo apt-get install gstreamer1.0*
 
 sudo apt-get install python-gi python3-gi \
    gstreamer1.0-tools \
    gir1.2-gstreamer-1.0 \
    gir1.2-gst-plugins-base-1.0 \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-libav
 
- if anaconda is used, add the system installed python packages to the python path so that they can be imported to ipython. Add the following line to ~.bashrc:

    # added by Anaconda 2.0.0 installer
    export PATH="/home/iha/anaconda/bin:$PATH"
    export PYTHONPATH="/usr/lib/python2.7/dist-packages/:$PYTHONPATH"

