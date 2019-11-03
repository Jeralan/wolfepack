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
import winsound
class GameMode(Mode):
    def appStarted(mode):
        spriteSheet = mode.app.loadImage('antSprites.png')
        spriteSheet = mode.app.scaleImage(spriteSheet, 1/2)
        mode.sprites = []
        for i in range(4):
            dirSprites = []
            for j in range(4):
                sprite = spriteSheet.crop((32 * j, 32 * i,
                                           32 * (j + 1), 32 * (i + 1)))
                dirSprites.append(ImageTk.PhotoImage(sprite))
            mode.sprites.append(dirSprites)


        winsound.PlaySound("cmupie.wav",winsound.SND_ASYNC)
        mode.burrows = [([False]*(mode.app.height//32)) for r in range(mode.app.width//32)]
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

    def keyPressed(mode,event):
        for ant in mode.ants:
            if event.key == 'Up':
                ant.dir = 0
                ant.dx, ant.dy = 0, -1
            elif event.key == 'Right':
                ant.dir = 1
                ant.dx, ant.dy = +1, 0
            elif event.key == 'Down':
                ant.dir = 2
                ant.dx, ant.dy = 0, +1
            elif event.key == 'Left':
                ant.dir = 3
                ant.dx, ant.dy = -1, 0

    def timerFired(mode):
        mode.antCount = 0
        while mode.antCount < len(mode.ants):
            mode.ants[mode.antCount].move(mode)
            if (mode.time - mode.ants[mode.antCount].id) % 32 == 0:
                mode.ants[mode.antCount].changeDir(mode)
                mode.antCount += 1
            else:
                mode.antCount += 1
        mode.time += 1
        
    def drawBurrows(mode,canvas):
        r = 17
        for col in range(len(mode.burrows)):
            for row in range(len(mode.burrows[col])):
                if mode.burrows[col][row]:
                    cx = 16+col*32
                    cy = 16+row*32
                    canvas.create_rectangle(cx-r,cy-r,cx+r,cy+r,fill="black")

    def redrawAll(mode,canvas):
        #drawCanvas()
        canvas.create_rectangle(0,0,mode.app.width,mode.app.height,
                            fill="blue")
        canvas.create_rectangle(0,mode.dirt,
                mode.app.width,mode.app.height,fill=rgbString(155,118,83))
        
        mode.drawBurrows(canvas)
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
