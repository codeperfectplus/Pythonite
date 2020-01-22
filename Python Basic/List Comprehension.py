'''
@author : CodePerfectPlus
@topic  : List Comprehensions

List Comprehension is faster way to create list instead of declearning it first.
'''

x = [(i,j) for i in range(5) for j in range(10) if i + j < 10]# It will return value of (i,j) which are not more than 10.
print(x)
