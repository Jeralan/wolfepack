from tkinter import *
from PIL import Image,ImageTk
import random

class Ant(object):
    def __init__(self, mode, cx, cy):
        self.mode = mode
        self.cx = cx
        self.cy = cy
        self.id = mode.time
        self.dy = 0
        self.dx = 1

        spriteSheet = mode.app.loadImage('antSprites.png')
        spriteSheet = mode.app.scaleImage(spriteSheet, 1/2)
        self.dir = 1
        self.spriteIndex = 0
        self.image = mode.sprites[self.dir][self.spriteIndex]
    
    def getHashables(self):
        return self.id #colors are unique per particle type

    def __hash__(self):
        return hash(self.getHashables())
    
    def __eq__(self, other):
        return ( type(other) == type(self) ) and self.id == other.id

    def check(self, other):
        pass

    def move(self, mode):
        self.spriteIndex = (self.spriteIndex + 1) % 4
        self.image = mode.sprites[self.dir][self.spriteIndex]
        self.cy += self.dy
        self.cx += self.dx

    def changeDir(self, mode):
        gridX = (self.cx-16)//32
        gridY = (self.cy-16)//32
        directions = [0,1,2,3]
        newDir = random.choice(directions)
        newDx,newDy = getCoords(newDir)
        newGridX,newGridY = gridX+newDx,gridY+newDy
        die = False
        while not isPossible(mode,newGridX,newGridY):
            directions.remove(newDir)
            if len(directions) == 1:
                mode.ants.remove(self)
                die = True
                mode.deadAnts[gridX][gridY] = True
                mode.antCount -= 1
                break
            else:
                newDir = random.choice(directions)
                newDx,newDy = getCoords(newDir)
                newGridX,newGridY = gridX+newDx,gridY+newDy

        self.dir = newDir
        self.dx,self.dy = newDx, newDy
        if (gridY+self.dy) >= 1 and not die:
            mode.burrows[int(gridX+self.dx)][int(gridY+self.dy)] = True

    def draw(self, canvas):
        canvas.create_image(self.cx, self.cy, 
                            image=self.image)

def isPossible(mode,gridX,gridY):
    if gridX < 0 or gridY < 0 or gridY >= len(mode.burrows[0]) or gridX >= len(mode.burrows):
        return False
    elif mode.burrows[gridX][gridY]:
        return True
    elif mode.burrows[max(gridX-1,0)][gridY]+mode.burrows[gridX][max(gridY-1,0)]+mode.burrows[min(gridX+1,len(mode.burrows)-1)][gridY]+mode.burrows[gridX][min(gridY+1,len(mode.burrows[0])-1)] > 1:
        return False
    else:
        return True


def getCoords(newDir):
        if newDir == 0:
            newDx, newDy = 0,-1
        elif newDir == 1:
            newDx, newDy = +1, 0
        elif newDir == 2:
            newDx, newDy = 0, +1
        elif newDir == 3:
            newDx, newDy = -1, 0
        return newDx,newDy


class Worm(object):
    def __init__(self, mode, cx, cy, selfID):
        self.mode = mode
        self.cx = cx
        self.cy = cy
        self.dy = -1
        self.dx = 0
        self.id = selfID

        spriteSheet = mode.app.loadImage('wormSprites.png')
        spriteSheet = mode.app.scaleImage(spriteSheet, 1/6)
        self.dir = 1
        self.spriteIndex = 0
        self.sprites = mode.wormCrawl
        self.image = self.sprites[self.spriteIndex]
    
    def getHashables(self):
        return self.id #colors are unique per particle type

    def __hash__(self):
        return hash(self.getHashables())
    
    def __eq__(self, other):
        return ( type(other) == type(self) ) and self.id == other.id

    def changeDir(self, mode):
        gridX = (self.cx-16)//32
        gridY = (self.cy-16)//32
        directions = [0,0,0,1,2,3]
        newDir = random.choice(directions)
        newDx,newDy = getCoords(newDir)
        newGridX,newGridY = gridX+newDx,gridY+newDy
        die = False
        while not isPossible(mode,newGridX,newGridY):
            directions.remove(newDir)
            if len(directions) == 1:
                mode.ants.remove(self)
                die = True
                mode.deadAnts[gridX][gridY] = True
                mode.antCount -= 1
                break
            else:
                newDir = random.choice(directions)
                newDx,newDy = getCoords(newDir)
                newGridX,newGridY = gridX+newDx,gridY+newDy

        self.dir = newDir
        self.dx,self.dy = newDx, newDy

    def isPossible(mode,gridX,gridY):
        if gridX < 0 or gridY < 0 or gridY >= len(mode.burrows[0]) or gridX >= len(mode.burrows):
            return False
        else: return True

    def move(self, mode):
        self.spriteIndex = (self.spriteIndex + 1) % len(self.sprites)
        self.image = self.sprites[self.spriteIndex]
        self.cx += self.dx
        self.cy += self.dy
        count = 0
        while count < len(mode.ants):
            if abs(mode.ants[count].cx-self.cx) < 32 and abs(mode.ants[count].cy-self.cy) < 32:          
                gridX = (mode.ants[count].cx-16)//32
                gridY = (mode.ants[count].cy-16)//32
                mode.deadAnts[gridX][gridY] = True
                mode.ants.remove(mode.ants[count])
            else:
                count += 1

    def draw(self, canvas):
        canvas.create_image(self.cx, self.cy, image=self.image, anchor='s')
