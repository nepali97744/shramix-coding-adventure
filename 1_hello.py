# 1.	Hello, World!

def main():
    
    print (f"Hello, {name()}")

def name(default = "world"):
    name = input("What is your name? ")
    if name == "":
        return default
    else:
        return (name)
if __name__ == "__main__":
    main()
