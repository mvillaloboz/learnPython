# declare variable 'filename' as having input from user with prompt
filename = raw_input("Please enter file name: ")

# declare variable 'txt' that uses the open function on 'filename'
txt = open(filename)

# displays variable 'txt' using the read function
print txt.read()