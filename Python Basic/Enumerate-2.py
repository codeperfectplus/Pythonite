'''
@author : CodePerfectPlus
@Topic  : Enumerate Extension
'''

my_list = ["apples","Mangoes", "Orange"]
count =0

#way1
for element in my_list:
    print(element)
    if count ==1:
        print("Count is 1")

#way 2
for x in range(len(my_list)):
    print(my_list[x])
    if x==1:
        print("X Is 1")

#way 3
# Enumerate function use for loop and count and give output with INDEXING
for x, element in enumerate(my_list):
    print(x, element)
