def reverse(s):
	return s[::-1]

def isPalindrome(s):
	#calling reverse function
	rev=reverse(s)

    #checking if both string are equal or not
	if (s == rev):
		return True
	return False

	#Driver code
s="KADAK"
ans=isPalindrome(s)

if ans == 1:
		print("Yes")
else:
		print("NO")