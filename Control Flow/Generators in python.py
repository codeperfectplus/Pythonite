# Simple Generator Function
def simpleGenerator():
	yield 1
	yield 2
	yield 3

x = simpleGenerator()

print(x.__next__());
print(x.__next__());
print(x.__next__());

