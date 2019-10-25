'''
in python, we can return multiple values using
class, list, tuple, dict
'''

#Example__001, Using Class
class Test:
	def __init__(self):
		self.str = 'Python'
		self.x = 20

def sub():
	return Test()

t = sub()
print(t.str)
print(t.x)

#Example__002, Using List
#This Function Will Return a list

def sub():
	str = "Python is A high-level language."
	x = 20
	return [str,x];

list = sub()
print(list)

#Example__003, Using Tuple

def sub():
	str = 'python is a high-level language'
	x = 20
	return (str, x);

tuple = sub()
print(tuple)
