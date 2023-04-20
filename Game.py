import random
r = "rock"
p = "paper"
s = "scissor"
def choose():
    user = input("What will you choose? Rock, Paper, or Scissors?")
    computer = random.choice(["r","p","s"])

Player_Score = 0
Computer_Score = 0

def player(player, computer):
    if (player == "r" and computer == "s") or (player == "p" and computer == "r") or (player == "s" and computer == "p"):
        Player_Score += 1 #type:ignore
        print("Nice! You just got a point!")

def computer(computer, player):
    if (computer == "r" and player == "s") or (computer == "p" and player == "r") or (computer == "s" and player == "p"):
        Computer_Score += 1 #type:ignore
        print("Ouch! Better luck next time!")

def Tie(player, computer):
    if (player == "r" and computer == "r") or (player == "p" and computer == "p") or (player == "s" and computer == "s"):
        print("It's a tie!")
        Player_Score += 0 #type:ignore
        Computer_Score += 0 #type:ignore

if Player_Score == 5:
    print("Congratulations, you have won!")

if Computer_Score == 5:
    print("Better luck next time!")