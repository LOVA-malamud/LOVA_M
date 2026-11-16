# קובצי תלויות

- `study.in` כולל קבוצות Data Science, מחברות, ראייה ממוחשבת, Backend ואיכות קוד. dmba ו־pygame דרושים לקוד שכבר קיים.
- קובצי `data-science.in`, `notebooks.in`, `vision.in`, `backend.in`, `quality.in` מתעדים את הכוונה לפי תחום; הם אינם רשימת כל התלויות העקיפות.
- `tensorflow-intel.in` ו־`torch-intel.in` מגדירים סביבות Deep Learning נפרדות ל־Intel, עם NumPy 1.26.4.
- שלושת קובצי `*-macos-intel-py312.txt` הם נעילות מלאות של הגרסאות שנפתרו והותקנו בפועל, כולל תלויות עקיפות וללא חבילות המערכת.

לשחזור זהה משתמשים בקובץ txt המתאים; לפתרון מחדש או לפלטפורמה אחרת מתחילים מקובץ in ובודקים תאימות. אין קובץ requirements אחד המערבב את שלוש הסביבות. קובץ requirements המקורי של DBSCAN נשמר במקומו ואינו מוחלף אוטומטית.

[הוראות שחזור, גרסאות ובדיקות](../PYTHON_ENVIRONMENT.md).
