# Rock, Paper, Scissors
import random

# Have user select rock, paper or scissors

# Have Program select rock(1), paper(2) or scissors(3)
action = random.randint(1, 3)


print(f"\nWelcome To Rock, Paper, Scissors!")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
user = int(input("Please choose Rock, Paper or Scissors (1-3) "))

# results
while True:
    if action == 1 and user == 1:
        print("You both selected Rock! Tie Game!")
        break
    elif action == 1 and user == 2:
        print("You Won! Paper Covers Rock!")
        break
    elif action == 1 and user == 3:
        print("You Lost! Rock Crushes Scissors")
        break
    elif action == 2 and user == 3:
        print("You Won! Scissors cuts Paper!")
        break
    elif action == 2 and user == 2:
        print("You both selected Paper! Tie game!") 
        break
    elif action == 2 and user == 1:
        print("You Lost! Paper Covers Rock!")
        break
    elif action == 3 and user == 1:
        print("You Won! Rock smashes Scissors!")
        break
    elif action == 3 and user == 2:
        print("You Lost! Paper Covers Rock")    
        break
    elif action == 3 and user == 3:
        print("You both selected Scissors! Tie Game!")    
        break
    else:
        print("Please make a valid selection!")