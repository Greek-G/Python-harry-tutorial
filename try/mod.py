import pyttsx3
engine = pyttsx3.init()
import random

choices = {"r": -1, "p": 1, "s": 0}  # 'r=Rock, 'p'=Paper, 's'=Scissors
computer = random.choice([-1, 0, 1])  #storing npc input

engine.say("Enter your choice")
engine.runAndWait()
youstr = input("Enter your choice (r = Rock, p = Paper, s = Scissors): ")
you = choices.get(youstr)  #storing user input

if you is None:   #Checking ipnt
    print("Invalid input! Please choose 'r', 'p', or 's'.")
else:  #declaring result
    print(f"Computer chose: {['rock', 'paper', 'scissor'][computer + 1]}")
    if computer == you:
        print("It's a draw!")
        engine.say("its draw play again")
        engine.runAndWait()
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
         print("You win!")
         engine.say("Excellent you win")
         engine.runAndWait()
    else:
        print("You lose!")
        engine.say("you lose try again")
        engine.runAndWait()

