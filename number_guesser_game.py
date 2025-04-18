import random
print("Welcome to the Number Guessing Game!")
print
top=input("Enter the max number: ")
if top.isdigit():
    top=int(top)
    if top<=0:
        print("Please enter a number greater than 0.")
        quit()
   
r=random.randint(0,top)
guesses=0
while True:
    guess = input("Guess a number between 0 and "+str(top)+" : ")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("Please enter a number.")
        continue
    guesses+=1
    if guess==r:
        print("You got it!And it took you",guesses,"guesses.")
        break
    elif guess<r:
        print("Too low.")
    
    else:
        print("Too high.")
        
    



