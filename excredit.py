#!/usr/bin/env python3

# James Livulpi
# October 19th 2013
# Triangle program with functions

# SELF EVALUATION
#   PROGRAM PRESENTATION
#     The header comment at the top contains
#       * Your name:yes 
#       * Date:yes 
#       * Short specification of the program: 
#     The comments have correct spelling, grammar and punctuation:yes 
#     The comments accurately describe the current version of the program:yes 
#     The #!-line, header comment, self-evaluation, import statements,
#       definition of main, and call to main are all separated
#       by single blank lines:yes 
#     Blank lines within main are not used (or used very sparingly):yes 
#     No lines are no longer than 79 characters plus a newline:yes 
#     There is a single space after every comma, but not before:yes 
#     There is a space after every # that starts a comment:yes 
#     Binary operators (+, *, //, etc.) are surrounded by single spaces:yes 
#     Old versions of this file and editor backups have been removed:yes 
#     In general, identifiers are meaningful words/phrases:yes 
#     Long identifiers use camelCaseConvention:yes 
#
#   OUTPUT PRESENTATION
#     All prompts end with a colon or question mark, followed by a space:yes 
#     The output has correct spelling, grammar and punctuation:yes 
#     The lines of output are no longer than 79 characters plus a newline:yes 
#     The prompts plus expected input are no longer than 
#       79 characters plus a newline:yes 
#     Blank lines in the output are used sparingly:yes 
#     The output explains well the purpose of the program:yes 
#     The prompts make it completely clear what is expected in the input:yes 
#
#   CORRECTNESS 
#     The file has a top line #!/usr/bin/python3 :yes 
#     The file has been made executable (by chmod u+x *.py):yes 
#     The program executes without errors in idle3:yes 
#     The program executes without errors in the shell:yes 
#     The program meets the I/O specification:yes 
#
#   DESIGN
#     The program contains a function main and a call to main:yes 
#
#   GOOD PRACTICES
#     At every stage of development, my program conformed to most of the
#       requirements above:yes 
#     I developed the program incrementally, testing very frequently
#       and adding/changing small amounts of code between the tests:yes 
#     When I type an opening construct such as ", (, 
#       I immediately type the corresponding closing construct, such as ", ),
#       and I keep inserting code between them:yes 


from graphics import *
import math

ppi = 72
width = 10 * ppi

def getPoint(win):
    point = win.getMouse()
    point.draw(win)
    return point

def calcDistance(point1, point2):
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    distance = math.sqrt(dx ** 2 + dy ** 2)
    return distance

def calcPerimeter(point1, point2, point3):
    a = calcDistance(point1, point2)
    b = calcDistance(point2, point3)
    c = calcDistance(point3, point1)
    perimeter = a + b + c 
    return perimeter

def calcArea(point1, point2, point3):
    a = calcDistance(point1, point2)
    b = calcDistance(point2, point3)
    c = calcDistance(point3, point1)
    side = calcPerimeter(point1, point2, point3) / 2
    area = math.sqrt(side * (side - a) * (side - b) * (side - c))
    return area
    
def main():
  
  win = GraphWin("Triangle" ,width,10 * ppi)
  win.setCoords(0,0,10,10)
  message = Text(Point(5,9.5), "Click to mark a corner of a triangle. ")
  message.setSize(24)
  message.draw(win)
  point1 = getPoint(win)
  message.setText("Click to mark the second corner of the triangle. ")
  point2 = getPoint(win)
  message.setText("Click to mark the third corner of the triangle. ")
  point3 = getPoint(win)
  triangle = Polygon(point1, point2, point3) 
  triangle.setFill("blue")
  triangle.setWidth(3)
  triangle.draw(win)
  message.setText("")
  lengA = calcDistance(point2, point1)
  lengB = calcDistance(point3, point2)
  lengC = calcDistance(point1, point3)
  perimeter = calcPerimeter(point1, point2, point3)
  area = calcArea(point1, point2, point3)
  message.setText("Area: %s square inches; Perimeter: %s inches. "
                  % (area, perimeter))
  message.setSize(12)
  close = Text(Point(5,9), "Click anywhere to close the window. ")
  close.draw(win)
  win.getMouse()
  win.close()

if __name__ == '__main__':
    main()
    
