import random
import string
def generate_password(min_length,numbers,special_characters) :
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    
    characters=letters
    if numbers:
        characters+=digits
    if special_characters :
        characters+=special
    pasw=""
    meets_criteria=False
    has_number=False
    has_special=False
    
    while not meets_criteria or len(pasw)<min_length :
        new_char=random.choice(characters)
        pasw+=new_char
        
        if new_char in digits:
            has_number=True
        if new_char in special:
            has_special=True
        meets_criteria = True
        if numbers:
            meets_criteria=has_number
        if special_characters :
            meets_criteria = meets_criteria and has_special
        
    return pasw
min_length=int(input("Enter the minimum Length: "))
has_number=input("Do you want to have numbers?(y/n) :  ").lower()=='y'
has_special = input("Do you want to have special characters?(y/n) :  ").lower()=='y'
print("Your generated password : ",generate_password(min_length,has_number,has_special))
    