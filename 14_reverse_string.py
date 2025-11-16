#14.	Reverse a string

def main():
    
    
    while True:
        try:
            user_input = input("Please enter a word you want reversed: ")
            reversed(user_input)
            continue_again = input("Do you want to continue? (Y/N): ").lower()
            
            while True:

                if continue_again == "y":
                    break
                elif continue_again == "n":
                    return ("Thank you for playing.")
                else:
                    continue_again = input("Please type either y to continue or n to exit: ").lower()
        except:
            print("Please enter a valid word.")


    



def reversed(user_input):
    
    while user_input == "":
        print("Please enter a word.")
        break
    else:

        reversed_word = ""
        for _ in user_input:
            reversed_word = _ + reversed_word
        
        print (reversed_word)

if __name__ == "__main__":
    main()