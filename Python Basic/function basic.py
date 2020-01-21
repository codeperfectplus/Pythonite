'''
@author : CodePerfectPlus
@Topic  : Funtion Basic
'''

def welcome(greeting):
	return "Hello and {}".format(greeting)

name = input("Enter Your Name Below : \n")
age = int(input("Enter Your Age Below :\n"))
print(welcome("Welcome"),'{}'.format(name))
if age < 18:
	print("You Are Not Eligible For Voting")

else :
	print("You Are Eligible For Voting!")

