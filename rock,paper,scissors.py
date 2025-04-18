import random
print("Welcome to Rock, Paper, Scissors!")
options=["rock","paper","scissors"]
user_wins=0
computer_wins=0
while True :
    user_input=input("Enter your choice: rock,paper,scissors or type q to quit : ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        print("Please enter a valid choice.")
        continue
    computer_choice=random.choice(options)
    print("Computer chose:",computer_choice)
    if user_input==computer_choice:
        print("It's a tie!")
    elif user_input=="rock" and computer_choice=="scissors":
        user_wins+=1
        print("You win!")
    elif user_input=="paper" and computer_choice=="rock":
        user_wins+=1
        print("You win!")
    elif user_input=="scissors" and computer_choice=="paper":
        user_wins+=1
        print("You win!")
    else:
        computer_wins+=1
        print("You lose!")   
        
print("You have",user_wins,"wins and the computer has",computer_wins,"wins.")
print("Goodbye! See you next time!")
        
        
        
        
    