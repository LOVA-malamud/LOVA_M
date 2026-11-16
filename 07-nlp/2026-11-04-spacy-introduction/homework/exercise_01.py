import spacy

nlp = spacy.load("en_core_web_sm")

text = "Taylor Swift performed in Los Angeles on March 3rd, 2023."

doc = nlp(text)

# ents מכיל ישויות; label_ הוא שם סוג הישות כמחרוזת.
for entity in doc.ents:
    print(entity.text, entity.label_)
