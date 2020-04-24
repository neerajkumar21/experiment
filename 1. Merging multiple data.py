import pandas as pd
import os

# Merging Data of Different sales in months
files = [file for file in os.listdir('./Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data')]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv('./Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/'+file)
    all_months_data = pd.concat([all_months_data, df])
all_months_data.to_csv('./all_data.csv', index=False)

# Reading new created data
all_data = pd.read_csv('./all_data.csv')
print(all_data.head())
