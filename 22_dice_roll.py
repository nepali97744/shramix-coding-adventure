#22.	Write a program to simulate a dice roll

import random
def main():

    rand_dice = random.randint(1,6)
    roll(rand_dice)

def roll(a):
    if a == 1:
        print ("--------")
        print ("|      |")
        print ("|  .   |")
        print ("|      |")
        print ("--------")
    elif a == 2:
        print ("--------")
        print ("|      |")
        print ("| .  . |")
        print ("|      |")
        print ("--------")
    elif a == 3:
        print ("--------")
        print ("|.     |")
        print ("|  .   |")
        print ("|    . |")
        print ("--------")
    elif a == 4:
        print ("--------")
        print ("|.   . |")
        print ("|      |")
        print ("|.   . |")
        print ("--------")
    elif a == 5:
        print ("--------")
        print ("|.    .|")
        print ("|  .   |")
        print ("|.    .|")
        print ("--------")
    elif a == 6:
        print ("--------")
        print ("|.    .|")
        print ("|.    .|")
        print ("|.    .|")
        print ("--------")

if __name__ == "__main__":
    main()