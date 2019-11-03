from cmu_112_graphics import *
from objectClass import *
from tkinter import *


class dustGame(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 25

class GameMode(Mode):
    def appStarted(mode):
        mode.particles = []
        mode.split = (2/3)*app.mode.height

    def mousePressed(mode,event):
        mode.particles.append(Particle(event.x,event.y))
    
    def mouseDragged(mode,event):
        mode.particles.append(Particle(event.x,event.y))

    def timerFired(mode):
        for particle in mode.particles:
            particle.move()
            for OtherParticle in mode.particles:
                if particle.collision(OtherParticle)
    def redrawAll(mode,canvas):
        #drawCanvas()
        for particle in mode.particles:
            particle.draw(canvas,mode)
        

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

def runWolfePack():
    dustGame(width=600,height=600)

def main():
    runWolfePack()

if __name__ == '__main__':
    main()
