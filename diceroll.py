#!/usr/bin/env python3

# James Livulpi
# 11/08/2013
# Simulates rolling two dice versus numbers 2 to 12

from graphics import *
import random

def main():
    win = drawWin()
    genGraphCombined(win)
    genGraphRandom(win)
    win.getMouse()
    win.close()
    
def rollOneDie():
    return random.randint(1, 6)

def rollTwoDice():
    return rollOneDie() + rollOneDie()

def rollTwoDiceCombined():
    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1000):
        combine = rollTwoDice()
        counts[combine] += 1
    return counts

def randomNumber2Through12():
    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1000):
        randNumber = random.randint(2, 12)
        counts[randNumber] += 1
    return counts

def genGraphCombined(win):
    combined = rollTwoDiceCombined()
    for x in range(2, 13):
        y = combined[x]
        bar = Rectangle(Point(x, 0), Point(x + 0.6, y))
        bar.setFill("blue")
        bar.draw(win)
        text = Text(Point(x + 0.2, -3), x)
        text.draw(win)
        text = Text(Point(x + 0.3, y + 3), y)
        text.draw(win)
    
def genGraphRandom(win):
    random = randomNumber2Through12()
    for x in range(2, 13):
        y = random[x]
        bar = Rectangle(Point(x + 15, 0), Point(x + 15.6, y))
        bar.setFill("red")
        bar.draw(win)
        text = Text(Point(x + 15.2, -3), x)
        text.draw(win)
        text = Text(Point(x + 15.3, y + 3), y)
        text.draw(win)

def drawWin():
    win = GraphWin("Graph", 800, 700)
    win.setCoords(1, -6, 29, 225)
    text = Text(Point(8, 215), "Rolling Two Dice Combined")
    text.draw(win)
    text = Text(Point(22, 215), "Random Numbers 2 Through 12")
    text.draw(win)
    return win

if __name__ == '__main__':
    main()
        
  


        
    
    
