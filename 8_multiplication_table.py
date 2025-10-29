# 8.	Print a multiplication table


def main():
    
    
    while True:
        try:
            user_input = int(input("Please enter a number you would like to generate multiplication table for: "))
            table_len = int(input("Please enter how long you want the table to be: "))

            table(user_input, table_len)
            try_again = input("Do you want to continue? (Y/N) ").lower()
            if try_again == "y":
                continue
            else:
                break

            
        except:
            print ("Please only enter numbers. Thank you, try again.")

def table(user_input, table_len):
      for i in range(table_len):
                j = i + 1
                total = user_input * j
                print(f"{user_input} * {j} = {total}")



if __name__ == "__main__":
    main()