#!/usr/bin/env python3

# James Livulpi
# 10/24/2013
# Outputs day number

# SELF EVALUATION
#   PROGRAM PRESENTATION
#     The header comment at the top contains
#       * Your name:Yes 
#       * Date:Yes 
#       * Short specification of the program:Yes 
#     The comments have correct spelling, grammar and punctuation:Yes 
#     The comments accurately describe the current version of the program:Yes 
#     The #!-line, header comment, self-evaluation, import statements,
#       definition of main, and call to main are all separated
#       by single blank lines:Yes 
#     Blank lines within main are not used (or used very sparingly):Yes 
#     No lines are no longer than 79 characters plus a newline:Yes 
#     There is a single space after every comma, but not before:Yes 
#     There is a space after every # that starts a comment:Yes 
#     Binary operators (+, *, //, etc.) are surrounded by single spaces:Yes 
#     Old versions of this file and editor backups have been removed:Yes 
#     In general, identifiers are meaningful words/phrases:Yes 
#     Long identifiers use camelCaseConvention:Yes 
#
#   OUTPUT PRESENTATION
#     All prompts end with a colon or question mark, followed by a space:Yes 
#     The output has correct spelling, grammar and punctuation:Yes 
#     The lines of output are no longer than 79 characters plus a newline:Yes 
#     The prompts plus expected input are no longer than 
#       79 characters plus a newline:Yes 
#     Blank lines in the output are used sparingly:Yes 
#     The output explains well the purpose of the program:Yes 
#     The prompts make it completely clear what is expected in the input:Yes 
#
#   CORRECTNESS 
#     The file has a top line #!/usr/bin/python3 :Yes 
#     The file has been made executable (by chmod u+x *.py):Yes 
#     The program executes without errors in idle3:Yes 
#     The program executes without errors in the shell:Yes 
#     The program meets the I/O specification:Yes 
#
#   DESIGN
#     The program contains a function main and a call to main:Yes 
#
#   GOOD PRACTICES
#     At every stage of development, my program conformed to most of the
#       requirements above:Yes 
#     I developed the program incrementally, testing very frequently
#       and adding/changing small amounts of code between the tests:Yes 
#     When I type an opening construct such as ", (, 
#       I immediately type the corresponding closing construct, such as ", ),
#       and I keep inserting code between them:Yes 

def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
            
def dayNum(month, day, year):
    retval = 31 * (month - 1) + day
    if month > 2:
        retval = retval - (4 *(month) + 23) // 10
        if isLeap(year):
            retval = retval + 1
    return retval

def getError(prompt):
    while True:
        try:
            n = int(input(prompt))
            break
        except ValueError:
            print("Please enter a interger...")
    return n
    
def main():
    month = getError("Month? ")
    day = getError("Day  ? ")
    year = getError("Year ? ")
    day = dayNum(month, day, year)
    print("That is day number", day)
            
            
 
        
    
if __name__ == '__main__':
    main()
                     
    
    
