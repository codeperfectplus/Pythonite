'''

'''
print('\nNested Function\n')

def function_1(text):
	text = text

	def function_2():
		print(text)

	function_2()

if __name__ == '__main__':
	function_1('Welcome')

print('\n closure Function \n')

def function_1(text):
	text = text
	def function_2():
		print(text)
	return function_2

if __name__ == '__main__':
	myFunction = function_1('Thanks !')
	myFunction()

