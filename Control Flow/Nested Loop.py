'''
Python Programming language allow to use one loop inside another loop.
for iterator in sequence:
	for iterator in sequence:
		statements(s)
		statements(s)
		'''
for i in range(1,7):
	for j in range(i):
		print(i, end ='')
	print()