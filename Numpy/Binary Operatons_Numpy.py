#Binary Operatons_Numpy\

#np is alias to numpy
import numpy as np

a = np.array( [[1, 2],
			   [4, 4]] )
b = np.array( [[5, 4],
			   [5, 2]] )

# add 2 array 
print("Sum Of array :" ,a+b)
print("Multipl of array :",a*b)

print('*'*25)
print(" Matrix Multiplication :\n"+"*****\n" ,a.dot(b))