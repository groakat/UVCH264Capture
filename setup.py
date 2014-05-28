import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "UVCH264Capture",
    version = "0.1.0",
    author = "Peter Rennert",
    author_email = "p.rennert@cs.ucl.ac.uk",
    description = ("Python script based on Gstreamer 1 to record H264 encoded video from webcams."),
    packages=find_packages(),
    #license = read('LICENSE.txt'),
    keywords = "video recording",
    url = "https://github.com/groakat/UVCH264Capture",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
    ],
)