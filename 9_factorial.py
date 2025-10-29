# 9.	Find the factorial of a number


def main():
    
    while True:
        try:
            user_input = int(input("Enter a number to find factorial of: "))
            total = 1 
            
            factorial_finder(user_input, total)

            try_again = input("Do you want to continue? (Y/N): ").lower()

            if try_again == "y":
                continue
            else:
                break



        except:
            print ("Please only enter valid number. Please try again.")

def factorial_finder(user_input, total):
    for i in range(user_input):
        total = (i+1) * total
               
    print (total)
            



if __name__ == "__main__":
    main()

    