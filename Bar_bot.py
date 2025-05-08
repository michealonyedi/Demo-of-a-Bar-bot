import time
from number_guessing_game import guess_the_number
from countdown_game import countdown
from payment_module import payment


game = ["number quessing game","countdown game"]
menu = {"smoothie": 20.70, "Mcdowels": 73.65, "coktail": 98.20, "beer": 5.43, "wine": 61.76,
         "vodka": 47.00, "wiskey": 100.00,
         "palmwine" : 7.20, "soft_drink": 3.00, "water": 1.00,  "juice": 10.00, "tea": 2.60}
def greetings():
    print("greetings! our distingushed customer.")
    time.sleep(3)
    print("welcome to suncity eatry and bar")
    time.sleep(3)
    print("please! what is your name sir?")
    name = input("enter your name here for future recognition:\n")
    time.sleep(2)
    print(f"welcome {name}! to suncity eatry and bar")


greetings()


def offer():
    print("what would you want us to offer you?\n"" some drinks? or play some games?")
    time.sleep(3)
    option = input("please! enter YES,NO for drink requent or GAMES to play some games\n").lower()
    if option == "yes":
        print(f"Here is our menu:")
        for item, price in menu.items():
          print(f"{item}: ${price:.2f}")
        time.sleep(3)
        selection = [items.strip() for items in input("enter your order here (comma-saperated):\n").split(',')]
        for item in selection:
            if item in menu:
               print("few munites please. getting your order ready....!")
               time.sleep(4)
               print(f"here is your order:{selection}")
               time.sleep(2)
               print("will be back with your bills for payment.")
               time.sleep(6)
               payment(selection,menu)
            else:
                print("we do not have that in stock.")
                return offer()   
    elif option == "no":
        print(f"okay! would be waiting if you make a change of mind")
        time.sleep(2)
        return offer()
    elif option == "games":
        print("what type of game do you want to play?")
        time.sleep(3)
        print(f"available games:{game}")
        time.sleep(2)
        enter = input("enter the game you want to play from the list of available games\n")
        if enter in game:
            if enter == "number guessing game":
                print("here we go")
                guess_the_number()
            elif enter == "countdown game":
                print("lets do it!")
                countdown() 
        elif not enter.strip():
            print("enter an input") 
            return enter     
        else:
            print("enter a valid input")
            return enter
    elif not option.strip():
           print("enter an input") 
           return option               
    else:
        print("please enter a valid input.")
        return option
    
             
offer()