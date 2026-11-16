# פתרון בסגנון דוגמת sklearn בשיעור 15, עם חישוב המרחקים שנלמד באותו שיעור.
# מחברת המורה:
# https://github.com/pythonai211225-rgb/02.08.2026/blob/main/knn_02_08_2026.ipynb

import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier


######################### הנתונים
members = np.array(['A', 'B'])
ages = np.array([50, 29])
salaries = np.array([5200, 8000])
renewed = np.array(['No', 'Yes'])

# כמו בדוגמת הפירות: כל שורה היא דוגמה, וכל עמודה היא תכונה.
# העמודה הראשונה היא גיל, והשנייה היא שכר.
X = np.column_stack((ages, salaries))
y = renewed

# שתי סוגריים מרובעים: רשומה אחת עם שתי תכונות.
new_member = np.array([[30, 6000]])
k = 1


######################### סעיף א - סיווג לפני נרמול
# הגדרת המודל כמו במחברת המורה, עם k=1 לפי השאלה.
# כשיש רק שכן אחד, weights='distance' אינו משנה את הסיווג.
model = KNeighborsClassifier(n_neighbors=k, weights='distance')
model.fit(X, y)

prediction = model.predict(new_member)

# מציגים גם את המרחקים כדי להבין מדוע המודל בחר את התשובה.
# np.linalg.norm מחשב את שורש סכום ריבועי ההפרשים, כפי שנלמד בשיעור.
print('(a) Before normalization')
for i in range(len(X)):
    diff_arr = X[i] - new_member[0]
    dist = np.linalg.norm(diff_arr)
    print(f'{members[i]}: distance={dist:.5f}, renewed={y[i]}')

print('Prediction:', prediction[0])


######################### סעיף ב - נרמול וסיווג מחדש
# נוסחת הנרמול מהשיעור: (x - Xmin) / (Xmax - Xmin)
# גיל: (age - 20) / (60 - 20)
# שכר: (salary - 4000) / (12000 - 4000)

# התאמה לנתוני השאלה: נתונים הגבולות של כל מסד הנתונים.
# השורה הראשונה מכילה מינימום לכל עמודה, והשנייה מקסימום לכל עמודה.
# אלה גבולות לנרמול בלבד, ולא חברים נוספים לאימון מודל KNN.
database_limits = np.array([[20, 4000], [60, 12000]])

scaler = MinMaxScaler()

# fit_transform לומד את הגבולות וגם מנרמל אותם.
# כאן דרושה רק למידת הגבולות; את הפלט של שתי שורות הגבול אין צורך לשמור.
# אם נבצע fit_transform על X בלבד, נקבל גבולות שונים מאלה שבשאלה.
scaler.fit_transform(database_limits)

# transform משתמש באותם גבולות עבור A, B והחבר החדש.
X_scaled = scaler.transform(X)
new_member_scaled = scaler.transform(new_member)

print('\n(b) After min-max normalization')
print('X_scaled (rows: A, B; columns: age, salary):')
print(X_scaled)
print('new_member_scaled:', new_member_scaled)

# מאחסנים במודל את הנתונים המנורמלים עם אותם הסיווגים.
model.fit(X_scaled, y)
prediction_scaled = model.predict(new_member_scaled)

for i in range(len(X_scaled)):
    diff_arr = X_scaled[i] - new_member_scaled[0]
    dist = np.linalg.norm(diff_arr)
    print(f'{members[i]}: distance={dist:.5f}, renewed={y[i]}')

print('Prediction:', prediction_scaled[0])


######################### סעיף ג - הסבר למבחן
print('\n(c) הסבר')
print('לפני הנרמול, הפרשי השכר גדולים בהרבה מהפרשי הגיל ושולטים במרחק.')
print('לכן A קרוב יותר, והתחזית היא No.')
print('אחרי הנרמול, הגיל והשכר נמדדים ביחס לטווח של כל עמודה.')
print('הגיל של החבר החדש קרוב מאוד לגיל של B, וכעת המרחק הכולל ל-B קטן יותר.')
print('לכן לאחר הנרמול התחזית היא Yes.')
