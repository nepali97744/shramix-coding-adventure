# 10.	Check if a number is prime

def main():
    

    while True:
        try:
            user_input = int(input("Enter a number to check if it's a prime number: "))
            print(is_prime(user_input))

            try_again = input("Do you want to continue? (Y/N): ").lower()
            if try_again == "y":
                continue
            else:
                break
        except:
            print("Please only enter a valid number. ")

def is_prime(user_input):
    for i in range(2, user_input-1):
        if user_input % (i) == 0:
            return (f"{user_input} is not a prime number.")
            
    else:
        return (f"{user_input} is a prime number.")
        
    

if __name__ == "__main__":
    main()