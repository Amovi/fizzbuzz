import math
numberprint = int(input("How many numbers should we print? "))
fizz = int(input("For multiples of what number shall we print Fizz? "))
buzz = int(input("For multiples of what number shall we print Buzz? "))
for i in range(1,numberprint+1):
    x = str(i)
if 0 == i%fizz and 0 == i%buzz:
     x = "FizzBuzz"
elif 0 == i%fizz:
    x = "Fizz"
elif 0 == i%buzz:
    x = "Buzz"
print (x)
