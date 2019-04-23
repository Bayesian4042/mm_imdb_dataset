


import pandas as pd


data = pd.read_csv('test_text.csv')

for col in data.columns:
        print(col)
        print(data[col].unique())

