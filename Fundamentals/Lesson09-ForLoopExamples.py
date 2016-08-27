for x in range(0, 3):
    print "We're on time %d" % (x)

####################################

fruits = ['banana', 'apple',  'mango']

for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]

print "Good bye!"

#######################################

for x in range(1, 11):
    for y in range(1, 11):
        print '%d * %d = %d' % (x, y, x*y)


#####################################

for letter in 'Python':     # First Example
   print 'Current Letter :', letter

fruits = ['banana', 'apple',  'mango']

for fruit in fruits:        # Second Example
   print 'Current fruit :', fruit

print "Good bye!"

######################################
#Early Exit

for x in xrange(3):
    if x == 1:
        break

#######################################

for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'

#######################################
