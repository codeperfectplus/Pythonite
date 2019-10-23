# import pandas Library

import pandas as pd 

# create a pandas dataframe using list, we can also use Dict
list_01 = ['Pandas', 'Numpy','Scipy' ,'Machine Learning', 'Deep Learning', 'Reinforcement Learning']
 
#now load data in df variable
df = pd.DataFrame(list_01)

#show the data
print(df)