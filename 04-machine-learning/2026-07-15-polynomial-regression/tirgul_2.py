import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

speed = np.array([20,30,40,50,60,70,80,90,100,110]).reshape(-1,1)

fuel_consumption = np.array([9.8,8.4,7.2,6.3,5.9,6.0,6.5,7.4,8.8,10.7])

poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(speed)

model = LinearRegression()
model.fit(x_poly, fuel_consumption)
model.coef_ = model.coef_
model.intercept_ = model.intercept_
predictions = model.predict(x_poly)
r2 = r2_score(fuel_consumption, predictions)
mse = mean_squared_error(fuel_consumption, predictions)

plt.scatter(speed, fuel_consumption, color='red',)
plt.plot(speed, predictions, color='blue')
plt.grid(True)
plt.show()