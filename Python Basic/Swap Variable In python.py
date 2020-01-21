'''
@author : CodePerfectPlus
@Topic  : Swap Variable In Python
'''
a = 12
b = 90
#Way 1
'''
temp = a
a = b 
b = temp 

print(f'\n After swaping \n a = {a} \n b ={b}')
'''

# pythonic Way

a, b = b, a
print(f'\n swaping in Pythonic Way \n a = {a} \n b = {b}')