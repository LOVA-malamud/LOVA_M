def star_odd(word: str) -> bool:
    for i in range(1, len(word),2):
        if word[i] != "*":
            return False
    return True


word_input = input("enter your word")
if star_odd(word_input):
    print("yes")
else:
    print("no")
