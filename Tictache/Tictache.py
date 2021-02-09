# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 23:29:27 2021

@author: Gilbert
"""

from turtle import *

def line(x1, y1, x2, y2):
    up()
    goto(x1, y1)
    down()
    goto(x2, y2)
    
def grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

def drawo(x, y):
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)

def floor(value):
    return ((value + 200) // 133) * 133 - 200

def tap(x,y):
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x,y)
    update()
    state['player'] = not player
    

state = {'player': 0}
players = [drawx,drawo]


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()