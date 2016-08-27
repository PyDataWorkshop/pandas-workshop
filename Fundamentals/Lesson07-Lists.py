## The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets.
## Important thing about a list is that items in a list need not be of the same type.
## Creating a list is as simple as putting different comma-separated values between square brackets.

#------------------------------------------------------------------#

# For example
list1 = ['physics', 'chemistry', 1997, 2000]; 
list2 = [1, 2, 3, 4, 5 ]; 
list3 = ["a", "b", "c", "d"] 

#------------------------------------------------------------------#

# Similar to string indices, list indices start at 0, and lists can be sliced, concatenated and so on.

### Accessing Values in Lists
## To access values in lists, use the square brackets for slicing along with the 
## index or indices to obtain value available at that index.
 
list1 = ['physics', 'chemistry', 1997, 2000]; 
list2 = [1, 2, 3, 4, 5, 6, 7 ]; 

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

#------------------------------------------------------------------#

list1 = ['physics', 'chemistry', 1997, 2000]; 
list2 = [1, 2, 3, 4, 5, 6, 7 ]; 

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

#------------------------------------------------------------------#

list1 = ['physics', 'chemistry', 1997, 2000]; 

print(list1) 
del(list1[2])

print("\nAfter deleting value at index 2 : " )
print(list1)
