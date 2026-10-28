# עבודה יומיומית ב־VS Code

## פעם ראשונה

פתח את תיקיית `LOVA_M` עצמה ב־VS Code. תוספי Python, Pylance ו־Jupyter כבר מותקנים. ההגדרות המקומיות ממליצות על `.venv-study`; ההגדרות הגלובליות לא שונו. חיבור SQLTools הקיים נשמר.

אם מוצגת סביבה ישנה בתחתית החלון:

1. לחץ `Cmd+Shift+P` ובחר **Python: Select Interpreter**.
2. בחר **Enter interpreter path** ואז את `.venv-study/bin/python` בתוך הפרויקט.
3. פתח Terminal חדש ובדוק:

```bash
python -c "import sys; print(sys.executable)"
```

הנתיב צריך להסתיים ב־`LOVA_M/.venv-study/bin/python`. בחירת Interpreter שמורה בחלון עשויה לגבור על ברירת המחדל בקובץ ההגדרות; לכן בודקים את הנתיב בפועל. צילום מצב הבחירה נמצא מקומית ב־`.local/environment/vscode-selection.json` כאשר העזר הצליח; אם הדוח מציין fail, יש לבצע את שלושת הצעדים האלה.

## הרצת קובץ Python

אפשר ללחוץ **F5** ולבחור `LOVA_M: Python file (study)`; קובץ launch המקומי מצביע ישירות ל־`.venv-study`, גם כאשר חלון ישן זוכר Interpreter אחר. קיימות גם משימות תחת Terminal → Run Task: הרצת הקובץ הנוכחי ובדיקות הסביבה.

פתח למשל את [מחלקת Point](../05-oop/2026-10-25-point/poing.py), בחר **Run Python File in Terminal**, או הרץ:

```bash
source .venv-study/bin/activate
python 05-oop/2026-10-25-point/poing.py
```

Pylance מספק השלמה ובדיקות טיפוסים בסיסיות. התראות בתרגילים ישנים עשויות להיות חלק מהלמידה. לא הופעל עיצוב אוטומטי ששינה תרגילי מקור.

## מחברות Jupyter

פתח את [מחברת בדיקת הסביבה](../experiments/environment-checks/environment-smoke.ipynb). בפינה העליונה בחר **Select Kernel**, ואז **Python Environments** או **Jupyter Kernels**:

| עבודה | Interpreter / Kernel |
|---|---|
| Python, OOP, SQL, Data/ML, APIs | `.venv-study` / `LOVA_M · study (Python 3.12)` |
| TensorFlow/Keras | `.venv-tensorflow` / `LOVA_M · tensorflow (Python 3.12)` |
| PyTorch ותמונות | `.venv-torch` / `LOVA_M · torch (Python 3.12)` |

בתא הראשון אפשר לבדוק `import sys; print(sys.executable)`. בחירת Kernel של מחברת נפרדת מבחירת Interpreter של קובץ Python. במחברות ישנות עשויה להישמר בחירה ישנה; בחר מחדש לפי העבודה. ההגדרה המקומית שומרת את תיקיית העבודה של כל מחברת לפי מיקומה, כדי לשמר נתיבי נתונים יחסיים.

אפשר גם להפעיל `.venv-study/bin/python -m jupyterlab` ולבחור אחד משלושת ה־Kernels הרשומים. לשחזור הרישום: `.venv-study/bin/python tools/register_kernels.py`.

## בדיקות ואיכות קוד

ב־Testing sidebar בחר Refresh Tests ו־Run Tests. הוגדר pytest ל־`tests/environment`, ולא לתרגילים האינטראקטיביים הישנים.

```bash
.venv-study/bin/python -m pytest
.venv-study/bin/python -m ruff check tools tests/environment
.venv-study/bin/python -m black --check tools tests/environment
```

Ruff ו־Black הוגבלו לכלי הבדיקה החדשים. להפעלה חוזרת של בדיקות הספריות:

```bash
.venv-study/bin/python tools/check_environment.py --profile study
.venv-tensorflow/bin/python tools/check_environment.py --profile tensorflow
.venv-torch/bin/python tools/check_environment.py --profile torch
.venv-study/bin/python tools/check_notebooks.py
```

אין צורך באימון מודלים גדולים כדי לבדוק את הסביבה.

## התקנת ספרייה חדשה

הפעל את הסביבה המתאימה, בדוק `sys.executable`, והשתמש ב־`python -m pip install NAME`. עדכן את קובץ התלויות המתאים לפי [מדריך הסביבות](../PYTHON_ENVIRONMENT.md), ובדוק `python -m pip check`. אין להשתמש ב־sudo או ב־pip גלובלי.

דוגמאות הגדרות לשחזור נמצאות ב־[settings.example.json](vscode/settings.example.json), [extensions.example.json](vscode/extensions.example.json) וב־`docs/vscode/workspace.example.code-workspace`. הגדרות המחשב הפעילות ו־`LOVA_M-study.code-workspace` נשארים מקומיים.

מקור: [תיעוד סביבות Python הרשמי של VS Code](https://code.visualstudio.com/docs/python/environments).

**מגבלת האוטומציה בסיום:** ברירות המחדל ו־F5 הוגדרו ונפתח VS Code, אך ניסיון בחירת Interpreter דרך עזר API זמני נעצר בבדיקת תחום החלון ולא שינה את הבחירה השמורה. יש לבחור `.venv-study/bin/python` פעם אחת בחלון הרגיל כדי שגם Pylance ו־Run Python File ישתמשו בה. המחברות נבדקו בפועל דרך שלושת ה־Kernels, אך יש לבחור Kernel בנפרד במחברות ישנות.
