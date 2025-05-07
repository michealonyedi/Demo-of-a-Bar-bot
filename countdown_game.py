import random
import time


def countdown():
    print("welcome to the countdown game")
    time.sleep(1)
    print("thinking of a number")
    random_number = random.randint(1, 30)
    count = 10
    while True:
        try:
            guess = int(input("enter the number guessed here  range 1 to 30\n"))
            count -= 1
            if count > 0:
                if guess < random_number:
                    print("analyzing...!")
                    time.sleep(1)
                    print(" the number is below the guessed value")
                elif guess > random_number:
                    print("analyzing...!")
                    time.sleep(1)
                    print("the number is above the guessed value")
                else:
                    print("analyzing...!")
                    time.sleep(1)
                    print(f"congratulations! you are correct and within the countdown of {count}")
                    break
            else:
                print(f" you have failed! the correct nuber is  {random_number}.")
                break

        except ValueError:
            print("enter a valid number")
    return


