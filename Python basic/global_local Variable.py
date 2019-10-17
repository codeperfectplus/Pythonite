'''A Global Variable is one that can be accessed anywhere.
a local Variable is the opposite,
 it can only be accessed within its frame.
 '''

x=6

def my_function():
     print(x)

     z=5
     print(z)
my_function()

''' We can't call "z" outside the function because z is local variable
'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

x=40

def function():
    global x #we can define function as a global
    print(x)
    x+=5
    print(x)
function()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

x=100
def function2(x):
    print(x)
    x+=5
    print(x)
    return x

x=function2(x)
print(x)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
x=200

def example(modify):
    print(modify)
    modify+=5
    print(modify)
    return modify

x=example(x)
print(x)
