

import pandas as pd

data = ['train_text','val_text','test_text']

#f = open('classes.txt',mode='at')

for d in data:
    data = pd.read_csv(d+'.csv')
    for col in data.columns[:-1]:
        #f.write(col+'\n')
        c = len([i for i in data[col] if i==1])
        print(col,d,c)



