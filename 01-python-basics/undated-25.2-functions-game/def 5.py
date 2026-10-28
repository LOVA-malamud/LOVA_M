import random
import time


def get_user_choice() -> str:
    """Get choice from user until got a valid choice.
    
    Returns:
        str: 'rock', 'paper', or 'scissors'
    """
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice


def get_random_computer_choice() -> str:
    """Get random choice from 'rock', 'paper', 'scissors'.
    
    Returns:
        str: 'rock', 'paper', or 'scissors'
    """
    return random.choice(["rock", "paper", "scissors"])


def print_user_choice_icon_and_delay(choice: str, how_long_sleep: float) -> None:
    """Print the user choice with icon and delay.
    
    Args:
        choice: 'rock', 'paper', or 'scissors'
        how_long_sleep: How long to sleep in seconds
    """
    print(f"You chose {choice} {ICONS[choice]}")
    time.sleep(how_long_sleep)


def print_computer_choice_icon(choice: str) -> None:
    """Print computer choice with icon.
    
    Args:
        choice: 'rock', 'paper', or 'scissors'
    """
    print(f"Computer chose {choice} {ICONS[choice]}")


def get_game_result(user_choice: str, computer_choice: str) -> str:
    """Determine the game result.
    
    Args:
        user_choice: 'rock', 'paper', or 'scissors'
        computer_choice: 'rock', 'paper', or 'scissors'
        
    Returns:
        str: 'user', 'draw', or 'computer'
    """
    if user_choice == computer_choice:
        return "draw"

    winning_conditions = [
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper")
    ]
    
    if (user_choice, computer_choice) in winning_conditions:
        return "user"
    else:
        return "computer"


def print_result_and_icon(game_result: str) -> None:
    """Print result with appropriate message.
    
    Args:
        game_result: 'user', 'draw', or 'computer'
    """
    if game_result == "draw":
        print("It's a draw!")
    elif game_result == "user":
        print("You win! 🎉")
    else:
        print("Computer wins! 🤖")


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
game_result = get_game_result(user_choice, computer_choice)
print_result_and_icon(game_result)
