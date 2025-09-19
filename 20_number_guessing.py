# 20.	Build a number guessing game
import random


def main():
    
    rndnumber = random.randint(1,10)
    tryagain = True
    while tryagain:
        try:
            
            userInput = int(input("Please guess any number from 1 to 10: "))
            
            if userInput != rndnumber:
                print("You've got the wrong number.")
            else:
                print (f"{userInput} is the right number. You guessed correct.")
                tryagain = False
                
        except:
            print("Please only enter numbers from 1 to 10. Try again.")



    print (rndnumber, end = " ")

if __name__ == "__main__":
    main()