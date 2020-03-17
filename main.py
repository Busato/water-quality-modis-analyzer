import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from pprint import pprint

#%matplotlib inline

dataset = pd.read_csv("./data/Dados_tratados.csv")
dataset = dataset.astype(float)

#
X = dataset[["Banda 1", "Banda 2"]].values
y = dataset["Chl-a (mg/L)"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=0
)

regressor = LinearRegression()
regressor.fit(X_train, y_train)  # training the algorithm

y_pred = regressor.predict(X_test)

df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
pprint(df)
