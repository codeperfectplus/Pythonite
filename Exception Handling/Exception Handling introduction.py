'''
like other language, python also provides the runtime error via exception handling method with the help of try except.
'''
try:
	a = 3
	if a < 4:
		b = a/(a-3)
		print("Value of b =", b)

except(ZeroDivisionError, NameError):
	print("Error Occurred")