import spacy

nlp = spacy.load("en_core_web_sm")


def print_person_entities(sentence):
    doc = nlp(sentence)

    # מסננים רק שמות של אנשים, בלי מקומות או סוגי ישויות אחרים.
    for entity in doc.ents:
        if entity.label_ == "PERSON":
            print(entity.text)


if __name__ == "__main__":
    print_person_entities("Serena Williams had dinner with Tom Hanks in Paris.")
