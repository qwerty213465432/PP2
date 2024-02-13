import random

def guess():

    num = random.randint(1, 20)

    print("Hello! What is your name?")

    name = input()

    print("Well,", name,  ", I am thinking of a number between 1 and 20.")

    yng = 0

    while True:
        print("Take a guess.")
        
        yg = int(input())

        yng += 1

        if yg < num:
            print("Your guess is too low.")
        elif yg > num:
            print("Your guess is too high.")
        else:
            print("Good job, ", name, "! You guessed my number in ", yng, "guesses!")
            break




guess()
