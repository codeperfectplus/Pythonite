'''A Prime Number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
The first few prime number are {2,3,5,7,11}
'''

a = 1
b = 30

for val in range(a, b + 1):
	if val >1:
		for n in range(2, val):
			if ( val % n) == 0:
				break

		else:
			print(val)
