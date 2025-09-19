# 3.	Calculate the area of a triangle area = 1/2 * b * h


def main():
    while True:
        try:
            height = int(input("Enter height of the triangle: "))
            base = int(input("Enter base of triangle: "))
            
            area_of_triangle = 0.5 * base * height

            print (f"Area of triangle is {area_of_triangle}")
            break
        
        except:
            print ("You can only enter a whole number.")

if __name__ == "__main__":
    main()