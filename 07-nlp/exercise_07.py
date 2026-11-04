import spacy

nlp = spacy.load("en_core_web_sm")


def print_pos_tags(sentence):
    doc = nlp(sentence)

    # pos_ הוא חלק הדיבר; explain מתרגמת את הקיצור להסבר קריא.
    for token in doc:
        print(f"{token.text} -> {token.pos_} -> {spacy.explain(token.pos_)}")


if __name__ == "__main__":
    print_pos_tags("The cat sat on the mat.")
