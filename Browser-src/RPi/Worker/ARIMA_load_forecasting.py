from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
from timeit import default_timer as timer
import pandas as pd
import glob
from datetime import datetime
from statsmodels.tsa.stattools import acf, pacf

for k in range(1,40): #Range to be replaced with the array of house numbers sent as input by the master node to the worker node.
    with open('data{0}.txt'.format(k)) as fp:
        data = [list(map(float, line.strip().split(' '))) for line in fp]
    fp.close()
    if len(data)!=0:
        history = data[0]   # List of 150 values selected to be  given as input
        size = int(len(data[0]) * 0.66)
        # train, test = df1['Total_load'][0:size], df1['Total_load'][size:]
        train = data[0][:size]
        predictions_roll_a = list()
        train_temp=list(train)
        # for t in range(len(test)):
        model = ARIMA(train_temp, order=(1,1,0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        pred = output[0]
        predictions_roll_a.append(pred)
        # obs = test[t]
        train_temp.append(pred[0]) # New ground truth to be appended as and when new data is entered.
        print('predicted=  ',pred)
        # dic["home{0}".format(j)]=pred # Save the demand predicted for each hour.
        file = open('result{0}.txt'.format(k), 'w')
        file.write(str(pred[0]))
        file.close()  




