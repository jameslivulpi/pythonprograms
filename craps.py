#!/usr/bin/env python3

# James Livulpi
# 11/08/2013
# Simulates 500 games of craps

import random

def main():
    win = playManyGames(500)
    probability = win / 500
    print("The probability of winning is %s/500 = %s " % (win, probability))

def rollOneDie():
    return random.randint(1,6)

def rollTwoDice():
    return rollOneDie() + rollOneDie()

def playOneGame():
    firstThrow = rollTwoDice()
    if firstThrow == 7 or firstThrow == 11:
        return True
    elif firstThrow == 2 or firstThrow == 3 or firstThrow == 12:
        return False
    else:
        while True:
            nextThrow = rollTwoDice()
            if nextThrow == firstThrow:
                return True
            elif nextThrow == 7:
                return False
            
def playManyGames(howMany):
    wins = 0
    for i in range(howMany):
        if playOneGame():
            wins = wins + 1
    return wins

if __name__ == '__main__':main()
