import pandas as pd
import sqlalchemy

engine=sqlalchemy.create_engine('postgresql+psycopg2://postgres:8868028382@127.0.0.1:5432/localbase_1')

df=pd.read_excel('home_equipments.xlsx')
df.to_sql('home_equipments',con=engine,if_exists='append',index=False)
