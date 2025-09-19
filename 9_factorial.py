# 9.	Find the factorial of a number


def main():
    
    while True:
        try:
            user_input = int(input("Enter a number to find factorial of: "))
            total = 1 
            for i in range(user_input):
                total = (i+1) * total
               
            print (total)
            break
        except:
            print ("Please only enter valid number. Please try again.")

if __name__ == "__main__":
    main()

    