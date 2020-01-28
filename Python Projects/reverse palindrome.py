''' 
Python Programe To Check if  a String is Palindrome or Not
'''

check1 = input("Choose Your Input For Check Palindrome\n For Integer Type --> i \n For Word Type   -->s\n").lower()
for i range(1,3):
	if check1 == 's':
		x = input("Enter Your Word Here :\n").lower()
	elif check1 == 'i':
		x = input("Enter Your Number Here :\n")
	else:
		print("Please Enter I or S only")

	w = "" # Empty String to save Reverse value in it.

#save string x to a new new variable and compare them
	for i in x:
		w = i + w   # save new value to w 
		if (x==w):
			print("Yes")
			break
	else:
		print("No")