import random

words = ["python", "hangman", "computer", "keyboard", "monitor"]
word = random.choice(words)
letters = list(word)
guessed = []
hearts = 3

print("Welcome to Hangman!")
print("The word has", len(letters), "letters.")

while hearts > 0:
    # Show the word with blanks
    display = []
    for letter in letters:
        if letter in guessed:
            display.append(letter)
        else:
            display.append("_")
    print(" ".join(display))

    # Check if the player won
    if "_" not in display:
        print("You won!")
        break

    print("Hearts left:", hearts)
    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that!")
    elif guess in letters:
        print("Correct!")
        guessed.append(guess)
    else:
        print("Wrong!")
        guessed.append(guess)
        hearts -= 1

if hearts == 0:
    print("You lost! The word was:", word)