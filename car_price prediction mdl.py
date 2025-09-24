import numpy as np
import pandas as pd
import tensorflow as tf
import os

dataset=pd.read_csv("car_price.csv")
pd.set_option("display.max_rows", None,"display.max_columns", None)
dataset.head()
dataset.shape
dataset.info()
dataset.describe()
dataset.isna().sum()
dataset['Age'] = 2020 - dataset['year']
dataset.drop('year',axis=1,inplace = True)
num_cols = ['Selling_Price(lacs)','Present_Price(lacs)','Kms_Driven','Age']
dataset.rename(columns = {'Selling_Price':'Selling_Price(lacs)','Present_Price':'Present_Price(lacs)','Owner':'Past_Owners'},inplace = True)
print('columns',dataset.columns)
df_main[df_main['Present_Price(lacs)'] > df_main['Present_Price(lacs)'].quantile(0.99)]
df_main[df_main['Selling_Price(lacs)'] > df_main['Selling_Price(lacs)'].quantile(0.99)]
dataset[dataset['Kms_Driven'] > dataset['Kms_Driven'].quantile(0.99)]
dataset.corr()['Selling_Price(lacs)']
dataset.pivot_table(values='Selling_Price(lacs)', index = 'Seller_Type', columns= 'Fuel_Type')
dataset.pivot_table(values='Selling_Price(lacs)', index = 'Seller_Type', columns= 'Transmission')
dataset.drop(labels='Car_Name',axis= 1, inplace = True)
dataset.head()
dataset = pd.get_dummies(data = dataset,drop_first=True)
dataset.head()
y = dataset['Selling_Price(lacs)']
X = dataset.drop('Selling_Price(lacs)',axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print("x train: ",X_train.shape)
print("x test: ",X_test.shape)
print("y train: ",y_train.shape)
print("y test: ",y_test.shape)
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score

CV = []
R2_train = []
R2_test = []


def car_pred_model(model, model_name):
    # Training model
    model.fit(X_train, y_train)

    # R2 score of train set
    y_pred_train = model.predict(X_train)
    R2_train_model = r2_score(y_train, y_pred_train)
    R2_train.append(round(R2_train_model, 2))

    # R2 score of test set
    y_pred_test = model.predict(X_test)
    R2_test_model = r2_score(y_test, y_pred_test)
    R2_test.append(round(R2_test_model, 2))

    # R2 mean of train set using Cross validation
    cross_val = cross_val_score(model, X_train, y_train, cv=5)
    cv_mean = cross_val.mean()
    CV.append(round(cv_mean, 2))

    # Printing results
    print("Train R2-score :", round(R2_train_model, 2))
    print("Test R2-score :", round(R2_test_model, 2))
    print("Train CV scores :", cross_val)
    print("Train CV mean :", round(cv_mean, 2))
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
car_pred_model(lr,"Linear_regressor.pkl")
from sklearn.linear_model import Ridge
from sklearn.model_selection import RandomizedSearchCV

# Creating Ridge model object
rg = Ridge()
# range of alpha
alpha = np.logspace(-3,3,num=14)

# Creating RandomizedSearchCV to find the best estimator of hyperparameter
rg_rs = RandomizedSearchCV(estimator = rg, param_distributions = dict(alpha=alpha))

car_pred_model(rg_rs,"ridge.pkl")
from sklearn.linear_model import Lasso
from sklearn.model_selection import RandomizedSearchCV

ls = Lasso()
alpha = np.logspace(-3,3,num=14) # range for alpha

ls_rs = RandomizedSearchCV(estimator = ls, param_distributions = dict(alpha=alpha))
car_pred_model(ls_rs,"lasso.pkl")
Technique = ["LinearRegression","Ridge","Lasso","RandomForestRegressor","GradientBoostingRegressor"]
results=pd.DataFrame({'Model': Technique,'R Squared(Train)': R2_train,'R Squared(Test)': R2_test,'CV score mean(Train)': CV})
display(results)