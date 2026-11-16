"""בדיקות להגשה: מריצות את הקבצים בעותק זמני בלי לשנות HTML קיים."""

import ast
import contextlib
import io
from pathlib import Path
import re
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parent
EXAMPLE_8 = "Apple is looking at buying a U.K. startup for $1 billion."


class HomeworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="lovam-nlp-homework-")
        cls.addClassCleanup(cls.temp.cleanup)
        cls.work = Path(cls.temp.name)
        cls.outputs = {}
        for number in range(1, 9):
            name = f"exercise_{number:02d}.py"
            shutil.copy2(ROOT / name, cls.work / name)
            result = subprocess.run(
                [sys.executable, "-B", str(cls.work / name)],
                input=EXAMPLE_8 + "\n" if number == 8 else "",
                capture_output=True, text=True, timeout=60,
            )
            if result.returncode:
                raise AssertionError(f"{name}: {result.stderr}")
            cls.outputs[number] = result.stdout
        cls.html = (cls.work / "exercise_08_visualization.html").read_text(encoding="utf-8")
        cls.modules = {}
        with contextlib.redirect_stdout(io.StringIO()):
            for number in (2, 4, 5, 6, 7):
                cls.modules[number] = runpy.run_path(str(ROOT / f"exercise_{number:02d}.py"))

    def printed(self, function, text):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            function(text)
        return output.getvalue().splitlines()

    def test_01_entities_and_exact_output(self):
        self.assertEqual(self.outputs[1].splitlines(), [
            "Taylor Swift PERSON", "Los Angeles GPE", "March 3rd, 2023 DATE",
        ])

    def test_02_person_example_and_function(self):
        expected = ["Serena Williams", "Tom Hanks"]
        self.assertEqual(self.outputs[2].splitlines(), expected)
        self.assertEqual(self.printed(self.modules[2]["print_person_entities"],
                                     "Serena Williams had dinner with Tom Hanks in Paris."), expected)

    def test_02_empty_and_no_person(self):
        for text in ("", "Paris is in France.", "The cat sat on the mat."):
            with self.subTest(text=text):
                self.assertEqual(self.printed(self.modules[2]["print_person_entities"], text), [])

    def test_03_lemmas(self):
        self.assertEqual(self.outputs[3].splitlines(), [
            "She -> she", "was -> be", "running -> run", "and -> and",
            "had -> have", "run -> run", "5 -> 5", "kilometers -> kilometer",
            "by -> by", "7 -> 7", "am -> am", ". -> .",
        ])

    def test_04_stop_words_example(self):
        expected = ["example", "sentence", "stop", "words"]
        self.assertEqual(ast.literal_eval(self.outputs[4]), expected)
        self.assertEqual(self.modules[4]["remove_stop_words"](
            "This is an example sentence with some stop words."), expected)

    def test_04_empty_punctuation_spaces_and_case(self):
        function = self.modules[4]["remove_stop_words"]
        for text in ("", "   \n\t", "...?!", "THE is and"):
            with self.subTest(text=text):
                self.assertEqual(function(text), [])
        self.assertEqual(function("Cats,  dogs!\n"), ["Cats", "dogs"])

    def test_05_custom_stop_word(self):
        self.assertEqual(self.outputs[5].splitlines(), [
            "SpaCy False", "is True", "awesome False", "and True", "powerful True", ". False",
        ])
        nlp = self.modules[5]["nlp"]
        self.assertTrue(nlp.vocab["powerful"].is_stop)
        self.assertEqual([t.text for t in nlp("SpaCy is awesome and powerful.") if t.is_stop],
                         ["is", "and", "powerful"])

    def test_06_example_matches(self):
        self.assertEqual(self.outputs[6].splitlines(), ["Artificial Intelligence", "artificial intelligence"])

    def test_06_case_repetition_and_nonmatches(self):
        module = self.modules[6]
        for text, expected in [
            ("ARTIFICIAL INTELLIGENCE; artificial intelligence!", ["ARTIFICIAL INTELLIGENCE", "artificial intelligence"]),
            ("", []), ("artificial general intelligence", []), ("artificially intelligent", []),
        ]:
            with self.subTest(text=text):
                doc = module["nlp"](text)
                found = [doc[start:end].text for _, start, end in module["matcher"](doc)]
                self.assertEqual(found, expected)

    def test_07_tags_explanations_and_function(self):
        expected = ["The -> DET -> determiner", "cat -> NOUN -> noun", "sat -> VERB -> verb",
                    "on -> ADP -> adposition", "the -> DET -> determiner", "mat -> NOUN -> noun",
                    ". -> PUNCT -> punctuation"]
        self.assertEqual(self.outputs[7].splitlines(), expected)
        function = self.modules[7]["print_pos_tags"]
        self.assertEqual(self.printed(function, "The cat sat on the mat."), expected)
        self.assertEqual(self.printed(function, ""), [])

    def test_08_simulated_input_and_pos(self):
        output = self.outputs[8]
        self.assertIn("Enter a sentence: ", output)
        for line in ("Apple -> PROPN -> proper noun", "is -> AUX -> auxiliary",
                     "looking -> VERB -> verb", "billion -> NUM -> numeral"):
            self.assertIn(line, output)
        tags = [line for line in output.splitlines() if " -> " in line]
        self.assertEqual(len(tags), 13)
        self.assertNotIn("None", output)
        self.assertIn("Visualization saved:", output)

    def test_08_valid_dependency_svg(self):
        self.assertIn("<html", self.html.lower())
        self.assertIn("</html>", self.html.lower())
        match = re.search(r"<svg\b.*?</svg>", self.html, re.DOTALL)
        self.assertIsNotNone(match)
        svg = ET.fromstring(match.group())
        self.assertTrue(svg.tag.endswith("svg"))
        def elements(class_name):
            return [node for node in svg.iter() if class_name in node.attrib.get("class", "").split()]
        words = ["".join(node.itertext()) for node in elements("displacy-word")]
        self.assertIn("Apple", words)
        self.assertIn("looking", words)
        self.assertGreater(len(elements("displacy-arc")), 0)
        self.assertGreater(len(elements("displacy-arrowhead")), 0)
        self.assertGreater(len(elements("displacy-label")), 0)
        ids = {node.attrib["id"] for node in svg.iter() if "id" in node.attrib}
        for node in svg.iter():
            for key, value in node.attrib.items():
                if key.endswith("href") and value.startswith("#"):
                    self.assertIn(value[1:], ids)

    def test_08_empty_input_preserves_existing_html(self):
        html_path = self.work / "exercise_08_visualization.html"
        before = html_path.read_bytes()
        result = subprocess.run([sys.executable, "-B", str(self.work / "exercise_08.py")],
                                input="   \n", capture_output=True, text=True, timeout=60)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Please enter a non-empty sentence.", result.stdout)
        self.assertEqual(html_path.read_bytes(), before)

    def test_08_single_word_input(self):
        result = subprocess.run([sys.executable, "-B", str(self.work / "exercise_08.py")],
                                input="Hello\n", capture_output=True, text=True, timeout=60)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Hello ->", result.stdout)
        self.assertIn("<svg", (self.work / "exercise_08_visualization.html").read_text())


if __name__ == "__main__":
    unittest.main(verbosity=2)
