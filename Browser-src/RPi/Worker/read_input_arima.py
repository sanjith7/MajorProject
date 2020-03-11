import pandas as pd
import numpy as np
paths = r'/Users/sanji/Desktop/mp/arima_input_datafiles/'
for i in range(1,40):
    df=pd.read_csv(paths+"data{0}.csv".format(i))
    df1 = df[-150:]
    history = list(df1['Total_load'].values)   # List of 150 values selected to be  given as input
    file = open('data{0}.txt'.format(i), 'w') #write to file
    for j in history:
        file.write(str(j)+' ')
    file.close()