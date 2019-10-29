def simplegenerator():
	t = 1
	print ('First Result is :', t)
	yield t

	t +=1
	print ('Second Result is :', t)
	yield t

	t +=1
	print ('Third Result is :', t)
	yield t 

x = simplegenerator()
next(x)
next(x)
next(x)

print("Square From 1 to 10")

squarefun = (num ** 2 for num in range(10))
for x in squarefun:
	print(x)


string = 'PythoN'
reverse = list(string[i] for i in range(len(string)-1, -1, -1))
print(reverse)