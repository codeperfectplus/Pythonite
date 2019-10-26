'''
args and kwargs in python.
'''
#Example__001
print("\nExample__001\n")

def sub(*args):
	for arg in args:
		print(arg)

sub('Python is a High Level ','Programing Language.')

#Example__002
print("\nExample__002\n")

def sub(arg1, *args):
	print("Hello, Programer :",arg1)
	for arg in args:
		print("Your Favourite Language :",arg)

sub("HI", "Python And Java")

#Example__003
print("\nExample__003\n")
def sub(**kwargs):
	for key, value in kwargs.items():
		print("%s=%s" %(key, value))

sub(python ='Machine Learning',Javascript ='Back-end')


#Example__004
print("\nExample__004\n")
#Using *args and **kwargs to call a function

def sub(arg1, arg2):
	print("arg1 :", arg1)
	print("arg2 :", arg2)

args = ("Hello", "World")
sub(*args)

kwargs = {'arg1' : 'Hello','arg2' : 'world'}
sub(**kwargs)

#Example__005
print('\nExample__005\n')
