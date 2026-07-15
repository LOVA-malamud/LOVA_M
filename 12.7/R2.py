import numpy as np
from sklearn.metrics import r2_score

# 1. הגדרת המערכים לפי הטבלה מהצילום מסך
y = np.array([2, 3, 7])
y_pred = np.array([2.5, 3.0, 6.5])

# 2. חישוב y_bar (הממוצע של y)
y_bar = np.mean(y)

# 3. חישוב SST ו-SSE בעזרת numpy
sst = np.sum((y - y_bar) ** 2)
sse = np.sum((y - y_pred) ** 2)

# 4. חישוב ה-R² בעזרת הפונקציה r2_score מתוך sklearn
r2 = r2_score(y, y_pred)

# הדפסת כל התוצאות הנדרשות ב-Goal
print(f"y_bar (Y-bar): {y_bar}")
print(f"SST:           {sst}")
print(f"SSE:           {sse}")
print(f"R² Score:      {r2:.4f}")