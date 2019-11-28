import random
from collections import Counter

#Take User Input for lower and Upper Range For auto Genrare 100 Number 
lower_range = int(input('Enter Lower Rnge :  ' ))
upper_range = int(input('Enter Upper Range : ' ))

#Create a empty List to Append Random Number to List
list0 = []

#create a random list to Lower range to Upper range
for i in range(100):
	x = random.randint(lower_range, upper_range)
	list0.append(x)

#count the NUmber most common 5
word_counts = Counter(list0)
for word, count in word_counts.most_common(5):
	print('The Number %d Comes %d times '  %(word,count))
