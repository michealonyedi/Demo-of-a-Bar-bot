import random
import time


def guess_the_number():
    number_to_guess = random.randint(1, 100)
    counter = 0
    print("i am thinking of a number from 1 to 100")
    time.sleep(3)
    print("can you make a guess of what it is?")
    while True:
        try:
            guess = int(input("enter the number guessed here.\n "))
            counter += 1
            if guess < number_to_guess:
                print("analyzing....!")
                time.sleep(3)
                print("the number is below")
            elif guess > number_to_guess:
                print("analyzing....!")
                time.sleep(3)
                print("the number is above")
            else:
                print("analyzing....!")
                time.sleep(3)
                print(f"correct! you have guessed the number right in {counter} times")
                break
        except TypeError:
            print("enter a valid number")
    return
