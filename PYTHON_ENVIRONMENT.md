# סביבת Python של LOVA_M

הוקמה ונבדקה ב־28–29 באוקטובר 2026. סביבת העבודה היומיומית המומלצת היא **`.venv-study`**. TensorFlow ו־PyTorch מופרדים כדי לא לערבב את NumPy 1.x הדרוש להם עם סביבת הנתונים החדשה.

## המחשב והמפרשים שנבדקו

| רכיב | ממצא |
|---|---|
| macOS | 26.5.2, build 25F84 |
| מעבד | Intel Core i7-9750H, x86_64 — אין Apple Silicon או Rosetta בתהליך שנבדק |
| זיכרון | 16GB |
| GPU | Intel UHD Graphics 630 ו־AMD Radeon Pro 5300M,‏ 4GB |
| דיסק | כ־278GiB פנויים לפני ההתקנות; כ־268GiB לאחר הגיבוי וההתקנות |
| Python של המערכת / Command Line Tools | 3.9.6, דרך `/usr/bin/python3` — לא שונה |
| Python עצמאי | 3.12.10, תחת `/Library/Frameworks/Python.framework/Versions/3.12/` — בסיס הסביבות החדשות |
| Anaconda | Python 3.13.5 תחת `/opt/anaconda3/` — לא שונה; לא נמצאו סביבות נוספות תחת envs |
| ברירת המחדל ב־Terminal בזמן הסריקה | `python3` היה Python 3.12.10; `python` היה Anaconda 3.13.5 |

גם `pip --version` נבדק בכל מפרש. שלוש התקנות הבסיס עברו `pip check`; ספריות גלובליות לא הותקנו ולא שודרגו. צילום המלא של רשימות המערכת נשמר מקומית ב־`.local/environment/global-before.json` ואינו לפרסום. `python -m pip` מתוך הסביבה הפעילה מונע שימוש ב־pip של מפרש אחר.

## מה נמצא לפני ההתקנה?

- `2.9.27/.venv`: סביבת Data/ML מצומצמת, pip 26.2.1; `pip check` עבר.
- `.venv-tf`: TensorFlow 2.16.2, Keras 3.15.1 ו־NumPy 1.26.4, pip 26.2.1; `pip check` עבר. לא היו בה כלי Jupyter מלאים.
- `.venv`: סביבה מעורבת, pip 25.1.1; `pip check` נכשל: SciPy 1.18.0 דורש NumPy >=2.0, אבל מותקן NumPy 1.26.4. **היא לא תוקנה ולא שונתה**, כדי לשמור על המצב הקיים.
- ב־VS Code נמצאו Python, Pylance, Jupyter ו־debugpy מותקנים מראש. הבחירות הישנות הצביעו לעיתים ל־`.venv` ולעיתים ל־`.venv-tf`; אין להסתמך על שם `python` בלבד.

הוחלט ליצור סביבות חדשות ולהשאיר את שלוש הישנות ללא שינוי. רשימות החבילות שלהן הושוו לפני ואחרי ונמצאו זהות. [צילום מלא לפני](docs/environment/installed-before.json) · [סריקת imports בקוד ובמחברות](docs/environment/source-imports.json).

## הסביבות החדשות

| סביבה | שימוש | Python | NumPy | גודל בקירוב | pip check |
|---|---|---|---|---|---|
| `.venv-study` | Python, SQL, OOP, Data/ML, מחברות, תמונות ו־APIs | 3.12.10 | 2.5.4 | 926MB | עבר |
| `.venv-tensorflow` | TensorFlow/Keras ותרגילי ANN/CNN | 3.12.10 | 1.26.4 | 1.8GB | עבר |
| `.venv-torch` | PyTorch, torchvision ו־GPU דרך MPS | 3.12.10 | 1.26.4 | 972MB | עבר |

יש 142, 77 ו־48 חבילות בהתאמה בקובצי הנעילה, **כולל תלויות עקיפות**; pip עצמו מגיע עם venv ואינו נכלל בנעילה. רוב התלויות העקיפות של סביבת הלימוד מגיעות מ־JupyterLab/Notebook. לא הותקנו ספריות נוספות רק בגלל פופולריות. [רשימות מלאות לאחר ההתקנה](docs/environment/installed-after.json).

## ספריות מרכזיות: לפני ואחרי

״לא הייתה״ מתייחס לשלוש סביבות המאגר; חבילה עשויה להתקיים ב־Anaconda בלי שתהיה זמינה למפרש של הפרויקט.

| ספרייה | מטרה | הייתה לפני | הותקנה כעת בסביבה החדשה |
|---|---|---|---|
| numpy | מערכים וחישוב מספרי | .venv 1.26.4<br>2.9.27/.venv 2.5.2<br>.venv-tf 1.26.4 | .venv-study **2.5.4**<br>.venv-tensorflow **1.26.4**<br>.venv-torch **1.26.4** |
| pandas | טבלאות וניתוח נתונים | .venv 3.0.3<br>2.9.27/.venv 3.0.5 | .venv-study **3.1.0** |
| scipy | חישוב מדעי וסטטיסטיקה | .venv 1.18.0<br>2.9.27/.venv 1.18.1<br>.venv-tf 1.17.1 | .venv-study **1.18.1**<br>.venv-tensorflow **1.17.1** |
| matplotlib | גרפים | .venv 3.11.0<br>2.9.27/.venv 3.11.1 | .venv-study **3.11.2**<br>.venv-tensorflow **3.11.2**<br>.venv-torch **3.11.2** |
| seaborn | תרשימים סטטיסטיים | 2.9.27/.venv 0.13.2 | .venv-study **0.13.2** |
| plotly | גרפים אינטראקטיביים | לא הייתה בסביבות המאגר | .venv-study **6.9.0** |
| scikit-learn | מודלי ML ועיבוד נתונים | .venv 1.9.0<br>2.9.27/.venv 1.9.0<br>.venv-tf 1.9.1 | .venv-study **1.9.1**<br>.venv-tensorflow **1.9.1** |
| statsmodels | מודלים סטטיסטיים | לא הייתה בסביבות המאגר | .venv-study **0.15.0** |
| openpyxl | קריאה וכתיבה של Excel | לא הייתה בסביבות המאגר | .venv-study **3.1.5** |
| jupyterlab | ממשק מחברות בדפדפן | לא הייתה בסביבות המאגר | .venv-study **4.6.4** |
| notebook | ממשק Notebook | לא הייתה בסביבות המאגר | .venv-study **7.6.3** |
| ipykernel | Kernel ל־Python | .venv 7.3.0 | .venv-study **7.4.0**<br>.venv-tensorflow **7.4.0**<br>.venv-torch **7.4.0** |
| pillow | טעינת תמונות | .venv 12.3.0<br>2.9.27/.venv 12.3.0 | .venv-study **12.3.0**<br>.venv-tensorflow **12.3.0**<br>.venv-torch **12.3.0** |
| opencv-python | ראייה ממוחשבת | לא הייתה בסביבות המאגר | .venv-study **4.14.0.94** |
| imageio | קריאה וכתיבה של תמונות | לא הייתה בסביבות המאגר | .venv-study **2.38.1** |
| fastapi | בניית APIs | לא הייתה בסביבות המאגר | .venv-study **0.162.0** |
| uvicorn | שרת ASGI | לא הייתה בסביבות המאגר | .venv-study **0.54.0** |
| requests | בקשות HTTP | .venv 2.34.2<br>.venv-tf 2.34.2 | .venv-study **2.34.2**<br>.venv-tensorflow **2.34.2** |
| httpx | HTTP וסביבת בדיקת API | לא הייתה בסביבות המאגר | .venv-study **0.28.1** |
| pydantic | אימות מבני נתונים | לא הייתה בסביבות המאגר | .venv-study **2.14.1** |
| python-dotenv | טעינת הגדרות מקובצי env מקומיים | לא הייתה בסביבות המאגר | .venv-study **1.2.4** |
| sqlalchemy | גישה למסדי נתונים ו־ORM | לא הייתה בסביבות המאגר | .venv-study **2.1.6** |
| aiosqlite | SQLite אסינכרוני | לא הייתה בסביבות המאגר | .venv-study **0.22.1** |
| torch | רשתות עצביות ו־MPS | לא הייתה בסביבות המאגר | .venv-torch **2.2.2** |
| torchvision | כלים לתמונות ב־PyTorch | לא הייתה בסביבות המאגר | .venv-torch **0.17.2** |
| tensorflow | רשתות ANN/CNN על CPU | .venv 2.16.2<br>.venv-tf 2.16.2 | .venv-tensorflow **2.16.2** |
| keras | API לבניית רשתות | .venv 3.15.1<br>.venv-tf 3.15.1 | .venv-tensorflow **3.15.1** |
| pytest | בדיקות | לא הייתה בסביבות המאגר | .venv-study **9.2.0** |
| ruff | בדיקת איכות קוד | לא הייתה בסביבות המאגר | .venv-study **0.17.3** |
| black | עיצוב קוד | לא הייתה בסביבות המאגר | .venv-study **26.10.1** |
| dmba | פונקציות במחברת הפולינומית הקיימת | לא הייתה בסביבות המאגר | .venv-study **0.2.4** |
| pygame | המשחק הגרפי הקיים | .venv 2.6.1 | .venv-study **2.6.1** |
| ipython | ממשק אינטראקטיבי ו־display במחברות | .venv 9.14.1 | .venv-study **9.17.1**<br>.venv-tensorflow **9.17.1**<br>.venv-torch **9.17.1** |

כל הספריות שביקשת הותקנו בסביבה תואמת, למעט תוסף ההאצה `tensorflow-metal`. נוספו dmba ו־pygame בעקבות imports קיימים; IPython מגיע עם סביבת המחברות ומשמש גם את הקוד הקיים.

## תאימות Deep Learning ו־GPU

- TensorFlow **2.16.2** הוא הגרסה האחרונה עם wheel רשמי ל־macOS Intel. הותקן עם NumPy 1.26.4 ו־SciPy <1.18. TensorFlow עבר פעולות Tensor,‏ CNN קטן וגרדיאנטים על CPU; רשימת ה־GPU שלו ריקה. [הנחיות TensorFlow הרשמיות](https://www.tensorflow.org/install/pip).
- PyTorch **2.2.2** ו־torchvision **0.17.2** הם זוג ה־wheels האחרון שנמצא ב־PyPI ל־macOS x86_64 ול־Python 3.12. אלה גרסאות ותיקות שנבחרו בגלל מגבלת התמיכה במחשב, ולא הגרסאות החדשות ביותר. פעולות Tensor,‏ CNN, גרדיאנט ו־torchvision NMS עברו. [קובץ Intel הרשמי ב־PyPI](https://pypi.org/project/torch/2.2.2/).
- ב־PyTorch נבדקו `torch.backends.mps.is_built()` ו־`is_available()` ושניהם החזירו **True**. גם כפל מטריצות בוצע בפועל על **mps:0**, ולא רק זוהה כרטיס מסך. אפשר לבחור `torch.device("mps" if torch.backends.mps.is_available() else "cpu")` ולהעביר גם מודל וגם נתונים לאותו device.
- חומרת AMD מתאימה עקרונית ל־tensorflow-metal לפי Apple, אך אין wheel של התוסף ל־Intel עם Python 3.12. נמצאה גרסת Intel 1.0.0 ל־Python 3.11; לא הותקנה ערימת Python/TF ישנה נוספת רק לשם כך. לא נבנה תוסף ממקור ולא נכפתה חבילה לא תואמת. [דרישות Apple](https://developer.apple.com/metal/tensorflow-plugin/) · [קובצי החבילה והגרסאות](https://pypi.org/project/tensorflow-metal/#files).

לא הותקנו CUDA/ROCm,‏ torchaudio, חבילות GPU ל־Linux, חבילות Apple Silicon, ספריות LLM/API נוספות או מודלים מוכנים: אין להן צורך מקומי מזוהה כרגע. הייבוא השגוי `mataplotlib.python` במחברת הישנה אינו ספרייה חסרה להתקנה; הוא טעות בקוד שנשמרה.

## תוצאות בדיקות והסתייגויות אמיתיות

| בדיקה | תוצאה |
|---|---|
| imports בסביבת הלימוד | 29 ספריות מרכזיות עברו |
| NumPy, Pandas, Matplotlib ו־scikit-learn | חישוב מערך, DataFrame, PNG בזיכרון ומודל ליניארי קטן עברו |
| SciPy/Statsmodels/Plotly/Excel | חישוב סטטיסטי, OLS, יצירת תרשים וקריאה חוזרת של workbook עברו |
| Pillow/OpenCV/ImageIO | המרת צבע וכתיבה/קריאה בזיכרון עברו |
| FastAPI/Pydantic/httpx/requests/dotenv | endpoint תקין, בדיקת קלט לא תקין ובקשות מדומות עברו; אין שירות חיצוני |
| SQLAlchemy ו־aiosqlite | שאילתות ב־SQLite בזיכרון עברו; המסד האישי לא שונה |
| pytest | 11 בדיקות התנהגות עברו |
| Ruff ו־Black | בדיקות לקוד כלי הסביבה החדשים בלבד; תרגילי הלימוד לא עוצבו מחדש |
| TensorFlow/Keras | 8 imports ופעולת CNN/גרדיאנט עברו; GPU לא זמין בסביבה זו |
| PyTorch/torchvision | 7 imports, פעולת CNN/גרדיאנט, NMS ופעולת MPS עברו |
| מחברות | מחברת זעירה הורצה בכל אחד משלושת ה־Kernels, עם assert של שם הסביבה |
| JupyterLab | שרת מוגן באסימון זמני על localhost: ממשק Lab ופתיחת מחברת החזירו HTTP 200; השרת נסגר |
| pip check | עבר בשלוש הסביבות החדשות; הכשל הישן ב־.venv נשאר מתועד |

**אירועים שלא הוסתרו:** בדיקת HTTP של Jupyter החזירה תחילה 404. התברר ש־231 נתיבים רגילים במאגר סומנו ב־macOS כ־Hidden, ולכן Jupyter הסתיר את תיקיות הלימוד. הוסר רק UF_HIDDEN מנתיבים שאינם מתחילים בנקודה; התוכן לא השתנה. הסימונים הקודמים שמורים ב־`.local/environment/hidden-flags-before.json`, ובגיבוי. אחרי התיקון הבדיקה עברה. dotfiles, סודות וסביבות נשארו מוסתרים.

קיימת אזהרת deprecation אחת בבדיקת FastAPI/Starlette: שימוש ב־httpx ב־TestClient מיושן ביחס לכיוון העתידי של Starlette. הבדיקה עובדת; אין התנגשות ב־pip check. לא נוספה חבילה אחרת כדי להשתיק אזהרה. אזהרות Jupyter נוספות לגבי תעבורת kernel ב־localhost ולגבי cache ראשוני תועדו בזמן ההרצה; לא נחשף שרת לרשת החיצונית.

המחברות הישנות עדיין עשויות להכיל שגיאות לימודיות: למשל df לפני הגדרתו, פלט שהודבק כקוד או שם import שגוי. התקנת IPython ו־dmba פותרת חוסרים בסביבה החדשה, אך אינה מתקנת קוד. [דוח הקוד המקורי](docs/validation.md).

תוצאות מפורטות: [Study](docs/environment/study-checks.json) · [TensorFlow](docs/environment/tensorflow-checks.json) · [PyTorch](docs/environment/torch-checks.json) · [Kernels](docs/environment/notebook-checks.json) · [JupyterLab](docs/environment/jupyter-server-check.json).

## שימוש יומיומי

משורש המאגר:

```bash
source .venv-study/bin/activate
python -c "import sys; print(sys.executable)"
python 05-oop/2026-10-25-point/poing.py
python -m pytest
python -m jupyterlab
```

לעבודה ב־TensorFlow או ב־PyTorch יש לפתוח Terminal חדש ולהפעיל את `.venv-tensorflow/bin/activate` או `.venv-torch/bin/activate`, בהתאמה. בסיום משתמשים ב־`deactivate`. לא מפעילים כמה סביבות זו בתוך זו.

במחברת בוחרים Kernel מתאים, בנפרד מה־Interpreter של קובץ Python. ה־Kernels נרשמו **בתוך `.venv-study/share/jupyter` בלבד**, עם שמות `lovam-study`,‏ `lovam-tensorflow`,‏ `lovam-torch`. שמות התצוגה מתחילים ב־`LOVA_M ·`. הפעלת JupyterLab מתוך `.venv-study` מציגה את שלושתם. [מדריך VS Code](docs/vscode-guide.md).

## שחזור במחשב אחר

על **Mac Intel עם Python 3.12** מותקן, מתוך שורש המאגר:

```bash
python3.12 -m venv .venv-study
.venv-study/bin/python -m pip install -r requirements/study-macos-intel-py312.txt

python3.12 -m venv .venv-tensorflow
.venv-tensorflow/bin/python -m pip install -r requirements/tensorflow-macos-intel-py312.txt

python3.12 -m venv .venv-torch
.venv-torch/bin/python -m pip install -r requirements/torch-macos-intel-py312.txt

.venv-study/bin/python tools/register_kernels.py
.venv-study/bin/python -m pytest
.venv-study/bin/python -m pip check
.venv-tensorflow/bin/python -m pip check
.venv-torch/bin/python -m pip check
```

אין להעתיק תיקיות venv למיקום אחר: בונים אותן מחדש. קובצי הנעילה מכוונים לפלטפורמה שנבדקה; ל־Apple Silicon, Windows או Linux יש לפתור מחדש את קובצי ה־`.in` ולבדוק תמיכה בגרסאות ה־Deep Learning לפי תיעוד הספק. אין לנסות להתקין wheel של Intel על ARM.

אפשר לשחזר רק את `.venv-study` אם לא עובדים עדיין ב־Deep Learning. [מפת קובצי התלויות](requirements/README.md) מסבירה כיצד לשמור על החלוקה.

## הוספת ספרייה בעתיד

בחר סביבה, בדוק `sys.executable`, הוסף את התלות לקובץ `.in` המתאים והתקן באמצעות `python -m pip install NAME`. הרץ smoke checks ו־`python -m pip check`; לאחר הצלחה שמור `python -m pip freeze > requirements/ENV-macos-intel-py312.txt` מתוך אותה סביבה. עדכון lock הוא שינוי מכוון לביקורת, ואין לדרוס lock של סביבה אחרת. אין צורך לעדכן חבילות שלא קשורות לשיעור.

## בטיחות ו־Git

ענף: `chore/learning-progress-python-environments`, על בסיס ענף הארגון הקודם. גיבוי נוסף מלא באמצעות APFS clone נשמר לפני השינויים ב־`/Users/lova/Desktop/LOVA_M-backup-before-learning-20261028`. אומתו 174 קובצי המקור/ההגדרות שמחוץ לסביבות; שימור הקוד והמחברות נבדק שוב בסיום.

אומתו כל 174 הקבצים שהיו לפני התוספת: אין מקור לימודי חסר או שונה. Point, KNN, DBSCAN ו־KMeans עברו גם עם הסביבה החדשה; [תוצאות ההרצה](docs/environment/existing-code-checks.json).

לא שונו המפרשים הגלובליים, הסביבות הישנות, מסד הנתונים או תרגילי המקור. הגדרות VS Code הן מקומיות לפרויקט, וחיבור ה־SQL המקורי נשמר. נפתח חלון VS Code עם סביבת העבודה; ברירת המחדל ו־F5 מצביעים ל־study. הבחירה השמורה בחלון הרגיל עדיין דורשת בחירת Interpreter חד־פעמית: העזר הזמני לבחירה דרך API נעצר בבדיקת תחום החלון ללא שינוי. לא נערך מסד ההגדרות ישירות. תיקיות `.venv-*`, `.local`, קובצי workspace והגדרות מקומיות מוחרגים מ־Git. יש בתיעוד דוגמאות ניידות להגדרות. לא בוצעו push או merge.
