'''
@author : CodePerfectplus
we  can use arithmatic operators to do elementwise operation on array to convert in a new array.
Arithmatic Operaqtors

'''
#np is alias to numpy
import numpy as np

a = np.array([1, 4, 5, 9])
#add 1 to every element

print("Adding 1 to Every Element : \n",a+1)

# Square Each Element
print(" Sqaure Each Element \n",a**2)

#subtract 5 in each elemnent
print(a - 5)

#Double Each Element
a*=2
print(a)