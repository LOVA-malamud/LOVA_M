# אשכולות לפי צפיפות — DBSCAN

[חזרה לתחום](../README.md) · [דף הבית](../../README.md)


[למידת מכונה](../README.md) · [אינדקס השיעורים](../../LESSONS_INDEX.md)

סימון התאריך המקורי: `2.9.27` — השנה דורשת אימות.

[קוד התרגיל](tirgul_DBSCAN.py) · [נתוני מעגלים](cluster_circles.csv) · [נתוני ירחים](cluster_moons.csv) · [תלויות](requirements.txt)

## הכנה במחשב חדש

מתוך תיקיית השיעור, ב־macOS או Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python tirgul_DBSCAN.py
```

ב־Windows מפעילים את הסביבה באמצעות `.venv\Scripts\Activate.ps1`. ב־VS Code בוחרים את מפרש Python מתוך `.venv` שבתיקיית השיעור. אם כבר יש סביבת לימודים עם התלויות הנדרשות, אפשר להשתמש בה.

סביבת `2.9.27/.venv` שהוזכרה בעבר הייתה נתיב מקומי במחשב המקורי; אינה חלק מהמאגר. נתוני התרגיל נשארו לצד הקוד כדי לשמור על נתיבים יחסיים.
