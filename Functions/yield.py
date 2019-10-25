''' 
yield function is similar to return. The yield statement suspends function's execution and sends a value back to caller.
but function can resume where is is left off.
when resumed, the function continues executon immediately after the last yield run.
This allow it's code to produce a series of value over time,raher then computing them aat once and sending them back list a list.
'''

#Example___001

def simpleGen():
	yield 1
	yield 2
	yield 3

for x in simpleGen():
	print(x)

'''
python program to generate square from 1 to 50 using yield
yield will suspend the function execution then function can resume itself.
'''
print("Square program 1 to 50\n")
#example___002

def nextSquare():
	i = 1;

	while True:
		yield i*i
		i += 1

for x in nextSquare():
	if x > 50:
		break
	print(x)


