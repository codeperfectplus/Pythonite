'''
[[ 1, 2 , 3],[4, 2, 5]]
shape of array is (2,3)
2 row and 3 columns
'''

import numpy as np  # np is alias for numpy, so we can use this instead of numpy.

arr = np.array( [[ 1, 2, 3],
	             [ 4, 2, 4]] )

#array type
print("Array is of type : ", type(arr))

#array dimension
print('No. of dimension : ',arr.ndim)

#shape of array
print("shape Of Array : ",arr.shape)

#array size
print("Size of Array: ",arr.size)

#Data-Type( Int,String, Boolean)
print("Type Of Elements Are : ",arr.dtype)