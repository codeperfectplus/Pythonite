''' List and Tuple in Python are just like array to store data
List are mutable and Tuple are immutable that means we can't change,modify a tuple.
generally tuple is used when we have to save some data as like "Ip address",
"Mac address"
'''

def example():
    return 20,13

x,y=example()
print(x,y)
'''The tuple had no bracket aroound it at all. if there are no encasing brackets
of any types,then  python will recognize the data as a tuple.Tuple also can have
() Curved bracket.

'''

x=[3,4,5,7,8,4,7,5]
print(x)

print(x[0],x[-1])
x.sort()
print(x)
'''
The Above Example Is for List.
 '''
