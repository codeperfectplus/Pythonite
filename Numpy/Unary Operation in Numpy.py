#Uranry Operations includes sum, min max,etc
# These can be applied by row wise or column wise

#np is alias for numpy

#for Row == 1
#for column ==0
import numpy as np

arr = np.array( [[1, 5, 5],
				 [4, 7, 2], 
				 [5, 6, 2]] )

#Largest Element Of array
print('largeast element of array',arr.max())
print('Row wise lrgest Element is :',arr.max(axis =1))
print('Column Wise Largest Elemnt Is :',arr.max(axis=0))

print()
print("*"*20)

print("Sum Of array is : ",arr.sum())
print("Collective Sum Of Each ROw :",arr.sum(axis=1))
print(" Collective sum of eacb column :" ,arr.sum(axis=0))