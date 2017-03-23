import math
list = int (input("How many numbers should we print?"))
fizz = int (input("For numbers of what multiple should we print 'fizz'?"))
buzz = int (input("For numbers of what multiple should we print 'buzz'"))
fizzbuzz = (fizz + buzz):
    print "numbers that are multiples of both numbers"
for i in xrange(1, 101):
    if i % fizzbuzz == 0:
        print "fizzbuzz"
    elif i % fizz == 0:
        print "fizz"
    elif i % buzz == 0:
        print "buzz"
    else:
        print i