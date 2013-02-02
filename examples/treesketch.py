from random import random
from math import pi

randomvals = [random() for i in range(0, 100000)]

def rv():
    return random()

def node(cr, i, angle): 
    if(i > 500 * rv()):
        return
    cr.save()
    cr.translate(0, -10)
    cr.rotate(i * angle)
    cr.set_source_rgb(0, 0, 0)

    width = 2
    cr.rectangle(0, 0, width, 10)
   
    if(rv() < 0.1):
        node(cr, i + 1, -angle)
    node(cr, i + 1, angle)
    cr.restore()   

def draw(cr, width, height):
    cr.set_source_rgb(0, 0, 0)
    cr.translate(width/2.0, height)
    cr.scale(0.5, 0.5)
    node(cr, 0, 0.001)
    cr.fill_preserve()
    cr.stroke()

