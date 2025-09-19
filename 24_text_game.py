#24.	Implement a basic text-based adventure game
# this is a hangman game with list of countries
import random


def main():
    
    total_countries = []
    import_country_list(total_countries)
    computer_selection_num = random.randint(0,len(total_countries)-1)
    computer_selection_country = total_countries[computer_selection_num]
    print(computer_selection_country)
    user_input(computer_selection_country)
    
    
def user_input(secret_word, count=10):
    display_word =["-"]*len(secret_word)
    while count > 0:
        print(" ".join(display_word))
        user_input = input("This is a hangman game. Please guess the name of the country one letter at a time. You will get a total of 10 tries: ").strip().upper()
        
        if user_input in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == user_input:
                    display_word[i] = user_input
                    if "".join(display_word) == secret_word:
                        print("You've successfully guessed the country name. Congratulations")
                        count = 0
            
            
            
        else:
            count -=1
            print(count)







def raw_country_list(total_countries):
    with open("24_list_of_countries.txt", "r") as file:
        for countries in file:
            newlist = countries.strip().upper()
            if newlist !="":
                total_countries.append(newlist)


def clean_country_list(total_countries):    
    with open("24_list_of_countries.txt", "w") as file:
        for country in total_countries:
            formatted_country = country.strip().upper()
            file.write(formatted_country)
            file.write("\n")
        
def import_country_list(total_countries):
    with open("24_list_of_countries.txt", "r") as file:
        for country in file:
            formatted_country = country.strip().upper()
            total_countries.append(formatted_country)








if __name__ == "__main__":
    main()