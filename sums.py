#!/usr/bin/env python3

# James Livulpi
# October 1st 2013
# Returns sums of first natural numbers and sum of first cubes

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



def sumN(n):
    accum = 0
    for i in range(n):
        next = i - n
        accum = accum - next 
    return accum

def sumNcubes(n):
    accum = 0
    for i in range(n):
        next = i - n
        accum = accum - next ** 3
    return accum
    
def main():
    n = eval(input("Please enter a natural number: "))
    x = sumN(n) 
    print("The sum of the first", n,"positive intergers is",x)
    y = sumNcubes(n)
    print("The sum of the first", n,"cubes is", y)

main()
