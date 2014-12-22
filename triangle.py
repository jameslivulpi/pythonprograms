#!/usr/bin/env python3

# James Livulpi
# 9/18/2013
# Three click triangle that calculates and displayes area and perimeter.

#SELF EVALUATION
#
# PROGRAM PRESENTATION
# The header comment contains
#       * Your name:Yes 
#       * Date:Yes
#       * Short specification of the program:Yes 
# There is a space after every # that starts a comment:Yes 
# The comments have correct spelling, grammar and punctuation:Yes 
# The comments accurately describe the current version of the program:Yes 
# All lines are no longer than 79 characters plus a newline:Yes 
# There is a single space after every comma, but not before:Yes 
# Old versions of this file and editor backups have been removed:Yes 
# Binary operators (+, *, //, etc.) are surrounded by single spaces:Yes 
# In general, identifiers are meaningful words/phrases:Yes 
# Long identifiers use camelCaseConvention:Yes 
# The #!-line, header comment, self-evaluation, import statements,
# definition of main, and call to main are all separated
#       by single blank lines:Yes 
# Blank lines within main are not used (or used very sparingly):Yes 
#
# OUTPUT PRESENTATION
# All prompts end with a colon or question mark, followed by a space:Yes 
# The output has correct spelling, grammar and punctuation:Yes 
# The lines of output are no longer than 79 characters plus a newline:Yes 
# The prompts plus expected input are no longer than 
#    79 characters plus a newline:Yes 
# Blank lines in the output are used sparingly:Yes 
# The output explains well the purpose of the program:Yes 
# The prompts make it completely clear what is expected in the input:Yes 
#
# PROGRAM CORRECTNESS
# The program meets the I/O specification:Yes 
# The program executes without errors in idle3:Yes 
# The file has a top line #!/usr/bin/python3 :Yes 
# The file has been made executable (by chmod u+x *.py):Yes 
# The program executes without errors in the Linux shell:Yes 
#
# DESIGN
# The program contains a function main:Yes 
# The program contains a call to main:Yes 
#
# GOOD PRACTICES
# At every stage of development, my program conformed to most of the
#    requirements above:Yes 
# I developed the program incrementally, testing very frequently
#    and adding/changing small amounts of code between the tests:Yes 
# When I type an opening construct such as ", (, 
#    I immediately type the corresponding closing construct, such as ", ),
#    and I keep inserting code between them:Yes 

from graphics import *

import math

ppi = 72
width = 10 * ppi

def main():
  
  win = GraphWin("Triangle" ,width,10 * ppi)
  win.setCoords(0,0,10,10)
  message = Text(Point(5,9.5), "Click to mark a corner of a triangle. ")
  message.setSize(24)
  message.draw(win)

  p1 = win.getMouse()
  Circle(p1, 1.5 / ppi)
  p1.draw(win)
  message.setText("Click to mark the second corner of the triangle. ")
  p2 = win.getMouse()
  Circle(p2, 1.5 / ppi)
  p2.draw(win)
  message.setText("Click to mark the third corner of the triangle. ")
  p3 = win.getMouse()
  Circle(p3,1.5 / ppi)
  p3.draw(win)

  triangle = Polygon(p1, p2, p3) 
  triangle.setFill("blue")
  triangle.setWidth(3)
  triangle.draw(win)
  message.setText("")

  dx = p2.getX() - p1.getX()   
  dy = p2.getY() - p1.getY()
  lengA = math.sqrt(dx ** 2 + dy ** 2)
  dx = p3.getX() - p2.getX()
  dy = p3.getY() - p2.getY()
  lengB = math.sqrt(dx ** 2 + dy ** 2)
  dx = p1.getX() - p3.getX()
  dy = p1.getY() - p3.getY()
  lengC = math.sqrt(dx ** 2 + dy ** 2)

  perimeter = lengA + lengB + lengC
  side = perimeter / 2
  area = math.sqrt(side * (side - lengA) * (side - lengB) * (side - lengC))
  message.setText("Area: %s square inches; Perimeter: %s inches. "
                  % (area, perimeter))
  message.setSize(12)
  close = Text(Point(5,9), "Click anywhere to close the window. ")
  close.draw(win)
  win.getMouse()
  win.close()

main()
