#!/usr/bin/env python3

# James Livulpi
# October 20th 2013
# Word Count

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

def main():
        count = [0,0,0]
        infile = open("file.txt", "r")
        for line in infile:
                words = line.split()
                count[0] = count[0] + 1
                count[1] += len(words)
                count[2] += len(line)
        print("The number of lines in the file:      ", count[0])
        print("The number of words in the files:     ", count[1])
        print("The number of characters in the file: ", count[2])

main()
