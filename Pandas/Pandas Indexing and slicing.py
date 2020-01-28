# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:42:13 2019

@author: CodePerfectPlus
@Topic : Indexing and Selecting Data with Pandas 
"""
import pandas as pd
df = pd.read_csv('nba.csv', index_col = "Name")

first = df[["Age" ,"College", "Salary"]]
print(first)
