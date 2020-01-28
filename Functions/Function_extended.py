'''
Check you name contain vowel Or Not Using python intersection function.
'''

def names():
	name = input("Please! Enter Your Name\n")     #Enter Your name 

	if set('aeiou').intersection(name.lower()):
		print("Your Name Contains a vowel")
	else :
		print("Your Name doesn't have a vowel")

	for letter in name:  # For Loop To Check Letter
		print(letter)
	

names()