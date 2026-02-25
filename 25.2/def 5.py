import random
import time


def get_user_choice() -> str:
    """
    get choice from user until got a valid choice
    :return:  str - 'rock', 'paper', 'scissors'
    """
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice


def get_random_computer_choice() -> str:
    """
    random 1 options from 'rock', 'paper', 'scissors'
    :return:  str - 'rock', 'paper', 'scissors'
    """
    return random.choice(["rock", "paper", "scissors"])


def print_user_choice_icon_and_delay(choice, how_long_sleep) -> None:
    """
    print the user choice + icon and sleep 2-3
    :param choice:  str - 'rock', 'paper', 'scissors'
    :param how_long_sleep:  how long sleep in seconds
    :return: None
    """
    print(f"You chose {choice} {ICONS[choice]}")
    time.sleep(how_long_sleep)
    pass


def print_computer_choice_icon(choice) -> None:
    """
    print computer choice + icon
    :param choice:  str - 'rock', 'paper', 'scissors'
    :return:
    """
    print(f"Computer chose {choice} {ICONS[choice]}")
    pass


def get_game_result(user_choice, computer_choice) -> str:
    """

    :param user_choice:  str - 'rock', 'paper', 'scissors'
    :param computer_choice: str - 'rock', 'paper', 'scissors'
    :return: str winner - 'user', 'draw', 'computer'
    """
    if user_choice == computer_choice:
        return "draw"

    if (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"


def print_result_and_icon(get_result) -> None:
    """
    👋 💥🤝✅
    Print result with icon
    :param get_result: str winner - 'user', 'draw', 'computer'
    :return: None
    """
    if get_result == "draw":
        print("draw")
    elif get_result == "user":
        print("user wins")
    else:
        print("computer wins")


# Icons for each choice
ICONS = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
}

print("🎮 Rock–Paper–Scissors")

user_choice = get_user_choice()
print_user_choice_icon_and_delay(user_choice, 1)
computer_choice = get_random_computer_choice()
print_computer_choice_icon(computer_choice)
get_result = get_game_result(user_choice, computer_choice)
print_result_and_icon(get_result)
