#17.	Find the length of a string without using the len() function

def main():
    
    
    while True:
        try:
            user_input = input("Plase enter a word to count: ")
            len_string(user_input)
            
            if try_again():
                pass
            else:
                break
            
        except:
            print("Please enter a valid input.")
    
    

def len_string(user_input):
    total = 0
    for _ in user_input:
        total+=1

    print (total)

def try_again():
    while True:
        user_input = input("Do you want to continue? (Y/N): ").lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            print ("Thank you for playing.")
            return False
        else:
            print("Please type Y to continue or N to exit.")

if __name__ == "__main__":
    main()
