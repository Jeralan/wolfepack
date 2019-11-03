from tkinter import *
from PIL import Image,ImageTk

class Ant(object):
    def __init__(self, mode, cx, cy):
        self.mode = mode
        self.cx = cx
        self.cy = cy
        self.id = mode.time

        spriteSheet = mode.app.loadImage('antSprites.png')

        self.dir = 1
        self.spriteIndex = 0
        self.sprites = []
        for i in range(4):
            dirSprites = []
            for j in range(4):
                sprite = spriteSheet.crop((64 * j, 64 * i,
                                           64 * (j + 1), 64 * (i + 1)))
                dirSprites.append(sprite)
            self.sprites.append(dirSprites)
        self.image = self.sprites[self.dir][self.spriteIndex]
        self.image = mode.app.scaleImage(self.image, 1/2)
    def getHashables(self):
        return self.id #colors are unique per particle type

    def __hash__(self):
        return hash(self.getHashables())
    
    def __eq__(self, other):
        return ( type(other) == type(self) ) and self.id == other.id

    def check(self, other):
        pass

    #def move(self):
        
        # if self.collision():
        #     pass

    def draw(self, canvas):
        canvas.create_image(self.cx, self.cy, 
                            image=ImageTk.PhotoImage(self.image))
