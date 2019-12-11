import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = int(input("Enter Length to Genrate Password:\n"))
if passlen<6:
    print("Choose 6 or Greater")
else:
    p =  "".join(random.sample(s,passlen ))
    print (p)