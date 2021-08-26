# simpleCherryPyPage
WARNING

The Alpine-Linux guys are "well known" to fuck-up their system so you end up with a half-cooked OS when it comes to certain libraries !

ALWAY DOUBLE CHECK YOUR LIBRARY VERSIONS !!!

This version of CherryPy (py3-cherrypy) is linked against python3.9 (3.9.6) but only Alpine-Edge (NOT latest !!!) supports it.
If your Docker Container won't run check if the current Python version matches the available modules usually stored in /usr/lib/Python3.X/site-packages 

Once your image has been build, you can run it via:
```docker run -d --rm -p 8080:8080 simpletest ```
