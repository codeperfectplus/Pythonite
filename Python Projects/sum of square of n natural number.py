'''
Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.
if N = 4 
1^2 + 2^2 + 3^2 + 4^2 = 30
The idea is to run a loop from 1 to n and for each i, 1 <= i <= n, find i2 to sum.
'''

def squaresum(n):
	sum = 0
	for i in range(1, n+1):
		sum += (i * i)
	return sum

n = int(input("Enter Number to Print Sum Of square of N Natural Number :\n"))
print(squaresum(n))