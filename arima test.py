# ARIMA Model
# Best paramaters (1,0,1)
# differenced series then invert the differenced series

# Get Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from statsmodels.tsa.stattools import acf, pacf

# Load data and set column date as index
url = 'https://raw.githubusercontent.com/ariessa/Gold_Prediction_Price_Model_Dataset/master/GPP_Model_4_Daily_Dataset.csv?token=ACQXPI44SXRP3I3IXDRNSXK5SWYHO'
data = pd.read_csv(url, index_col=0)

# Drop rows with missing values
data = data.dropna()

# # Reset index
# data = data.reset_index(drop=True)

# Features
data['1_Day_Moving_Average'] = data['Price'].shift(1).rolling(window=1).mean()
data['2_Days_Moving_Average'] = data['Price'].shift(1).rolling(window=2).mean()
data.head()

# Drop any rows with missing values
data = data.dropna()
data

# # # Reset index
# # data = data.reset_index(drop=True)

# Features, column that influences prediction target
X = data[['1_Day_Moving_Average', '2_Days_Moving_Average']]

# Prediction target, the column to predict
y = data['Price']


# create a differenced series
def difference(dataset, interval=1):
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return np.array(diff)


# invert differenced value
def inverse_difference(history, yhat, interval=1):
    return yhat + history[-interval]


X

# Convert to 1D array
X = X.iloc[:, 0].values

# Seasonal difference
days_in_year = 30
differenced = difference(X, days_in_year)

# Check stationarity
result = adfuller(differenced)
# print('ADF Statistic: {}'.format(result[0]))
# print('p-value: {}'.format(result[1]))
# print('Critical Values: ')
# for key, value in result[4].items():
#   print('\t{0}: {1}'.format(key, round(value, 3)))

# Fit model
model = ARIMA(differenced, order=(2, 0, 2))
model_fit = model.fit(disp=0)
# print(model_fit.summary())

# Multi-step out-of-sample forecast
start_index = len(differenced)
end_index = start_index + 19
forecast = model_fit.predict(start=start_index, end=end_index)

# Invert the differenced forecast to something usable
history = [x for x in X]
prediction = []
day = 1
for yhat in forecast:
    inverted = inverse_difference(history, yhat, days_in_year)
    #   print('Day %d: %f' % (day, inverted))
    history.append(inverted)
    prediction.append(inverted)
    day += 1

del prediction[0:2]

# Load data of gold prices
compare_url = 'https://raw.githubusercontent.com/ariessa/Gold_Prediction_Price_Model_Dataset/master/compare_gold_price.csv?token=ACQXPI3RN2LBEVEUOH56UF25SWYP2'
compare_data = pd.read_csv(compare_url)
# compare_data['Price'] = pd.to_numeric(compare_data['Price'], downcast='float')
compare_data['Price'] = compare_data['Price'].apply(lambda x: float(x.split()[0].replace(',', '')))
compare_data['Price'] = compare_data['Price'].astype(float)

pred = pd.Series(prediction)

compare_data['Prediction'] = pred
compare_data.set_index('Date', inplace=True)
compare_data
# compare_data.plot.line(title ="Comparison of Actual vs Predicted Gold Price", figsize=(16, 5))


# Mean Squared Error
error = mean_absolute_error(compare_data['Price'], compare_data['Prediction'])
print("MAE: %.3f" % error)