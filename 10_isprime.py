# 10.	Check if a number is prime

def main():
    user_input = int(input("Enter a number to check if it's a prime number: "))

    for i in range(2, user_input-1):
        if user_input % (i) == 0:
            break
    else:
        print ("is prime")
        
        
    

if __name__ == "__main__":
    main()