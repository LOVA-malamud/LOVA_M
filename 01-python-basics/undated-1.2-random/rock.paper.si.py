import random

choice: int = ['rock', 'paper', 'sicssors']
player_choice: int = input('choose rock, paper, sicssors??')
computer_choice: int = random.choice(choice)
print(computer_choice)
if player_choice == computer_choice:
    print('its draw')
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win")
else:
    print("Computer wins")

