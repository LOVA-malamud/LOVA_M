# Python, SQL & Data Science · Classwork

My course exercises from Python fundamentals through relational queries and regression. Original lesson dates, filenames, solutions and data are preserved.

**Status:** learning archive with completed examples and unfinished experiments. This is not one installable application.

[Browse by topic](TOPICS.md) · [Homework](https://github.com/LOVA-malamud/ekom_home_work) · [ML exam notes](https://github.com/LOVA-malamud/machine_learning_exam_b)

## Find a concept

| Topic | Start here |
| --- | --- |
| Strings, branching and random values | [Fundamentals](TOPICS.md#python-fundamentals-and-control-flow) |
| Lists, sets, dictionaries and grouping | [Data structures](TOPICS.md#lists-sets-and-dictionaries) |
| Functions, validation and small algorithms | [Problem solving](TOPICS.md#functions-and-problem-solving) |
| SQL filtering, aggregation, joins and relationships | [Relational data](TOPICS.md#sql-and-relational-data) |
| Array indexing and tabular exploration | [NumPy and pandas](TOPICS.md#numpy-and-pandas) |
| Linear/polynomial regression, MSE and R² | [Models and evaluation](TOPICS.md#regression-visualization-and-evaluation) |

## Use the exercises

Use Python 3.12+ for the mixed classwork syntax. Most introductory scripts need only the standard library. From the repository root, this small example needs no input or third-party packages:

```bash
python3 '22.2/def.py'
```

For other files, read the source and imports first. Data-science examples use NumPy, pandas, matplotlib, seaborn, scikit-learn and, in one notebook, dmba. Pygame is needed only for the graphical game. There is no shared pinned dependency environment; install only the chosen exercise's dependencies in a local virtual environment.

View notebooks on GitHub or open them with Jupyter. The root pandas notebook expects `Churn_Modelling.csv` in its working directory. Keep SQL work in a disposable copy of the study database. Some scripts prompt for input; the game uses files from its own dated folder.

## What is preserved

Date-named folders contain the original lessons; root notebooks and the CSV/SQLite files remain where they were. [TOPICS.md](TOPICS.md) adds navigation without moving sources. Hebrew comments and exercise instructions remain intact.

## Checks and limitations

There is no repository-wide automated test suite. The documentation pass checks links and representative standard-library examples; it does not certify every answer. Empty placeholders and the unfinished plotting notebook are identified in the index. Dataset provenance and database contents have not been independently verified.

On 2026-10-28, `22.2/def.py` ran successfully under Python 3.12.10 and printed `30` and `-2`.
