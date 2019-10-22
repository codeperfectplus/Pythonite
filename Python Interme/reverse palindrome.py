''' 
python programe to check if  a string is palindrome
or not'''

x = "malayalam"
w = ""

for i in x:
	w = i + w
	if (x==w):
		print("Yes")
else:
		print("NO")