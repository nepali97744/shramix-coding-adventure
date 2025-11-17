#17.	Find the length of a string without using the len() function

def main():
    user_input = input("Plase enter a word to count: ")
    
    len_string(user_input)
    
    

def len_string(user_input):
    total = 0
    for _ in user_input:
        total+=1

    print (total)


if __name__ == "__main__":
    main()
