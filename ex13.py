# PARAMETERS, UNPACKING, VARIABLES

from sys import argv  # this is called an import
# argv is the "argument varible"
# argv holds the arguments you pass to your Python scriptwhen you run it

# Read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second varible is:", second)
print("Your third varible is:", third)
