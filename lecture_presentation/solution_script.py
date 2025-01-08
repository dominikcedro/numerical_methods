"""
code downloaded from kaggle of user Ali Giray Çelenk
modified by Dominik Cedro
desc: Example use of polynomial regression.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline


def activate_polynomial(degree, ax):
    df = pd.read_csv('polynomial-regression.csv')
    X = df.drop(columns=['araba_max_hiz'])
    y = df['araba_max_hiz']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    polynomial_features = PolynomialFeatures(degree=degree)
    X_train_poly = polynomial_features.fit_transform(X_train)
    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    X_range_df = pd.DataFrame(X_range, columns=['araba_fiyat'])
    X_range_poly = polynomial_features.transform(X_range_df)
    y_range_pred = model.predict(X_range_poly)
    mse = mean_squared_error(y_test, model.predict(polynomial_features.transform(X_test)))
    r2 = r2_score(y_test, model.predict(polynomial_features.transform(X_test)))
    print(f'Degree: {degree}, MSE: {mse}, R²: {r2}')
    ax.plot(X_range, y_range_pred, label=f'Degree {degree}')


fig, ax = plt.subplots()
df = pd.read_csv('polynomial-regression.csv')
X = df.drop(columns=['araba_max_hiz'])
y = df['araba_max_hiz']
ax.scatter(X, y, color='blue', label='Actual')

for degree in range(1, 6):
    activate_polynomial(degree, ax)

ax.set_xlabel('X')
ax.set_ylabel('y')
ax.set_title('Polynomial Regression for Different Degrees')
ax.legend()
plt.show()