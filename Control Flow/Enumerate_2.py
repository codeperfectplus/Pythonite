'''
Zip Function to used to combine two list together and it's works like iteration.
'''


x = ['Hellow', 'Hi']
y = ['World', 'Programmer']


for x, y in zip (x, y):
	print(x,y)


x = [5 ,7, 10, 12, 15, 20]
y = [3 ,5, 4, 10, 10, 19]
for x , y in zip(x,y):
	print('%s is greater than %s' %(x,y))

