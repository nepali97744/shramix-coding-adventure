# 13.	Convert a decimal number to binary

# repeatedly dividing the number by 2 and collecting the remainders.


def main():
    user_decimal = int(input("Please enter a number to convert to binary: "))
    final_binary = ""
    while user_decimal / 2 !=0:
        remainder = (user_decimal - user_decimal%2)//2
        temp_binary = user_decimal%2
        final_binary = str(temp_binary) + final_binary
        user_decimal = remainder

    print(final_binary)


    

if __name__ == "__main__":
    main()