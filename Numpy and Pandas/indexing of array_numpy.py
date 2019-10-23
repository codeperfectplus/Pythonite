''' 
indexing is helpful for analysing and manipulating data for find insight.
slicing :: numpy array can be sliced.
'''

#np is alias for numpy
import numpy as np

arr = np.array(   [[-1, 2, 0, 4],
	               [-3, 5, 7, 3],
	               [5, 3, -4, 2],
	               [6, -5, 1, 6]]   )


# slicing with first 2 row and alternate columns
slic = arr[:2 , ::3]
slic2 = arr[:2 , ::2]
print(slic)
print()
print(slic2)


#boolean array indexing example

cond = arr > 0
temp = arr[cond]

print('Elements greater than 0 : \n',temp)