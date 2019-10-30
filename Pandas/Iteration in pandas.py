'''
Iteration using for loop in python

'''


import pandas as pd

df = pd.read_csv('nba.csv')

for i, j in df.iterrows():
	print(i,j)
	print()

	
'''

# importing pandas module 
import pandas as pd 
	
# making data frame from csv file 
data = pd.read_csv("nba.csv") 

for key, value in data.iteritems(): 
	print(key, value) 
	print() 
'''