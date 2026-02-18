languages_web = {
    "JavaScript",
    "TypeScript",
    "Python",
    "PHP",
    "Ruby",
    "Go",
    "Java",
    "C#"
}

languages_data_science = {
    "Python",
    "R",
    "Julia",
    "Scala",
    "MATLAB",
    "Java",
    "SQL"
}

languages_systems = {
    "C",
    "C++",
    "Rust",
    "Go",
    "Zig",
    "Assembly"
}

languages_mobile = {
    "Swift",
    "Kotlin",
    "Java",
    "Dart",
    "JavaScript",
    "C#"
}

print("\n🌐 Languages for Web Development:")
print(sorted(languages_web))

print("\n📊 Languages for Data Science:")
print(sorted(languages_data_science))

print("\n❓ Which languages are good for BOTH Web AND Data Science?")
print(languages_web & languages_data_science)

print("\n❓ Languages that can do Web, Mobile, OR Data Science?")
print(languages_web | languages_mobile | languages_data_science)

print("\n❓ Languages ONLY for System Programming (not web/mobile/data)?")
print(languages_systems - languages_web - languages_mobile - languages_data_science)

print("\n❓ Which languages work for Web but NOT Mobile?")
print(languages_web - languages_mobile)

print("\n❓ Is 'Python' in the web development set?")
print("Python" in languages_web)

print("\n❓ The ultimate polyglot language (in ALL four categories)?")
print(languages_web & languages_data_science & languages_systems & languages_mobile)

modern_web = {"JavaScript", "TypeScript", "Python"}
print("\n❓ Is modern_web a PROPER subset of web languages?")
print(modern_web < languages_web)
