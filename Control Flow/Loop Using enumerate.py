'''Loop Using enumerate
enumerate is used to loop through the containers printing the index number along
 with the value presentin the particular index.
'''

# using enumerate
for key, value in enumerate( ['The', 'Quick', 'Brown', 'Fox']):
	print(key, value)

#zip is used to combine 2 similar containers printing the values sequentinally.
#using zip

question = ['name', 'colour', 'shape']
answer = ['appple', 'red', 'a circle']

for question, answer in zip(question,answer):
	print('what is your {}? I am {}'.format(question, answer))

print()

'''Using Sorted(s):a
sorted() is used to print the container is sorteed order. it doesn't sort the conatiner, 
but just prints the container in sorted order for 1 instance.
use of set() can be combined to remove duplicates
'''

list_01 = [1, 3, 6, 4, 7, 1, 2, 3, 1, 7, 6]
print("The list in sorted order is : ")
for i in sorted(list_01):
	print(i, end ='')	

print('\n') # only for space in output
print("List Is in Order Without Duplicates Value ")
for i in sorted(set(list_01)):
	print(i, end ='')
print()
# using Reversed()

print('The List in Reversed order is')
for i in reversed(list_01):
	print(i, end='')
print()
# using range function reversed()
for i in reversed(range(1, 10, 3)):
	print (i)

for i in reversed(range(2, 100, 7)):
	print(i)

