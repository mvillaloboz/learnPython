# import argument variable function
from sys import argv

# set how many arguments for the argv
script, filename = argv

# print the fact that filename argument will be truncated
# tell user how to exit without truncating
# tell user how to continue with operation
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# accept input from user with prompt '?'
raw_input("?")

# tell the user that the file is being opened
# set variable 'target' to open the filename and write to it
print "Opening the file..."
target = open(filename, 'w')

# tell user the file has been cleared
# clear the target variable, which has the filename and write stored to it
print "Truncating the file. Goodbye!"
target.truncate()

# tell the user that we need three lines
print "Now I'm going to ask you for three lines."

# set the variables for the three lines as input with prompts
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# tell the user the file is being written
print "I'm going to write these to the file."

# write each line with a newline character between
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# tell user the file is being close
# close the target variable
print "And finally, we close it."
target.close()