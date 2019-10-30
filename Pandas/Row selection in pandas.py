import pandas as pd 

df = pd.read_csv('nba.csv', index_col='Name')

first = df.loc['Avery Bradley']
second = df.loc['R.J. Hunter']

print(first, '\n\n\n\n',second)