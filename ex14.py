from sys import argv

script, user_name, time = argv
prompt1 = 'Yes or No? '
prompt2 = 'Enter City: '
prompt3 = 'Enter Computer: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I see that it's %s o'clock." % (time)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt1)

print "Where do you live %s?" % user_name
lives = raw_input(prompt2)

print "What kind of computer do you have?"
computer = raw_input(prompt3)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)