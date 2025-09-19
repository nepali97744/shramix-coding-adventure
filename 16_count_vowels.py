# 16.	Count the number of vowels in a string

def main():
    user_word = input ("Please enter word to find out how many vowels there are in it: ").lower()

    vowels = "aeiou"
    count = 0
    for c in user_word:
        if c in vowels:
            count+=1
    print (count)
       


if __name__ == "__main__":
    main()