import random

choices = {"r": -1, "p": 1, "s": 0}  # 's' -> Rock, 'w' -> Paper, 'g' -> Scissors
computer = random.choice([-1, 0, 1])  

youstr = input("Enter your choice (r = Rock, p = Paper, s = Scissors): ")
you = choices.get(youstr)

if you is None:
    print("Invalid input! Please choose 'r', 'p', or 's'.")
else:
    print(f"Computer chose: {['rock', 'paper', 'scissor'][computer + 1]}")
    if computer == you:
        print("It's a draw!")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print("You win!")
    else:
        print("You lose!")
