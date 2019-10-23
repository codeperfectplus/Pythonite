# create array with help of numpy
# print() is used for space between differnt array to show properly in output

import numpy as np 

#Array Created with float type
a = np.array( [[1, 2, 4],[4, 5, 4]], dtype ='float')
print(a)
print()    
#Creating Array From Tuple
b = np.array((1, 3, 6))
print(b)
print()
#creating a array with all zero values
c = np.zeros((3,2))
print(c)
print()
#crete a constant value array of complex type
d = np.full((4, 4), 5,dtype='complex')
print(d)