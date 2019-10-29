#Simple Generator for fibonacci number
def sub(limit):
	#initializing first two fibonacci number
	a, b = 0, 1

	#one by one yield next fibonacci number
	while a < limit:
		yield a
		a, b = b, a+b

x = sub(5)

#Using For in Loop 
print("\n For In Loop \n")
for i in sub(5):
	print(i)
