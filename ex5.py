name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.00 # inches
height_cent = height * 2.54
weight = 180 # lbs
weight_kg = weight * .453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %f centimeters." % height_cent
print "He weighs %d pounds." % weight
print "That's %f kilograms." % weight_kg
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is trick, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
