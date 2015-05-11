from sys import argv

script, blorg, second = argv

print "The script is called:", script
print "Your first variable is:", blorg
print "Your second variable is:", second
third = raw_input("Third? ") 
print "Your third variable is: %r" % third