"""Import csv file and create table in PostgreSQL database"""

import pandas as pd
import numpy as np
from sqlalchemy import create_engine

#read car_prices csv file
df = pd.read_csv('C:/Users/auhro/Downloads/car_prices.csv')
df

#connect and store the csv file to postgreSQL database
engine = create_engine('postgresql://postgres:siravit1220@localhost:5432/postgres')

table_name = 'carprices'
df.to_sql(table_name, engine, if_exists='replace', index=False)

query = f"SELECT * FROM {table_name};"
result_df = pd.read_sql_query(query, engine)
print(result_df)
result_df