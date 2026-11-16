def count_freq(sentence: str) -> dict[str, int]:
    dictionary = {}
    sentence = sentence.lower()
    list = sentence.split()
    for word in list:
        x = list.count(word)
        dictionary[word] = x
    return dictionary

print(count_freq("To be or not to be"))