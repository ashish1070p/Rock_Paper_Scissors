import random

choices = ["rock", "paper", "scissors"]

def winner(user_selection, computer_selection):
    result = ""
    user_selection = user_selection.lower()
    computer_selection = computer_selection.lower()
    print("You Selected! " + user_selection)
    print("Computer Selected! " + computer_selection)
    if user_selection == computer_selection:
        result = "Tie!!"
    elif user_selection =="rock" and computer_selection == "scissors":
        result = "You win"
    elif user_selection =="rock" and computer_selection == "paper":
        result = "Computer win"
    elif user_selection =="paper" and computer_selection == "scissors":
        result = "Computer win"
    elif user_selection =="paper" and computer_selection == "rock":
        result = "You win"
    elif user_selection =="scissors" and computer_selection == "rock":
        result = "Computer Wins"
    elif user_selection =="scissors" and computer_selection == "paper":
        result = "We Win"
    return result

while True:
    print("Rock? Paper? or Scissors?", end="")
    selection = input()
    if selection.lower() not in choices:
        continue
    computer_selection = random.choice(choices)
    print(winner(selection,computer_selection))

    print("Do you wanna continue(Yes/No)" ,end="")
    end_selection = input()
    end_selection = end_selection.lower()
    if end_selection == "yes":
        continue
    else:
        print("Thank you for playing")
        break






