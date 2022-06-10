import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

url = 'https://raw.githubusercontent.com/data-max-hq/workshop-mlops-epoka/main/1_train/data/winequality-red.csv'
response = requests.get(url)

with open('./data/winequality-red.csv', 'wb') as f:
    f.write(response.content)

wine_data = pd.read_csv('./data/winequality-red.csv')

X = wine_data.drop('quality', axis=1)
y = wine_data['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=101, train_size=0.8)

regressor = LinearRegression()
regressor.fit(X_train,y_train)

with open('../2_models/model.pkl', 'wb') as file:
    pickle.dump(regressor, file)
