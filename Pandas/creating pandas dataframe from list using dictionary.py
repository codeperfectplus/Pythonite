'''
Cretae Data Frame Using Dictionary in python.
Dictionary is a (key-value) Pair Data Type in python.
'''

import pandas as pd 

dict ={     'Name':['john', 'joe', 'Alex', 'Iris', 'berry'],
            'degree':['B.Sc', 'M.Sc', 'M.A', 'B.A', 'C.A']  }

df =pd.DataFrame(dict)
print(df)