#!/usr/bin/env python3

from graphics import *
from random import *

class Ball:
    def __init__(self,win,x,y):
        self.win = win
        self.x = x
        self.y = y
        self.radius = 10
        self.dx = 5
        self.dy = 5
        self.circle = Circle(Point(self.x,self.y),self.radius)
        color = color_rgb(randrange(256),randrange(256),randrange(256))
        self.circle.setFill(color)
        self.circle.draw(self.win)
        
    def bounce(self):
        
        self.x = self.dx + self.x
        self.y = self.dy + self.y
        if self.x - 10 < 0 or self.x + 10 > 500:
            self.dx = -self.dx
        if self.y - 10 < 0 or self.y + 10 > 500:
            self.dy = -self.dy
        self.circle.move(self.dx,self.dy)

def main():
    win = GraphWin("Bonce Many", 500, 500)
    balls= []
    click = win.getMouse()
    x = click.getX()
    y = click.getX()
    while True:
        for i in range(30):
            if click == True:
                balls.append(Ball(win,(x,y),(x,y)))
        for item in balls:
                item.bounce()
    win.close()

if __name__ == '__main__':
	main()
        

    
