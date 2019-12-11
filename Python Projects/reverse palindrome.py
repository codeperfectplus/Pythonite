''' 
python programe to check if  a string is palindrome
or not'''

x = "211112"
w = ""

# save string x to a new new variable and compare them
for i in x:
	w = i + w
	#print(w)
	if (x==w):
		print("Yes")
		break

else:
	print("No")