#!/usr/bin/env python3

# James Livulpi
# September 3rd 2013
# A calculator that evaluates exactly three expressions

# SELF EVALUATION
#
# PROGRAM PRESENTATION
# The header comment contains
#       * Your name:Yes
#       * Date:Yes
#       * Short specification of the program:Yes 
# There is a space after every # that starts a comment:Yes
# The comments have correct spelling, grammar and punctuation:Yes
# All lines are no longer than 79 characters plus a newline:Yes
# There is a single space after every comma, but not before:Yes
# Old versions of this file and editor backups have been removed:Yes 
#
# OUTPUT PRESENTATION
# All prompts end with a colon or question mark, followed by a space:Yes 
# The output has correct spelling, grammar and punctuation:Yes 
# The lines of output are no longer than 79 characters plus a newline:Yes 
# The prompts plus expected input are no longer than 
#    79 characters plus a newline:Yes
#
# PROGRAM CORRECTNESS
# The program meets the I/O specification:Yes
# The program executes without errors in idle3:Yes
# The file has a top line #!/usr/bin/python3 :Yes 
# The file has been made executable (by chmod u+x *.py):Yes  
# The program executes without errors in the Linux shell:Yes 
# DESIGN
# The program contains a function main:Yes 
# The program contains a call to main:Yes
#
# GOOD PRACTICES
# When I type an opening construct such as ", (, 
#    I immediately type the corresponding closing construct, such as ", ),
#    and I keep inserting code between them:Yes 

def main():
    for i in range(3):
       question = (input("Enter an arithmetical expression: "))
       answer = eval(question)
       print (question, "=", answer)
       
main()
    
