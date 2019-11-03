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
        self.sprites = []
        for i in range(4):
            dirSprites = []
            for j in range(4):
                sprite = spriteSheet.crop((32 * j, 32 * i,
                                           32 * (j + 1), 32 * (i + 1)))
                dirSprites.append(sprite)
            self.sprites.append(dirSprites)
        self.image = self.sprites[self.dir][self.spriteIndex]
    
    def getHashables(self):
        return self.id #colors are unique per particle type

    def __hash__(self):
        return hash(self.getHashables())
    
    def __eq__(self, other):
        return ( type(other) == type(self) ) and self.id == other.id

    def check(self, other):
        pass

    def move(self):
        self.spriteIndex = (self.spriteIndex + 1) % 4
        self.image = self.sprites[self.dir][self.spriteIndex]
        self.cy += self.dy
        self.cx += self.dx

    def changeDir(self, mode):
        newDir = random.randint(0, 3)
        self.dir = newDir
        if self.dir == 0:
            pass
            #self.dx, self.dy = 0, -1
        elif self.dir == 1:
            self.dx, self.dy = +1, 0
        elif self.dir == 2:
            self.dx, self.dy = 0, +1
        elif self.dir == 3:
            self.dx, self.dy = -1, 0
        gridX = (self.cx-16)//32
        gridY = (self.cy-16)//32
        print(gridX,gridY,self.dx,self.dy)
        mode.burrows[int(gridX+self.dx)][int(gridY+self.dy)] = True

    def draw(self, canvas):
        canvas.create_image(self.cx, self.cy, 
                            image=ImageTk.PhotoImage(self.image))
