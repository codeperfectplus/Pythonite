''' 
A function is  set of instructions like any other laguage. so writing the same code again and again.
we can use function and can keep our code DRY.
Don't Repeat.
These  Functions are called user-defined functions.
'''

def check_number(x):
	if (x % 2 == 0):
		print("Given Number Is Even")

	else:
		print("Given Number Is Odd")

check_number(7)
check_number(5)
check_number(4)
check_number(120)
# Try To Keep Your Code Dry as Possible.
	
def student_name(firstname,lastname):
	print(firstname, lastname)

student_name(firstname = 'Alex', lastname = 'Jean')