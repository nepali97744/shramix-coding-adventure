# 8.	Print a multiplication table


def main():
    
    
    while True:
        try:
            user_input = int(input("Please enter a number you would like to generate multiplication table for: "))
            table_len = int(input("Please enter how long you want the table to be: "))

            for i in range(table_len):
                j = i + 1
                total = user_input * j
                print(f"{user_input} * {j} = {total}" )
            break
        except:
            print ("Please only enter numbers. Thank you, try again.")



if __name__ == "__main__":
    main()