from cmu_112_graphics import *
from objectClass import *
from tkinter import *

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

class dustGame(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50

def rgbString(red, green, blue):
    # Don't worry about how this code works yet.
    return "#%02x%02x%02x" % (red, green, blue)

import random
class GameMode(Mode):
    def appStarted(mode):
        mode.ants = []
        mode.time = 0
        mode.dirt = 32

    def addAnt(mode,x,y):
        x,y = x-16,y-16
        x= roundHalfUp(x/32)*32
        y= roundHalfUp(y/32)*32
        x,y = x+16,y+16
        if y < mode.dirt:
            mode.ants.append(Ant(mode,x,y))

    def mousePressed(mode,event):
        mode.addAnt(event.x,event.y)

    def timerFired(mode):
        mode.time += 1
        #for ant in mode.ants:
            #ant.move()
    
    def redrawAll(mode,canvas):
        #drawCanvas()
        canvas.create_rectangle(0,0,mode.app.width,mode.app.height,
                            fill="blue")
        canvas.create_rectangle(0,mode.dirt,
                mode.app.width,mode.app.height,fill=rgbString(155,118,83))
        
        for ant in mode.ants:
            ant.draw(canvas)
        

class SplashScreenMode(Mode):
    def keyPressed(mode, event):
        #checks if help keys are inputted but otherwise 
        #plays the game if any key is pressed
        #if event.key == "S":
            #superHelp()
        #elif event.key == "h":
            #mode.app.setActiveMode(mode.app.helpMode)
        mode.app.setActiveMode(mode.app.gameMode)

    def redrawAll(mode,canvas):
        #Tells the player to press a key to start the game or
        #press h for help
        canvas.create_rectangle(0,0,mode.app.width,mode.app.height,
                            fill="black")
        canvas.create_text(mode.app.width/2,mode.app.height/2,
                            text="(maximize screen pls)", 
                            font = ('Comic Sans MS',30,'bold italic underline'),
                            fill = "Yellow", anchor = "n")
        canvas.create_text(mode.app.width/2,mode.app.height/2,
                            text="Press any key to start!", 
                            font = "Arial 20 bold",
                            fill = "White", anchor = "s")
        '''
        canvas.create_text(mode.app.width/2,mode.app.height/2,
                            text="Press h for help!", 
                            font = "Arial 20 bold",
                            fill = "White", anchor = "n")
        '''

class HelpMode(Mode):
    pass

def runWolfePack():
    dustGame(width=600,height=600)

def main():
    runWolfePack()

if __name__ == '__main__':
    main()
