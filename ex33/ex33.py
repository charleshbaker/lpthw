
def numeric_list_builder(length):
    i = 0
    numbers = []
    while i < length:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + 1
        print "Numbers now:  ", numbers
        print "At the bottom i is %d" % i
    return numbers

myList = numeric_list_builder(10)

print "The numbers:  "
for num in myList:
    print num


