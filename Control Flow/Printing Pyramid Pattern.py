'''
Patterns can be printed using simple for loops. first outer loops is used to handle number of row
and innner nested loop is used to handle the number of columns.
'''

def pypart(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*",end = '')
        print('\n')

n = 5
pypart(n)
