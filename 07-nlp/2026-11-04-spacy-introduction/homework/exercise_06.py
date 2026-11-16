import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

# LOWER משווה בלי להבחין בין אותיות גדולות לקטנות.
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

pattern = nlp("artificial intelligence")

matcher.add("AI", [pattern])

doc = nlp(
    "Artificial Intelligence is the future. "
    "I study artificial intelligence."
)

matches = matcher(doc)
for match_id, start, end in matches:
    # ההתאמה מחזירה מיקומי טוקנים; החיתוך שומר את הכתיב המקורי.
    print(doc[start:end].text)
