import pandas as pd
import sqlalchemy

engine=sqlalchemy.create_engine('postgresql+psycopg2://postgres:8868028382@127.0.0.1:5432/Database_001')

df=pd.read_excel('example_1.xlsx')
df.to_sql('home_equipments',con=engine,if_exists='append',index=False)
