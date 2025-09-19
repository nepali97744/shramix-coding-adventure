#12.	Find the greatest common divisor (GCD) of two numbers

def main():
    num_first = int(input("Please enter first number: "))
    num_second = int(input("Please enter second number: "))

    divisor = num_first + num_second
    gcd = 1
    while divisor > gcd:
        if num_first%divisor == 0 and num_second%divisor == 0:
            print (f"{divisor} is the greatest common divisor.")
            break
        else:
            divisor = divisor-1

if __name__ == "__main__":
    main()