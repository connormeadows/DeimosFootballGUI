"""

  THE GUI FOR THE ROCKET "FOOTBALL"

  Using tkinter because it's free, built-in, simple, and still powerful enough to make 
  a cool interface. 
  All windows are subject to change as I better learn to what information I will have
  access, how that input will look to me, and how the output needs to look for the team.

  The intent is to compile this using pyinstaller to get that lovely machine-code speed
  and set a raspberry pi (just going to run the raspian OS, there's no need for anything
  else) to load the exe on startup. 

  You'll notice that I almost always use "place" instead of "pack".
  Most of my front-end experience to date is in web development, so "place" feels more
  comfortable to me because it's like absolute positioning of elements.

"""



# Don't ask my why I put the import in an exception handler, Stackoverflow told me to. 
# AFIK lowercase tkinter works on every platform. Oh Well. 
try:
    from tkinter import *
except:
    from Tkinter import *

# Global colors. It's easier to change them once here than in every appearance
backgroundOverall = "grey82"
myRed = "red4"

bigbg = "white"
titlebg = myRed
titlefg = "white"

# Global fonts
titleFont = "Helvetica 100 bold"
subtitleFont = "Arial 30"
frameTitleFont = "Arial 24"

goButtonText = "Launch"

# Going to be some sort of graph related to the rocket's flight
# Will probably be height with respect to time, but can be anything
def graphWindow():
    print("Making the graph portion")

    graphCanvas = Canvas(mainFrame, bg = bigbg, cursor = "cross")

    # Making the axes, they only look correct when the entire window takes the full screen
    xAxis = graphCanvas.create_line((.02 * bigW), (.45 * bigH), (.47 * bigW), (.45 * bigH))
    yAxis = graphCanvas.create_line((.02 * bigW), (.02 * bigH), (.02 * bigW), (.45 * bigH))

    # This is just a forloop to generate a random line. In "production" the graph will
    # be populated with actual data, so this loop will be going through a list of data
    maxHeight = .45 * bigH
    for i in range(2, 35):
        try:
            coord = coord, (i * .01 * bigW), ( maxHeight - i * .01 * bigH)
        except:
            coord = (.02 * bigW), ( maxHeight )
    newPath = graphCanvas.create_line(coord)

    graphCanvas.place(relheight = .48, relwidth = .48, relx = 0.01, rely = 0.01)
    return

# A frame for information about the rocket itself. I do not yet know what information
# the rocket will actually be sending back so I can't really populate this. I'm IMAGINING 
# it could have info like temperature, speed, fuel/power level, etc. 
def rocketInfoWindow():
    print("Making the rocket info window")
    
    infoFrame = Frame(mainFrame, bg = bigbg)
   
    infoTitle = Label(infoFrame, bg = titlebg, fg = titlefg,
                      text = "Rocket Information", font = frameTitleFont)

    infoFrame.place(relheight = .48, relwidth = .48, relx = 0.51, rely = 0.01)
    infoTitle.place(relheight = .1, relwidth = .38, relx = .31, rely = .02)
    return

# Information about relevant environment variables that could affect the rocket's flight
# Currently I have wind, clouds, and precipitation, but this could have whatever info
# is necessary to have available in real time. Nothing in this window matters without 
# sensors and/or internet access.
def environmentWindow():
    print("Making the info window")
    
    enviFrame = Frame(mainFrame, bg = bigbg)

    enviTitle = Label(enviFrame, bg = titlebg, fg = titlefg,
                      text = "Environment Information", font = frameTitleFont)
   
    smallTitleFont = "Arial 15"

    # It doesn't just have to have wind speed, it can also have direction, change, etc. 
    windSpeedFrame = Frame(enviFrame, bd = 4, bg = bigbg)
    windTitle = Label(windSpeedFrame, bg = backgroundOverall,
                      fg = "black", font = smallTitleFont,
                      text = "Wind")

    # As with wind, this can have any useful info about the water in the air that
    # isn't falling. If the water IS falling, then proceed to the next window.
    cloudFrame = Frame(enviFrame, bd = 4, bg = bigbg)
    cloudTitle = Label(cloudFrame, bg = backgroundOverall,
                       fg = "black", font = smallTitleFont, 
                       text = "Clouds")

    # Water is falling, here's how it's doing that. 
    precipFrame = Frame(enviFrame, bd = 4, bg = bigbg)
    precipTitle = Label(precipFrame, bg = backgroundOverall,
                        fg = "black", font = smallTitleFont,
                        text = "Precipitation")

    enviFrame.place(relheight = .48, relwidth = .98, relx = 0.01, rely = 0.51)
    enviTitle.place(relheight = .1, relwidth = .22, relx = 0.39, rely = 0.02)    
    windSpeedFrame.place(relheight = .85, relwidth = .31, relx = .01, rely = .13)
    cloudFrame.place(relheight = .85, relwidth = .31, relx = .345, rely = .13)
    precipFrame.place(relheight = .85, relwidth = .31, relx = .68, rely = .13)
    
    windTitle.place(relheight = .1, relwidth = .96, relx = .02, rely = .02)
    precipTitle.place(relheight = .1, relwidth = .96, relx = .02, rely = .02)
    cloudTitle.place(relheight = .1, relwidth = .96, relx = .02, rely = .02)
    
    return

# The method for the "Launch" button. DOES NOT ACTUALLY LAUNCH THE ROCKET
def startButton():
    loadFrame.pack_forget()
    mainFrame.pack()
    graphWindow()
    rocketInfoWindow()
    environmentWindow()
    return

root = Tk()

outsidePadding = 3
bigW = root.winfo_screenwidth() - outsidePadding
bigH = root.winfo_screenheight() - outsidePadding

# Makes it full screen on startup
root.geometry("{0}x{1}+0+0".format(bigW, bigH))

# loadFrame is what is shown on load. Hints the name.
# mainFrame is what will be seen the rest of the time.
loadFrame = Frame(root, height = bigH, width = bigW, bg = backgroundOverall)
mainFrame = Frame(root, height = bigH, width = bigW, bg = backgroundOverall)
# Not to be confused with the "mainframe" servers  always being
# hacked in movies.

#The content for the loadFrame. The Welcome Screen, if you please
title = Label(loadFrame, text = "DEIMOS", font = titleFont, fg = myRed, bg = backgroundOverall)
title.config(anchor = CENTER)

subtitle = Label(loadFrame, text="The University of Alabama", font=subtitleFont, fg = "white", bg = backgroundOverall)

# The big button on the load screen that you click to go to the mainFrame. 
# Once again, I reiterate, NOT INTENDED TO LAUNCH THE ROCKET
goButton = Button(loadFrame, bg = myRed, fg = "white", text = goButtonText,
                  width = len(goButtonText), padx = 4, justify = CENTER, 
                  font = subtitleFont, activebackground = "white", activeforeground = myRed,
                  command = startButton)

loadFrame.pack()
title.place(relheight = .5, relwidth = .7, relx = .15, rely = .12)
subtitle.place(relheight = .15, relwidth = .7, relx = .15, rely = .45)
goButton.place(relheight = .15, relwidth = .3, relx = .35, rely = .6)

root.mainloop()
