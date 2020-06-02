try:
    from tkinter import *
except:
    from Tkinter import *

backgroundOverall = "grey82"
myRed = "red4"

titleFont = "Helvetica 100 bold"
subtitleFont = "Arial 30"

goButtonText = "Launch"

def graphWindow():
    print("Making the graph portion")

    graphCanvas = Canvas(mainFrame, bg="white", cursor = "cross")

    # Making the axes
    xAxis = graphCanvas.create_line((.02 * bigW), (.45 * bigH), (.47 * bigW), (.45 * bigH))
    yAxis = graphCanvas.create_line((.02 * bigW), (.02 * bigH), (.02 * bigW), (.45 * bigH))

    maxHeight = .45 * bigH
    for i in range(2, 35):
        try:
            coord = coord, (i * .01 * bigW), ( maxHeight - i * .01 * bigH)
        except:
            coord = (.02 * bigW), ( maxHeight )
    newPath = graphCanvas.create_line(coord)

    graphCanvas.place(relheight = .49, relwidth = .49, relx = 0.01, rely = 0.01)
    return

def rocketInfoWindow():
    print("Making the rocket info window")
    return

def environmentWindow():
    print("Making the info window")
    return

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

root.geometry("{0}x{1}+0+0".format(bigW, bigH))


# loadFrame = Frame(root, height = 600, width = 1000, bg = backgroundOverall)
loadFrame = Frame(root, height = bigH, width = bigW, bg = backgroundOverall)
mainFrame = Frame(root, height = bigH, width = bigW, bg = backgroundOverall)

title = Label(loadFrame, text = "DEIMOS", font = titleFont, fg = myRed, bg = backgroundOverall)
title.config(anchor = CENTER)

subtitle = Label(loadFrame, text="The University of Alabama", font=subtitleFont, fg = "white", bg = backgroundOverall)

# DOES NOT ACTUALLY LAUNCH THE ROCKET. ONLY LAUNCHES THE FOOTBALL INTERFACE.
goButton = Button(loadFrame, bg = myRed, fg = "white", text = goButtonText,
                  width = len(goButtonText), padx = 4, justify = CENTER, 
                  font = subtitleFont, activebackground = "white", activeforeground = myRed,
                  command = startButton)

loadFrame.pack()
title.place(relheight = .5, relwidth = .7, relx = .15, rely = .12)
subtitle.place(relheight = .15, relwidth = .7, relx = .15, rely = .45)
goButton.place(relheight = .15, relwidth = .3, relx = .35, rely = .6)

root.mainloop()