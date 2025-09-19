# 6.	Check if a number is even or odd

def main():
    while True:  
        try:
            user_input = int(input("Enter a number: "))
            if is_even(user_input):
                print (f"{user_input} is even.")
                break
            else:
                print (f"{user_input} is odd.")
                break
        except:
            print ("Please enter a number.")

    
def is_odd(a):
    return True if a%2 !=0 else False

def is_even(a):
    return True if a%2 == 0 else False
    


if __name__ == "__main__":
    main()