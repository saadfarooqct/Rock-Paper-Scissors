import random

r = "rock"
p = "paper"
s = "scissor"

def choose():
    user = input("What will you choose? Rock, Paper, or Scissors?")
    computer = random.choice(["r","p","s"])
choose()

class Game:
    def __init__(self, player, computer, tie) -> None:
        self.player = player
        self.computer = computer
        self.tie = tie

def player(player, computer):
    if (player == "r" and computer == "s") or (player == "p" and computer == "r") or (player == "s" and computer == "p"):
        player_score += 1 #type: ignore
        print(f"You have {player_score} point(s)!")

def computer(computer, player):
    if (computer == "r" and player == "s") or (computer == "p" and player == "r") or (computer == "s" and player == "p"):
        computer_score += 1 #type: ignore
        print(f"The Computer has {computer_score} point(s)")

def tie(player, computer):
    if (player == "r" and computer == "r") or (player == "p" and computer == "p") or (player == "s" and computer == "s"):
        print("It's a tie!")
        player_score += 0 #type: ignore
        computer_score += 0 #type: ignore

if player_score == 5: #type: ignore
    print("Congratulations, you have won!")

if computer_score == 5: #type: ignore
    print("Better luck next time!")