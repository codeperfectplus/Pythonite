# check wheather no. is prime or not

num = 11

if num > 1:

	for i in range (2,num//2):

		if (num % i) == 0:
			print(num, " Is Not a prime Number")
			break
	else:
		print(num, 'is a prime number')