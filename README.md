# Deimos Control Center
The GUI and all neccessary code to deliver the functionality of the Control Center

## General Information
As of right now, all code will be written in python and later compiled using pyinstaller to make it run more speedily on the hardware. 
The **Control Center** will be a small, plastic suitcase filled with our necessary hardware including a raspberry pi, on which this code will run, an arduino ( or multiple ) to work with sensors and send information back to the pi for presentation, and any sensors we need.

## The GUI
###### About the Interface
The GUI is being made with the Tkinter python library.
While more advanced GUI libraries were considered, Tkinter was ultimately chosen because it's built-in, easy to use, free, and includes enough to build a beautiful interface. 
There are two main "pages" of the interface: the "Welcome Screen" and the "Main Screen"
The **Welcome Screen** ( referred to in the code as the "Load Screen" ) has no notable functonality other than a button the user clicks to enter the Main Page.
The **Main Screen** displays all important information about the rocket's flight, including a graph of progress, a log of information being sent by the rocket itself, and a log of environment information. Most information still TBD.

###### About the Code
Almost all elements positioned on the screen using tk's **.place()** method because it works similarly to positioning of HTML elements, with which the programmer has significant experience. 
Whenever possible, elements are positioned relatively to their parent, rather than absolutely on the screen. This is to allow the window to resize well ( though the interface is meant to run in full screen and defaults to full screen )
This is not organized into a class as is typically recommended for TK GUIs; I didn't see a real need to do that.
