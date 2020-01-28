'''
A counter turns a sequence of values into a defaultdict(int)-like object mapping keys to counts. we will use 
it to create Histogram
'''
from collections import Counter
document = (10,1,10,5,7,4,1,1,10,10,9,10,1,3,9,9,4,8,6,7,3,6,7,3,10,5,3,10,4,6,8,10,5,5,10,10,9,10,10,8,7,7,10,8,
6,4,6,1,9,10,2,3,9,2,3,8,1,7,3,10,6,6,9,6,7,9)
word_counts = Counter(document)
for word, count in word_counts.most_common(10):
	print('The Number %d Comes %d times '  %(word,count))