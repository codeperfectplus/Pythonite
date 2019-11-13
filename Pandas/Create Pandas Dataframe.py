# import pandas Library

import numpy as np
import pandas as pd 

df = pd.DataFrame(np.arange(0,20).reshape(5,4), index =['row1', 'row2', 'row3', 'row4', 'row5'], columns =['col1', 'col2', 'col3', 'col4'])
print(df)

df.loc['row1']
