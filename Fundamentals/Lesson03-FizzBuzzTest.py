##Python 2 Version

count = 0
while (count < 101):
    if (count % 5) == 0 and (count % 3) == 0:
        print "FizzBuzz"
        count = count +1
    elif (count % 3) == 0:
        print "Fizz"
        count = count + 1
    elif (count % 5) == 0:
        print "Buzz"
        count = count +1
    else:
        print count
        count = count + 1
        
        
