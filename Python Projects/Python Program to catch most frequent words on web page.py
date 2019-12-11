
import requests 
from bs4 import BeautifulSoup 
import operator 
from collections import Counter 

'''Function defining the web-crawler/core 
spider, which will fetch information from
 a given website, and push the contents to 
the second function clean_wordlist()'''
def start(url): 


	wordlist = [] 
	source_code = requests.get(url).text 

	# BeautifulSoup object which will 
	# ping the requested url for data 
	soup = BeautifulSoup(source_code, 'html.parser') 

	# Text in given web-page is stored under 
	# the <div> tags with class <entry-content> 
	for each_text in soup.findAll('div', {'class':'entry-content'}): 
		content = each_text.text 

		# use split() to break the sentence into 
		# words and convert them into lowercase 
		words = content.lower().split() 
		
		for each_word in words: 
			wordlist.append(each_word) 
		clean_wordlist(wordlist) 

# Function removes any unwanted symbols 
def clean_wordlist(wordlist): 
	
	clean_list =[] 
	for word in wordlist: 
		symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
		
		for i in range (0, len(symbols)):
 			word = word.replace(symbols[i], '') 
			
		if len(word) > 0: 
			clean_list.append(word) 
	create_dictionary(clean_list) 

# Creates a dictionary conatining each word's 
# count and top_20 ocuuring words 
def create_dictionary(clean_list): 
	word_count = {} 
	
	for word in clean_list: 
		if word in word_count: 
			word_count[word] += 1
		else: 
			word_count[word] = 1
			
	''' To get count of each word in 
		the crawled page --> 
		
	# operator.itemgetter() takes one 
	# parameter either 1(denotes keys) 
	# or 0 (denotes corresponding values) 
	
	for key, value in sorted(word_count.items(), 
					key = operator.itemgetter(1)): 
		print ("% s : % s " % (key, value)) 
		
	<-- '''

	
	c = Counter(word_count) 
	
	# returns the most occuring elements 
	top = c.most_common(10) 
	print(top) 

# Driver code 
if __name__ == '__main__': 
	start("https://www.geeksforgeeks.org/send-message-to-fb-friend-using-python/") 
