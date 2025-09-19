#14.	Reverse a string

def main():
    user_input = input("Please enter a word you want reversed: ")
    reversed_word = ""

    for _ in user_input:
        reversed_word = _ + reversed_word

    print (reversed_word)



if __name__ == "__main__":
    main()