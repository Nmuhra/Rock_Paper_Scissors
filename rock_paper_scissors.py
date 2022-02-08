from pickle import TRUE
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock,paper,scissors]
def new_func():
    choices = ["rock", "paper", "scissors"]
    return choices

while True:
    choices = new_func()

    computer = random.choice(choices)
    player = None

    while player not in choices:
          player = int(input("0 for rock, 1 for paper, 2 for or scissors?: "))
    print(images[player])
    if player == computer:
     print("computer: ",computer)
     print("player: ", player)
     print("Draw")

    elif player =="rock":
        if computer == "paper":
         print("computer: ",computer)
         print("player", player)
         print("you lose :(")

    elif player =="rock":
        if computer == "scissors":
         print("computer: ",computer)
         print("player", player)
         print("you win :)")

    elif player =="paper":
        if computer == "scissors":
         print("computer: ",computer)
         print("player", player)
         print("you lose :(")   

    elif player =="paper":
        if computer == "rock":
         print("computer: ",computer)
         print("player", player)
         print("you win :)")

    elif player =="scissors":
        if computer == "rock":
         print("computer: ",computer)
         print("player", player)
         print("you lose :(")

    elif player =="scissors":
        if computer == "paper":
         print("computer: ",computer)
         print("player", player)
         print("you win :)")

    play_again = input("wanna go again? (yes/no): ").lower()
    
    if play_again !="yes":
        break

print("Bye!")
