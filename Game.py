import random

r = "rock"
p = "paper"
s = "scissor"

player_score = 0
computer_score = 0

for i in range(6):
    if i == 5:
        if player_score > computer_score:
            print("Congratulations, you have won!\n")
        else:
            print("Better luck next time!\n")
            break

    user_choice = input("What will you choose? Rock, Paper, or Scissors? \n")
    computers_choice = random.choice(["r","p","s"])

    if (user_choice == "r" and computers_choice == "s") or (user_choice == "p" and computers_choice == "r") or (user_choice == "s" and computers_choice == "p"):
        player_score += 1
    elif(user_choice == "r" and computers_choice == "p") or (user_choice == "p" and computers_choice == "s") or (user_choice == "s" and computers_choice == "r"):
        computer_score += 1
    elif(user_choice == "r" and computers_choice == "r") or (user_choice == "p" and computers_choice == "p") or (user_choice == "s" and computers_choice == "s"):
        print("It's a tie! \n")

    print(f"Your score is: {player_score}")
    print(f"The computer's score is: {computer_score}")