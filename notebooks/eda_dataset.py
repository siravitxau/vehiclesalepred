"""Exploratory Data Analysis"""

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import Levenshtein
from fuzzywuzzy import fuzz

# connect and query dataset from PostgreSQL database
engine = create_engine('postgresql://postgres:siravit1220@localhost:5432/postgres')
table_name = 'carprices'
query = f"SELECT * FROM {table_name};"
df = pd.read_sql_query(query, engine)
df.head()

# information in the dataset
df.info()

# list of car manufacturer
list = df['make'].unique()
list # unsorted and contain None
valid_list = [make for make in list if make is not None]
valid_list # Not null list
list_sorted = sorted(valid_list)
list_sorted # car manufacturer name are not in the same way (Uppercase, Lowercase, Short name, Wrong name)

# use Fuzzy Matching to find similar car manufacturer that may be the same name
def find_similar_brand(list_sorted):
    similar_brand = {}
    for i in range(len(list_sorted)):
        for j in range(i+1, len(list_sorted)):
            brand_1 = list_sorted[i]
            brand_2 = list_sorted[j]
            similarity_ratio = fuzz.ratio(brand_1.lower(), brand_2.lower())
            if similarity_ratio >= 85: # adjustable 
                if brand_1 not in similar_brand:
                    similar_brand[brand_1] = [brand_2]
                else:
                    similar_brand[brand_1].append(brand_2)
    return similar_brand

similar_brand_list = find_similar_brand(list_sorted)
similar_brand_list # dictionary of original brand with similar brand (threshold=1)
manufacturer_brand_list = [key for key in similar_brand_list]
manufacturer_brand_list # completed list of car manufacturer !
