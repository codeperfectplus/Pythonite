''' range() and xrange() are two functions that could be used to itrate a certain number of item in for loops in python
in python 3, there is no xarange().

ranger() == This returns a list of numbers createed using range() functions
xrange() == This fucntions returns the generator object that can be used to display
number only by looping.

Ranger is Fatser if iterating over the same sequence multiple time.
1. Return Type
2. memeory
3. operaton usages
4. speed
'''
#Return Type
a = range(1,1000)
print('Type Of a is :')
print(type(a))


#Memory Usgaes
import sys

a = range(1, 1000)
#testing the size of a
print('The Size Alloted Using Range() is :')
print(sys.getsizeof(a))

#Operations Usages, slicing
a = range(1, 6)

print("The list after slicing using range is :")
print(a[:5])
