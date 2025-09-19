# 25.	Create a program to read and write data to a file

def main():
    while True:
        try:
            add_more = input("Type A to add more names, R to read the list of name and E to exit: ").strip().upper()
            if add_more == "A":
                write_to_file()
            elif add_more == "R":
                read_from_file()
            elif add_more == "E":
                break
            else:
                print("Please only select from the following options: A to add more names, R to read from file and E to exit.")
        except:
            print("Please only select from the following options: A to add more names, R to read from file and E to exit.")



def write_to_file():
    with open("25_file.txt", "a") as file:
        name = input("What's your name? ").strip().upper()
        file.write(name)
        file.write("\n")

def read_from_file():
    with open("25_file.txt") as file:
        for line in file:
           
            print(f"Hi, my name is {line}", end = "")



if __name__ == "__main__":
    main()