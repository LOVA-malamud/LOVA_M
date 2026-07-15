import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

study_hours = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)

grades = np.array([55,60,66,73,80,85,89,92,94,95])

print(study_hours)

poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(study_hours)

print("x_poly=",x_poly)

model = LinearRegression()
model.fit(x_poly, grades)

print("model.coef_=",model.coef_)
print("model.intercept_=",model.intercept_)

predictions = model.predict(x_poly)
print("predictions=",predictions)

r2 = r2_score(grades, predictions)
print("R² Score:", r2)

mse = mean_squared_error(grades, predictions)
print("Mean Squared Error:", mse)

plt.scatter(study_hours, grades, color='red',)
plt.plot(study_hours, predictions,)
plt.grid(True)
plt.show()