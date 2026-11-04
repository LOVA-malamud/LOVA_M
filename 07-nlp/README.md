# שיעורי בית ב־NLP ו־spaCy — 04.11.2026

הפתרונות נבדקים מול [המטלה הרשמית של המורה](https://github.com/pythonai211225-rgb/nlp/blob/main/Kc-NLP-hw.md).
להסבר על סביבת העבודה ו־Tokens: [מבוא לשיעור](2026-11-04-spacy-introduction/README.md).

| תרגיל | נושא |
|---|---|
| [01](exercise_01.py) | הדפסת ישויות ושמות הסוגים שלהן |
| [02](exercise_02.py) | פונקציה שמדפיסה רק ישויות מסוג PERSON |
| [03](exercise_03.py) | מילה וצורת הבסיס שלה — lemma |
| [04](exercise_04.py) | החזרת רשימת מילים ללא מילות עצירה, פיסוק ורווחים |
| [05](exercise_05.py) | סימון powerful כמילת עצירה ובדיקת is_stop |
| [06](exercise_06.py) | PhraseMatcher שאינו מבחין בין אותיות גדולות לקטנות |
| [07](exercise_07.py) | פונקציה שמדפיסה חלקי דיבר והסברים |
| [08](exercise_08.py) | קלט משתמש, חלקי דיבר ותרשים תלות תחבירית באמצעות displaCy |

## סביבת עבודה והרצה

במחשב זה כבר מותקנת סביבת Conda בשם `spacy_env`: Python 3.11.13, spaCy 3.8.18 והמודל `en_core_web_sm` 3.8.0. אין צורך בהתקנה חוזרת. גרסאות התלויות והוראות שחזור מופיעות ב־[requirements.txt](2026-11-04-spacy-introduction/requirements.txt) ובמדריך המבוא.

משורש `LOVA_M`, בטרמינל של VS Code:

```bash
/opt/anaconda3/envs/spacy_env/bin/python 07-nlp/exercise_01.py
/opt/anaconda3/envs/spacy_env/bin/python 07-nlp/exercise_08.py
```

אפשר להחליף את המספר כדי להריץ כל אחד משמונת התרגילים. תרגיל 8 ממתין למשפט באנגלית. לאחר הריצה פתח בדפדפן את `07-nlp/exercise_08_visualization.html` כדי לראות את התרשים; `render` מחזיר HTML ובקובץ Python רגיל אין תצוגת Notebook אוטומטית. קלט ריק מציג הודעה ואינו משנה תרשים קודם.

הרצה עם קלט אוטומטי, בלי להמתין להקלדה:

```bash
printf '%s\n' 'The cat sat on the mat.' | /opt/anaconda3/envs/spacy_env/bin/python 07-nlp/exercise_08.py
```

ב־VS Code בחר **Python: Select Interpreter → spacy_env**. למחברת בחר Kernel בשם **Python nov-04 (spacy_env)**.

## בדיקות

```bash
/opt/anaconda3/envs/spacy_env/bin/python -B -m unittest discover -s 07-nlp -p test_homework.py -v
/opt/anaconda3/envs/spacy_env/bin/python -m pip check
```

[הבדיקות](test_homework.py) מריצות את כל שמונת הקבצים ומשוות לדוגמאות המורה. הן בודקות גם קלט ללא אנשים, קלט ריק, פיסוק ורווחים, התאמת ביטוי באותיות גדולות, וחזרה על ביטויים. לתרגיל 8 מוזן קלט אוטומטי, ונבדקים עמוד HTML, מבנה SVG, מילים, קשתות, ראשי חצים ותוויות תלות תקינות. הרצות ה־HTML מתבצעות בתיקייה זמנית כדי לשמור על התרשים המקומי הקיים.

תוצאת האימות ב־04.11.2026: **14 בדיקות עברו**, כולל הרצת כל שמונת התרגילים ובדיקת SVG. גם `pip check` עבר ללא תלויות שבורות.

## הערות על הפלט ועל Pylance

- תוצאות ניתוח שפה עשויות להשתנות עם גרסת המודל; הבדיקות מקבעות את הציפיות לסביבה המתועדת. `7am` מחולק כאן לשני Tokens, והפיסוק מודפס בתרגילי lemma ו־POS.
- שינוי `nlp.vocab["powerful"].is_stop` בתרגיל 5 חל על האיות הזה במילון של אותו תהליך. הוא אינו משנה את התקנת המודל או את התרגילים האחרים.
- בעורך נצפתה אזהרת `reportPrivateImportUsage` על `spacy.explain` בתרגילים 7 ו־8. נבדקו קוד הספרייה, ההרצה ו־[התיעוד הרשמי](https://spacy.io/api/top-level#explain): הפונקציה ציבורית ופועלת. הקריאה נשמרה כפי שנלמדה; לא הושבתו בדיקות Pylance ולא שונתה הספרייה כדי להסתיר את האזהרה.
- קובץ ההמחשה הוא פלט שניתן ליצור מחדש ועשוי להכיל קלט אישי. הוא מוחרג מ־Git, יחד עם סביבות Python ומטמונים. קובץ קיים אינו נמחק.
