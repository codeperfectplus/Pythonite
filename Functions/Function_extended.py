def names():
	name = str(input("Please! Enter Your Name"))

	if set('aeiou').intersection(name.lower()):
		print("Your Name Contains a vowel")
	else :
		print("Your Name doesn't have a vowel")

	for letter in names:
		print(letter)

names()