'''
python program for accnmulate() and chain()
'''

import itertools

import operator

list_1 =[2, 5, 7, 9]

list_2 =[3, 6, 5, 3]

list_3 =[2, 5, 3, 2]

# using accumulate()
print('The Sum After Each Iteration is : ',end = " ")
print(list(itertools.accumulate(list_1)))

# using accumulate()
#multipllication by iteration row wise
print('The Product after each iteration is :' , end =' ')
print(list(itertools.accumulate(list_1,operator.mul)))

 #Print all Element of list
print("All values in mentioned chain are :", end=' ')
print(list(itertools.chain(list_1, list_2, list_3)))