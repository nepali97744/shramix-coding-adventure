#18.	Print a pattern like a pyramid or diamond

def main():
    user_symbol = input("Please enter a symbol to create a diamond: ")

    length = 20

    while length > 0:
        print (user_symbol * length, end = "\n ")
        length -=2


if __name__ == "__main__":
    main()