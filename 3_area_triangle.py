# 3.	Calculate the area of a triangle area = 1/2 * b * h


def main():
    while True:
    
        
        
        area_of_triangle = 0.5 * height() * base()

        print (f"Area of triangle is {area_of_triangle}")
        break
        

def height():
    while True:
        try:
            return(int(input("Enter height of the triangle: ")))
        except:
            print ("You can only enter a whole number. Please enter height again.")

def base():
    while True:
        try:
            return(int(input("Enter base of the triangle: ")))
        except:
            print("You can only enter a whole number. Please enter base again.")

if __name__ == "__main__":
    main()