''' 
A function is  set of instructions like any other laguage. so writing the same code again and again.
we can use function and can keep our code DRY.
Don't Repeat.
These  Functions are called user-defined functions.
'''

def check_number(x):
	if (x % 2 == 0):         # checking Divisibility by 2
		print("Given Number Is Even")   # 2,4,6,8....

	else:
		print("Given Number Is Odd")   #1,3,5,7...

check_number(7)
check_number(5)
check_number(4)
check_number(120)
# Try To Keep Your Code Dry as Possible.
	
def student_name(firstname,lastname):
	print(firstname, lastname)


student_name("john","adam")
student_name(lastname = 'Jean',firstname = 'Alex',)