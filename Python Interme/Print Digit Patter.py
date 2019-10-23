# function to pritn the patter 

def pattern(n):

	for i in n:

		print("|" , end = "")

		print("* " * int(i))

n = "12345678"
pattern(n)