# 4.	Convert Celsius to Fahrenheit °F = °C * 9/5 + 32

def main():
    print ("This program converts your celcius into farenheit.")
    
    while True:
        try:
            user_celcius = float(input("Please enter the number you want to convert: "))

            converted_farenheit = (user_celcius * (9/5) + 32)
            print (f"{user_celcius} celcius is equal to {converted_farenheit:.2f} farenheit.")
            break
        except ValueError:
            print ("Please only enter a valid number.")





if __name__=="__main__":
    main()

