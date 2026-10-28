# הרצה ותלויות

## בסיסי Python

Python 3.10+ נדרש לתחביר הקיים. רוב תרגילי הבסיס משתמשים בספרייה הסטנדרטית בלבד. הריצו קובץ אחד בכל פעם. חלקם אינטראקטיביים; אין לייבא את כולם כתוכנית אחת.

## סביבות קיימות

`.venv/`, `.venv-tf/` ו־`2.9.27/.venv/` נשמרו בנתיבים המקוריים, כולל קבצים שלא היו ב־Git. סביבות venv אינן ניידות: סקריפטים פנימיים עשויים לכלול נתיבים מוחלטים, ולכן סביבת DBSCAN לא הועברה עם השיעור. התיקייה הישנה `2.9.27/` מכילה כעת רק סביבה מקומית מוחרגת.

להרצת KNN משורש המאגר עם הסביבה הקיימת:

```bash
2.9.27/.venv/bin/python 04-machine-learning/date-unverified-9.9.27-knn/tirgul_00.py
```

ל־DBSCAN יש [requirements.txt מקורי](../04-machine-learning/date-unverified-2.9.27-dbscan/requirements.txt) עם גרסאות קבועות. מומלץ לשחזר סביבה חדשה **בתיקיית השיעור**:

```bash
cd 04-machine-learning/date-unverified-2.9.27-dbscan
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python tirgul_DBSCAN.py
```

## תלויות לפי תחום

| תחום | imports שנמצאו |
|---|---|
| NumPy | numpy |
| Pandas | pandas |
| ML וגרפים | numpy, pandas, scikit-learn, matplotlib, seaborn |
| מחברת פולינומית | גם dmba ו־IPython |
| כימות תמונה | גם Pillow |
| Deep Learning | tensorflow, numpy, scikit-learn |
| משחק | pygame |
| מחברות | jupyter/ipykernel; IPython |
| כלי דיבור | פקודת say של macOS |

זוהי מפת imports, לא הבטחת תאימות של גרסאות. לא נוצר קובץ requirements כללי עם גרסאות מנוחשות. התקינו רק את תלויות השיעור בסביבה נפרדת. לא הותקנו או שודרגו חבילות במסגרת הארגון.

## מחברות ונתיבים

מפעילים kernel עם תיקיית העבודה של המחברת. מחברת Pandas המקומית מפנה ל־`../../datasets/local-only/Churn_Modelling.csv`. יתר המחברות אינן קוראות קובצי נתונים מקומיים. יש במחברות טעויות וקטעים לא גמורים שתועדו בדוח האימות; לא תוקנה הלוגיקה הלימודית.

DBSCAN משתמש ב־`Path(__file__)`, וכך גם טעינת התמונה ב־KMeans ותמונות המשחק לאחר תיקון הנתיבים. לא נמצאו imports בין קובצי לימוד מקומיים.

## SQL

שמרו את סדר התרגילים בכל שיעור: לדוגמה Exercise_01 יוצר את sales, והשאר משתמשים בטבלה זו. תרגילי Netflix דורשים טבלה חיצונית שאינה במאגר. אין להריץ על מסד אישי או מסד של פרויקט אחר.
