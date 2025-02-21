import random

choices = {"r": -1, "p": 1, "s": 0}  # 'r=Rock, 'p'=Paper, 's'=Scissors
computer = random.choice([-1, 0, 1])  #storing npc input

youstr = input("Enter your choice (r = Rock, p = Paper, s = Scissors): ")
you = choices.get(youstr)  #storing user input

if you is None:   #Checking ipnt
    print("Invalid input! Please choose 'r', 'p', or 's'.")
else:  #declaring result
    print(f"Computer chose: {['rock', 'paper', 'scissor'][computer + 1]}")
    if computer == you:
        print("It's a draw!")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print("You win!")
    else:
        print("You lose!")
