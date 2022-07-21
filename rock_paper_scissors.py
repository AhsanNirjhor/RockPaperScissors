from pickle import TRUE
import random
user_win = 0
computer_win = 0
draw = 0
options = ["rock", "paper","scissors"]

N = input("How many time you want to play: ")
m = 0
print("\nLet's play")

while m < int(N) :
    user_input = input("Type Rock/Paper/Scissors: ")
    
    if user_input.lower() not in options :
        print("Wrong input :(")
        continue
    randompic = random.randint(0,2)
    computer_picks = options[randompic]
    print("Computer picks", computer_picks + ".")

    if user_input.lower() == "rock" and computer_picks == "scissors":
        print("You win :)")
        user_win +=1
    elif user_input.lower() == "paper" and computer_picks == "rock":
        print("You win :)")
        user_win +=1
    elif user_input.lower() == "scissors" and computer_picks == "paper":
        print("You win :)")
        user_win +=1
    elif user_input.lower() == computer_picks:
        print("Its a draw. ")
        draw +=1
    else :
        print ("Computer wins :(")
        computer_win +=1
    m +=1

print ("You won",  user_win , "times.")
print("Computer won", computer_win , "times.")
print("It was draw", draw , "times")

if user_win > computer_win:
    print("Congratulations you win the game. :)")
elif user_win == computer_win:
    print("Oh no ! it was a draw. :<")
else:
    print("Sorry ! You lost the game ")

print ("Good bye !")