from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

name = raw_input("What is your name: ")

print "My name is %s and the script is called %s." % (name, script)
