# 5.	Find the largest among three numbers

def main():
    while True:
        try:
            first_num, second_num, third_num = input("Please enter three numbers followed by a comma: ").split(",")

            num_list = [first_num, second_num,third_num]
            converted_list = []
            for i in num_list:
                new_int = int(i)
                converted_list.append(new_int)

            sorted_list = sorted(converted_list, reverse=True)
            print(sorted_list[0])
            break
                


        except:
            print ("You can only enter numbers to sort. Please try again.")

   

if __name__ == "__main__":
    main()