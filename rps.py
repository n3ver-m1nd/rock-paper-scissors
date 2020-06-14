import random

pc = random.choice(["rock", "paper", "scissors"])

class Player:
    def __init__(self, rdy, choise):
        self.rdy = rdy
        self.choise = choise

player = Player(True, input("Rock, paper or scissors? "))

while player.rdy == True:
    if pc == player.choise:
        print("Draw!")
    elif player.choise == "rock":
        if pc == "paper":
            print("You lose!")
            
        else:
            print("You win!")

    elif player.choise  == "paper":
        if pc == "scissors":
            print("You lose!")
        else:
            print("You win!")

    elif player.choise  == "scissors":
        if pc == "rock":
            print("You lose!")
        else:
            print("You win!")

    else:
        print("Invalid input")

    break



