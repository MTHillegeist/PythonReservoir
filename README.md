# PythonReservoir
Simple reservoir simulation with Python (3.8.1) and PyOpenGL. Never finished.

I built this project because I was interested in recreating something like
Schlumberger's ECLIPSE program as a Python application. In ECLIPSE,
you write a single text file with all the information defining the Reservoir
using their manual for the syntax.

This program would have instead been a module the user imports, then fills
in the Reservoir class with their specs in order to build the simulation.

In it's current state, this application is only a basic framework you could
turn into that kind of application. You can define a reservoir dimensions,
specify the saturations, porosity, and pressure of the reservoir cells (this
is done in Main.py currently, but would have been in a file seperate from
the OpenGL code in its final state.) The program displays red or blue (linearly
interpolated) cells depending on the saturation of the blocks. See images for
examples of what this looked like.
