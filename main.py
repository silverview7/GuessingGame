from random import randrange

randNum = randrange(50)
attempts = 0
print("Welcome to guessing game")
print("In this game you must guess a number from 0 to 49")
print("Each time you attempt a number you will be given a hint")
print("You have 5 attempts.")
print("Good Luck!")

while attempts <= 4:
    try:
        user_integer = input("Enter an integer: ")
        user_integer = int(user_integer)
        if user_integer < randNum:
            print("The number is greater than " + str(user_integer))
        elif user_integer > randNum:
            print("The number is less than " + str(user_integer))
        else:
            print("You guessed the correct number!")
            break
        attempts += 1
        print("You have " + str(5-attempts) + " remaining.")

    except ValueError:
        print("You must enter a valid integer!")

print("The correct number was: " + str(randNum))
print("Thanks for playing guessing game hope to see you soon!")
