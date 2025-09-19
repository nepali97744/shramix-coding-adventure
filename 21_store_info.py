#21.	Create a program to store and manage student information (name, age, grades)
def main():
    
    
    
    while True:
        try:
            std_name = input("Please enter your name: ")
            std_age = int(input("Please enter your age: "))
            std_grade = input("Please enter your grade: ")
            write_to_file(std_name,std_age,std_grade)
            if add_another() == "y":
                continue
            else:
                break
        except ValueError:
            print ("Please only type number for your age.")
        except:
            print ("Please try again.")




def write_to_file(name,age,grade):
    with open("21info.txt", "a") as file:
        file.write(name)
        file.write(",")
        file.write(str(age))
        file.write(",")
        file.write(grade)
        file.write("\n")

def add_another():
    ans = input ("Do you want to add another student? (y/n): ").lower()
    return ans




if __name__ == "__main__":
    main()