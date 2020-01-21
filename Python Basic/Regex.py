'''
@author : CodePerfectPlus
@Topic  : Regex
'''

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")
'''
findall	:Returns a list containing all matches
search	:Returns a Match object if there is a match anywhere in the string
split	:Returns a list where the string has been split at each match
sub	    :Replaces one or many matches with a string
'''