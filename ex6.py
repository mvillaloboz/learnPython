# setting the variables as strings
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# displaying the variable strings
print x
print y

# displaying the variables inside of other strings using character formatters
print "I said: %r." % x
print "I also said: '%s'." % y

# setting the variables for the next set of lines
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# displaying the joke evaluation lines
print joke_evaluation % hilarious

# setting the variables for w and e
w = "This is the left side of..."
e = "a string with a right side."

# displaying w and e together
print w + e