import random
import time
from words import word_list
user_name = input("Enter Your Name : ")
time.sleep(1)
print(f"\t\t ****** Welcome {user_name} ***** \n\n")

# generating random word from list word_list
random_word = random.choice(word_list)
random_word = random_word.upper()
#print(random_word)
n = len(random_word)

for dash in range(n):
    print("_",end="  ")
    print("\n")
    
    
guessed_letter = [] # contains  all the guessed words 
attempt = 10
is_correct_word = False

while attempt>0:
    print("\nTotal Trials left : ",attempt)
    print("\n----*--------*--------*--------*--------*--------*--------*--------*\n")
    get_char = input("Guess the Single Character : ").upper()
    
    if(len(get_char)==1):
        if get_char in guessed_letter:
            print(f"\n{get_char} is Already Guessed\n")
        elif get_char in random_word:
            print("\nWell done ...Correct Guess \n")
            guessed_letter.append(get_char)
        elif get_char not in random_word:
            print("\nWrong Guess :(\n")
            guessed_letter.append(get_char)
            attempt-=1
    else:
        print("\nEnter Only Single Character \n")
                
    status = ''        
    if is_correct_word==False:
        for letter in random_word:
            if letter in guessed_letter:
                status = status+letter
            else:
                status = status+"_  "
        
        print("this is status now : ",status)
        
    if status == random_word:
        print("\n\t\t\t YOU WIN :)\n")
        break
    elif status!=random_word and attempt<=0:
        print("\n\t\t\t YOU LOSE :(\n")
        print("The Correct Word is : ",random_word.upper())
            
            