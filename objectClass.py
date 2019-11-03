from tkinter import *

def rgbString(red, green, blue):
    # Don't worry about how this code works yet.
    return "#%02x%02x%02x" % (red, green, blue)

class Particle(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.particleType = ''
        self.fallRate = 3 # 1 particle size per timer fire
        self.activated = False

        dust = rgbString(255, 194, 153)
        self.allColors = []
        self.color = dust
        self.allColors.append(self.color)
    
    def getHashables(self):
        return self.color #colors are unique per particle type

    def __hash__(self):
        return hash(self.getHashables())
    
    def __eq__(self, other):
        return ( type(other) == type(self) ) and \
               (self.color == other.color)

    def move(self):
        self.cy += self.fallRate

    def draw(self, canvas):
        canvas.create_rectangle(cx - 1, cy - 1, cx + 1, cy + 1,
                                fill = self.color)