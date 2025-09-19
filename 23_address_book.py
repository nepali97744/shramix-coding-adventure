#23.	Build a simple address book
def main():
    

    while True:
        try:
            add_or_read = input("Do you want to add to the address book or look at the address book? Type A to add, B to look or E to exit ").lower()
            if add_or_read == "a":
                write_to_book()
            elif add_or_read == "b":
                read_from_book()
            elif add_or_read == "e":
                break
            else:
                print ("You can only select a or b. Please try again.")
        except:
            print("Please type a to add, b to look at the address book.")

def write_to_book():
    while True:
        try:
            user_name = input("Please enter your name: ")
            user_address = input("Please enter your address: ")
            add_to_address_book(user_name,user_address)
            if want_to_continue() == "y":
                continue
            else:
                break
        except:
            print("Please enter valid input.")

def read_from_book():
    with open("23_addres.txt", "r") as file:
        for line in file:
            name, address = line.strip().split(",")
            print (f"{name}, {address}")

     




def add_to_address_book(user_name, user_address):
    with open("23_addres.txt", "a") as file:
        file.write(user_name)
        file.write(",")
        file.write(user_address)
        file.write("\n")

def want_to_continue():
    return(input("Do you want to continue? (y/n) ").lower())

if __name__ == "__main__":
    main()