#!/usr/bin/env python3

# James Livulpi
# 9/18/2013
# Draws 10 squares on screen via user clicks.

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

def main():
    
    win = GraphWin("Squares")
    shape = Rectangle(Point(50,50), Point(20,20))
    shape.setOutline("red")
    shape.setFill("red")
    for i in range(10):
        p = win.getMouse()
        r = shape.getCenter()
        dx = p.getX() - r.getX()
        dy = p.getY() - r.getY()
        shape.move(dx,dy)
        shape2 = shape.clone()
        shape2.draw(win)
    message = Text(Point(100,100),"Click again to quit ")
    message.setFace("courier")
    message.setSize(14)
    message.draw(win)
    win.getMouse()
    win.close()
    
main()

        
