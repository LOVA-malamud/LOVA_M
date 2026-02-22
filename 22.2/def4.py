import random

def get_random_number() -> int:
    """
    pick a random number
    :return: random number between 1-100
    """
    return random.randint(1, 100)

def get_number_from_user() -> int:
    """
    get a number from user
    :return: number between 1-100
    """
    number =  int(input("Guess the number: [1-100] "))
    if not 1 <= number <= 100:
        print("Number is out of range")
    return number

def more_then_max(guess, max_guesses_possible):
    """

    :param guess: the input of user
    :param max_guesses_possible: 10 gueses
    :return: if user can keep guessing
    """
    if guess > max_guesses_possible:
        return True
    else:
        return False

def tell_user_if_guess_guess_higer_lower(user_number, lucky_number):
    if user_number > lucky_number:
        print('guess lower', current_guess)
    if user_number < lucky_number:
        print('guess higher', current_guess)


lucky_number = get_random_number()
current_guess = 0
max_guess = 9

while True:
    user_number = get_number_from_user()
    current_guess += 1

    if user_number == lucky_number:
            print('BINGO!!!')
            break
    if more_then_max(current_guess, max_guess):
            print('to many attempts')
            break
    tell_user_if_guess_guess_higer_lower(user_number, lucky_number)