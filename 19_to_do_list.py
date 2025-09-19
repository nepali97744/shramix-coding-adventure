# 19.	Create a simple to-do list program

def main():
    # prompt user for things to add to list until they type exit
    # add the user input to a list and then display it at the end.

    user_list = []
    while True:
        user_input = input("Please enter items you want to add to list, type exit to finish entering: ").lower()
        if user_input != "exit":
            user_list.append(user_input)
        else:
            print("Please find your todo list below:")
            break
    
    for _ in user_list:
        print (_)



if __name__ == "__main__":
    main()