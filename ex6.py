# Strings and Text
# A STRING is a bit of text you want to display to someone
# A string must have "" or '' for it to be considered a string
# A string can have as many variable as possible
# A variable is a line with a set of name and value
# "f-string" is used when adding a variable in a string

types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")  # A string inside a string
print(f"I also said:'{y}'")  # A string inside a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
