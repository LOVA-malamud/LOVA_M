import spacy

nlp = spacy.load("en_core_web_sm")

text = "SpaCy is awesome and powerful."

# שינוי המאפיין במילון משפיע על הטוקן powerful במסמך שנעבד.
nlp.vocab["powerful"].is_stop = True

doc = nlp(text)

for token in doc:
    print(token.text, token.is_stop)
