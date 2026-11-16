"""דוגמה ראשונה ל־spaCy: חלוקת משפט באנגלית ל־Tokens."""

import spacy

def main():
    nlp = spacy.load("en_core_web_sm")
    text = "I am learning natural language processing."
    doc = nlp(text)

    print("Sentence:", text)
    print("Tokens:")
    for token in doc:
        print(token.text)


if __name__ == "__main__":
    main()
