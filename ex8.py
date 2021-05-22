# Printing Printing
# Using a fuction to turn the formatter into other strings.
# "" is put on one two and not true and false as python recognises
# true and false a keywords representing the concept of true or false

formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "or a song about fear"
))
