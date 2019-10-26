'''
Python Programming language allow to use one loop inside another loop.
for iterator in sequence:
	for iterator in sequence:
		statements(s)
		statements(s)
		'''

from __future__ import print_function

for i in range(1,4):
	for j in range(i):
		print(i, end ='')
	print()
