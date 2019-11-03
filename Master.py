import cmu_112_graphics
import objectClass
from tkinter import *


class dustGame(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)

class GameMode(Mode):
    def appStarted(app):
        particles = []

    def mousePressed(app):
        particles.append(Particle(event.x,event.y))

    def timerFired(app):
        for particle in particles:
            particle.move()

    def reDrawAll(app,canvas):
        drawCanvas()
        for particle in particles:
            particle.draw(canvas)

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