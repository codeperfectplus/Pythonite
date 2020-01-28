'''A Prime Number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
The first few prime number are {2,3,5,7,11}
'''
input("Enter Your Range For Print Number \nLower Range \n Upper Range\n Like  1 to 20")
a = int(input("Lower Range :\n "))
b = int(input("Upper Range :\n "))
solution =[]
'''
a = Lower Range 
b = Upper Range
solution = a list to contain prime Number
'''
print("-"*20)   
for val in range(a, b + 1):
	if val >1:
		for n in range(2, int(val**0.5)):
			if ( val % n) == 0:
				break

		else:
			solution.append(val)

print(solution)
