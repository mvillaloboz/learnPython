print "How old are you?",
age = raw_input()
print "How tall are you?",
height = int(raw_input())
print "How much do you weigh?",
weight = int(raw_input())

height_m = height * 0.3048
weight_m = weight * 0.453592
weight_s = weight * 0.157473

print "So, you're %r years old, %r feet tall and weigh %r pounds." % (age, height, weight)
print "In Europe, you'd be %d meters tall and weigh %d kilograms (%d stone)." % (height_m, weight_m, weight_s)

print "What year is it?",
year = raw_input()
print "What hour is it?",
hour = raw_input()
print "What minute is it?",
min = raw_input()

print "So, it is %r:%r in the year %r." % (hour, min, year)