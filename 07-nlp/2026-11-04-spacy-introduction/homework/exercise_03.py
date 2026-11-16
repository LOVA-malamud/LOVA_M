import spacy

nlp = spacy.load("en_core_web_sm")

text = "She was running and had run 5 kilometers by 7am."

doc = nlp(text)

# lemma_ מחזיר את צורת הבסיס של המילה לפי ההקשר במשפט.
for token in doc:
    print(f"{token.text} -> {token.lemma_}")
