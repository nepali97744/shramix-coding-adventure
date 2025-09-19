# 15.	Check if a string is a palindrome

def main():
    user_word = input("Please enter a word to check if it's a palindrome: ").lower()

    word_holder = "".join(reversed(user_word))

    if user_word == word_holder:
        print(f"{user_word} is a palindrome.")
    else:
        print (f"{user_word} is not a plaindrome.")




if __name__ == "__main__":
    main()