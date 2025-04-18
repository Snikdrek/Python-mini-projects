print("hey there! Welcome to my quiz game!!")
choice=input("Do you want to play? Type (yes/no): ")
choice=choice.lower()
score=0
tot=0
if choice=="no":
    print("o oh! Maybe next time!")
    exit()
elif choice=="yes":
    print("Great! Let's start")
    print("Question 1: What is the capital of France?")
    print("A. Madrid")
    print("B. Paris")
    print("C. Rome")
    print("D. London")
    answer=input("Enter your answer: ")
    answer=answer.lower()
    tot+=1
    if answer=="b":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("Question 2: What is the capital of Spain?")
    print("A. Madrid")
    print("B. Paris")
    print("C. Rome")
    print("D. London")
    answer=input("Enter your answer: ")
    answer=answer.lower()
    tot+=1
    if answer=="a":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("Question 3: What is the capital of Italy?")
    print("A. Madrid")
    print("B. Paris")
    print("C. Rome")
    print("D. London")
    answer=input("Enter your answer: ")
    tot+=1
    answer=answer.lower()
    if answer=="c":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("Question 4: What is the capital of England?")
    print("A. Madrid")
    print("B. Paris")
    print("C. Rome")
    print("D. London")
    answer=input("Enter your answer: ")
    answer=answer.lower()
    tot+=1
    if answer=="d":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("Question 5: What is the capital of Germany?")
    print("A. Madrid")
    print("B. Paris")
    print("C. Berlin")
    print("D. London")
    answer=input("Enter your answer: ")
    answer=answer.lower()
    tot+=1
    if answer=="c":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("Question 6: What is the capital of Russia?")
    print("A. Madrid")
    print("B. Moscow")
    print("C. Rome")
    print("D. London")
    answer=input("Enter your answer: ")
    answer=answer.lower()
    tot+=1
    if answer=="b":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("Question 7: What is the capital of India?")
    print("A. Madrid")
    print("B. Paris")
    print("C. Rome")
    print("D. New Delhi")
    answer=input("Enter your answer: ")
    answer=answer.lower()
    tot+=1
    if answer=="d":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("Question 8: What is the capital of China?")
    print("A. Madrid")
    print("B. Paris")
    print("C. Beijing")
    print("D. London")
    answer=input("Enter your answer: ")
    answer=answer.lower()
    tot+=1
    if answer=="c":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("Question 9: What is the capital of Japan?")
    print("A. Madrid")
    print("B. Paris")
    print("C. Rome")
    print("D. Tokyo")
    answer=input("Enter your answer: ")
    answer=answer.lower()
    tot+=1
    if answer=="d":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    print("Question 10: What is the capital of Australia?")
    print("A. Madrid")
    print("B. Paris")
    print("C. Canberra")
    print("D. London")
    answer=input("Enter your answer: ")
    answer=answer.lower()
    tot+=1
    if answer=="c":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
    
    print("Your score is: ",score,"/",tot)
    print("Thank you for playing!")
else:
    print("Invalid input! Please try again!")
    
    