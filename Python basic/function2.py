'''
@author : CodePerfectPlus
@Topic  : Function -2
'''

def my_func(food):
    for x in food:
        print(x)

fruits_list =['Apple','Mango','Banana','Guavava']
electronics_item=['charger','iron','Fridge','Fan',"T.v"]

print('List 1')
my_func(fruits_list)
print('----------------------')
print('List 2')
my_func(electronics_item)
 #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def mul_fun(x):
     return 2**x

print(mul_fun(2))
print(mul_fun(3))
print(mul_fun(4))
print(mul_fun(5))
print(mul_fun(6))
