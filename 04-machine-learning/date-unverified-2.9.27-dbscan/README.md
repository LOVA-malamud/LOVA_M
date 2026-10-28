# סביבת Python לתרגיל DBSCAN

הספריות של התרגיל מותקנות בסביבה וירטואלית מקומית שנשארה ב־`2.9.27/.venv` בשורש המאגר ומופיעות עם גרסאות קבועות בקובץ `requirements.txt`.

## הפעלה

מתוך Terminal בתיקייה הזאת:

```bash
source ../../2.9.27/.venv/bin/activate
python tirgul_DBSCAN.py
```

בסיום העבודה אפשר לצאת מהסביבה:

```bash
deactivate
```

## שחזור הסביבה בעתיד

אם `.venv` נמחקה או עוברים למחשב אחר:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

ב־VS Code, כאשר פותחים את שורש המאגר, יש לבחור כמפרש Python את:

```text
2.9.27/.venv/bin/python
```

לאחר ההעברה, הסביבה הישנה נשארה בנתיב המקורי כדי לא לשבור scripts של venv. מומלץ ליצור כאן סביבה חדשה לפי הוראות השחזור.
