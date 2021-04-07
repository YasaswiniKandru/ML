# Training the model using the above data for 10 different countries.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv("file.csv");
df = pd.DataFrame(data)
a=df.iloc[:,:-1].values  
b=df.iloc[:,-1:].values 

#Taking referenvce from https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
X_train, X_test, y_train, y_test = train_test_split(a, b, test_size=0.30, random_state=1)
reg = LinearRegression().fit(X_train, y_train)
r_sq = reg.score(X_train, y_train)

#2.9 and 15.4 are the beds count per 1000 people and percent of people above 65 in USA
usa_data = np.array([[2.9, 15.4]])
usa_mortality = reg.predict(usa_data)
print("Mortality rate for USA is",usa_mortality[0][0])


