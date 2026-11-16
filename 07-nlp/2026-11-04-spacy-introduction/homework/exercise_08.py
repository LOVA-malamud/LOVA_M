from pathlib import Path

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")


def main():
    sentence = input("Enter a sentence: ")
    if not sentence.strip():
        print("Please enter a non-empty sentence.")
        return

    doc = nlp(sentence)
    # חלק הדיבר וההסבר שלו לכל טוקן, כולל סימני פיסוק.
    for token in doc:
        print(f"{token.text} -> {token.pos_} -> {spacy.explain(token.pos_)}")

    # dep מצייר קשרים תחביריים; page=True יוצר עמוד HTML שלם.
    html = displacy.render(doc, style="dep", page=True)
    html_path = Path(__file__).with_name("exercise_08_visualization.html")
    html_path.write_text(html, encoding="utf-8")
    print("Visualization saved:", html_path)


if __name__ == "__main__":
    main()
