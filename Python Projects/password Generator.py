'''
Password Generation Using Random Function in Python.
Random is python module to generate random value or select random vlaue from list, string.
'''
import random
list = []

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = int(input("Enter Length to Genrate Password:\n"))
n = int(input("How Many Password Your Want to print :\n"))
'''
passlen = Length of password . Password Length should be greater than 8
n = Number of password for your project
s = symbol and letter for auto-generation password
'''
for i in range(n):
    if passlen<8:   
        print("Choose 8 or Greater")
    else:
        p =  "".join(random.sample(s,passlen))
        list.append(p)  # append Password in list 
print(list)
