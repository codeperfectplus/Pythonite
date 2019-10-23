'''
Sort values the way to arrange data in particular order.In Numpy, we can perform various sorting operaions using the various functions that are provided
in the library like sort,lexsort
'''

#np in alias of numpy
import numpy as np

# sort value in row , for row =0,column =1

a = np.array( [[12, 15],
			   [10, 5]] )
arr = np.sort(a, axis=0)
print(arr)



