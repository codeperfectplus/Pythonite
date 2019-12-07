'''
we can create array By many method
'''
import numpy as np


# Create Numpy array by list
list = [1, 3, 5, 6]
list2= [1, 4, 5, 7]

arr = np.array([list,list2])

type(arr)

#create numpy array by arrange
np.arange(0,20)
np.arange(1,21).reshape(4,5)

#by random
np.random.randn(3,3)

#by one and zeros
np.ones((4,3))

#by random sample
np.random.random_sample((2,4))

np.random.randint(0,100,10).reshape(5,2)


