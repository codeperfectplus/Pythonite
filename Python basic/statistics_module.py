'''
@author : CodePerfectPlus
@Topic  : Statistics Module

statistics Module can only be apply on python 3'''



import statistics as st

list_01=[2,4,6,7,4,3,6,8,0,2,4,7,5,2,7,3,8,5,3,5,6]

x=st.mean(list_01)
print(x)

y=st.median(list_01)
print(y)

a=st.stdev(list_01)
print(a)

b=st.variance(list_01)
print(b)
