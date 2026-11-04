# מבוא ל־NLP ול־spaCy — 04.11.2026

## מה לומדים היום?

**NLP — Natural Language Processing**, או עיבוד שפה טבעית, הוא תחום העוסק בעיבוד טקסט ושפה באמצעות מחשב. בשיעור הראשון מכינים סביבת עבודה, טוענים מודל באנגלית ומחלקים משפט ליחידות טקסט.

**spaCy** היא ספריית Python לעיבוד שפה טבעית. `en_core_web_sm` הוא מודל קטן לאנגלית שמתקינים בנפרד מהספרייה. בדוגמה שלנו טוענים אותו באמצעות `spacy.load("en_core_web_sm")`.

**Token** הוא יחידה בטקסט, למשל מילה או סימן פיסוק. חלוקת טקסט ל־Tokens נקראת **Tokenization**. זו אינה בהכרח חלוקה לפי רווחים: גם הנקודה בסוף המשפט שלנו היא Token בפני עצמה. ב־spaCy החלוקה מבוצעת על ידי ה־Tokenizer, המשתמש בכללים המתאימים לשפה.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I am learning natural language processing.")

for token in doc:
    print(token.text)
```

`nlp` הוא צינור עיבוד הטקסט שנטען. הקריאה `nlp(text)` מחזירה אובייקט `Doc`, שאפשר לעבור על ה־Tokens שלו בלולאה. `token.text` הוא הטקסט של היחידה הנוכחית. כאן מתמקדים רק בחלוקה ל־Tokens.

הפלט הצפוי הוא שבע יחידות:

```text
I
am
learning
natural
language
processing
.
```

## סביבת העבודה של השיעור

במחשב נמצאה Conda, ונוצרה סביבה נפרדת בשם `spacy_env`:

| רכיב | גרסה |
|---|---|
| Python | 3.11.13 |
| spaCy | 3.8.18 |
| ipykernel | 7.4.0 |
| en_core_web_sm | 3.8.0 |

מיקום ה־Python במחשב זה: `/opt/anaconda3/envs/spacy_env/bin/python`.

`ipykernel` מאפשר ל־Jupyter Notebook להריץ קוד בסביבה הזו. ה־Kernel הוא תהליך Python שמבצע את התאים במחברת; בחירתו חשובה גם אם בטרמינל מופעלת סביבה אחרת.

הסביבה כבר הוכנה. **אין צורך להתקין שוב כדי להריץ את הדוגמה.** הפקודות הבאות מתעדות את ההקמה, ומיועדות גם לשחזור במחשב שבו הסביבה עדיין אינה קיימת. מריצים משורש הפרויקט:

```bash
conda create -n spacy_env python=3.11 pip -y
conda run -n spacy_env python -m pip install -r 07-nlp/2026-11-04-spacy-introduction/requirements.txt
conda run -n spacy_env python -m ipykernel install --user --name spacy_env --display-name "Python nov-04 (spacy_env)"
conda run -n spacy_env python -m spacy validate
conda run -n spacy_env python -m pip check
```

קובץ הדרישות מקבע את גרסאות ספריות השיעור ואת המודל שנבדקו, אך אינו מקבע את כל התלויות העקיפות. בהתקנה שבוצעה בפועל הותקנו תחילה `spacy` ו־`ipykernel`, והמודל הורד באמצעות:

```bash
conda run -n spacy_env python -m spacy download en_core_web_sm
```

`conda run -n spacy_env` בוחר במפורש את הסביבה, ו־`python -m pip` מתקין דרך ה־Python שלה. אין להשתמש ב־`pip` כללי. אין צורך לשדרג או לשנות את הסביבות הישנות של הפרויקט.

## הרצה ב־VS Code

למחברת Jupyter: פתח קובץ `.ipynb`, לחץ **Select Kernel**, ובמידת הצורך **Select Another Kernel → Jupyter Kernel**, ובחר **Python nov-04 (spacy_env)**. אם מוצגת רשימת **Python Environments**, אפשר לבחור `spacy_env` עם Python 3.11.13. הרחבות Python ו־Jupyter כבר מותקנות במחשב.

להרצת קובץ Python: פתח את `main.py`, הפעל **Python: Select Interpreter** מחלונית הפקודות (`Cmd+Shift+P`) ובחר `spacy_env`. אם הסביבה עדיין אינה ברשימה, בחר **Enter interpreter path** והזן `/opt/anaconda3/envs/spacy_env/bin/python`.

לחלופין, בטרמינל של VS Code, משורש הפרויקט, אפשר להריץ ללא שינוי הסביבה הפעילה:

```bash
conda run -n spacy_env python 07-nlp/2026-11-04-spacy-introduction/main.py
```

בדיקת ה־Python הפעיל בתוך תא במחברת:

```python
import sys
print(sys.executable)
```

הנתיב צריך להצביע ל־`spacy_env/bin/python`. אם מתקבלת הודעה שהספרייה או המודל אינם מותקנים, בדוק קודם שנבחר ה־Kernel הזה. אחרי החלפת Kernel, הרץ מחדש את התאים מתחילת המחברת.

אפשר גם לפתוח את `LOVA_M-nlp.code-workspace` שבשורש הפרויקט: זו תצורת עבודה מקומית נוספת עם נתיב ברירת מחדל ל־Python של השיעור. אם VS Code זוכר Interpreter קודם, בחר אותו במפורש לפי ההוראות למעלה. בחירת ה־Kernel במחברת נפרדת מבחירת ה־Interpreter.

## מה נבדק בפועל?

- `python -m spacy validate` אישר התאמה בין הספרייה למודל.
- `python -m pip check` הסתיים ללא תלויות שבורות.
- `main.py` טען את המודל והדפיס את שבע היחידות המוצגות למעלה.
- ה־Kernel הרשום הופעל בפועל והריץ טעינת מודל וטוקניזציה באמצעות ה־Python של `spacy_env`.
- כל גרסאות החבילות וקובצי `pyvenv.cfg` בחמש סביבות הפרויקט הקודמות הושוו למצב ההתחלתי ונשארו ללא שינוי.

דוח האימות המקומי נשמר ב־`.local/nlp-2026-11-04/verification.log`. הדוח, סביבות Python והגדרות העבודה המקומיות מוחרגים מ־Git; קוד השיעור, התיעוד וקובץ הדרישות מיועדים לשמירה במאגר.

## מקורות

- [התקנת spaCy](https://spacy.io/usage)
- [פקודות הורדה ובדיקת תאימות](https://spacy.io/api/cli)
- [רישום Kernel לסביבת Python](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)

זהו חומר מבוא בלבד; לא נוספו תרגילים מעבר לדוגמת החלוקה ל־Tokens.
