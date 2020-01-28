'''
 import pandas Library
Pandas is Python Library for dataframe, Like to read write and load data in dataframe.
Pandas is must known library for Data Science.
'''
import numpy as np
import pandas as pd 

df = pd.DataFrame(np.arange(0,20).reshape(5,4), index =['row1', 'row2', 'row3', 'row4', 'row5'], columns =['col1', 'col2', 'col3', 'col4'])
print(df)

df.loc['row1']
