import spacy

nlp = spacy.load("en_core_web_sm")


def remove_stop_words(sentence):
    doc = nlp(sentence)
    words = []

    # הפלט כולל מילים בלבד: ללא מילות עצירה, פיסוק או רווחים נפרדים.
    for token in doc:
        if not token.is_stop and not token.is_punct and not token.is_space:
            words.append(token.text)
    return words

if __name__ == "__main__":
    sentence = "This is an example sentence with some stop words."
    print(remove_stop_words(sentence))
