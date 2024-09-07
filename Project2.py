import random
print("Welcome to Rock Paper Scissors Game")

options = ("rock","paper","scissors")
player = None
computer_choice = random.choice(options)
input("1--> rock  2--> paper  3--> scissors")
player = int(input("Enter your choice:"))



if(player ==1):
    player_choice = "rock"
    print("Player's choice : Rock")
     
elif(player ==2):
    player_choice = "paper"
    print("Player's choice : Paper")

elif(player ==3):
    player_choice = "scissors"
    print("Player's choice: Scissors")
else:
    print("Invalid choice")
    exit()

print("Computer's choice:",computer_choice)

if player_choice == computer_choice:
    print("It's a tie")
elif player_choice =="rock" and computer_choice =="scissors":
    print("You won !!")
elif player_choice =="paper" and computer_choice == "rock" :
    print("You won !!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You won !!")

else:
    print("Computer won!!")