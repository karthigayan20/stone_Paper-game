######### ROCK ,PAPER & SCISSIOR #########
import random

game_images=[rock,paper,scissors]
user_choice=input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.")
if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number,you lose!")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("Computer chose:")
    print
