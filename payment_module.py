import time
payment_options = {1: "cash", 2: "credit card", 3: "mobile money"}


def payment(selection,menu):   
    print("generating payment module...!")
    time.sleep(3)
    print("Here is your total bill")
    total_cost = 0
    for item in selection:
        if item in menu:
            cost = menu[item]
            print(f"{item} cost's: ${cost:.2f}")
            total_cost += cost
        else:
            print(f"item '{item}' is not in the menu") 
    print(f"Total to pay: ${total_cost:.2f}") 
    time.sleep(3)          
    def pay():
        print("select a payment option")
        for key, value in payment_options.items():
                print(f"{key}: {value}")
                
        try:
            payment_process = int(input("Enter a payment option here (1, 2, or 3):\n"))
        except ValueError:
            print("Invalid input! Please enter a number corresponding to a payment option.")
            return pay()
        if payment_process == 1:
            cash = float(input("insert the amount of cash deposited here.\n"))
            time.sleep(4)
            if cash == total_cost:       
                print("please wait while we process your payment...!")
                time.sleep(3)
                print("analizing...!")
                time.sleep(3)
                print("payment successful, have a nice day!")
                time.sleep(3)
                return selection    
            elif cash < total_cost:
                print("please wait while we process your payment...!")
                time.sleep(3)
                print("analizing...!")
                time.sleep(3)
                print("payment not successful, insufficient cash deposite!")
                return cash
            else:
                cash > total_cost
                print("please wait while we process your payment...!")
                time.sleep(3)
                print("analizing...!")
                time.sleep(3)
                print("payment successful, excessive cash deposite!")
                balance = cash - total_cost
                time.sleep(2)
                print("getting your balance...!")
                time.sleep(4)
                print(f"here is your balance:${balance}\n"
                     "have a nice day!")
                time.sleep(3)
                return selection                                 
        elif payment_process == 2:
            cash = float(input("insert your credit card and enter the amount to be paid here.\n"))
            time.sleep(4)
            if cash == total_cost:       
                print("please wait while we process your payment...!")
                time.sleep(3)
                print("analizing...!")
                time.sleep(3)
                print("payment successful, have a nice day!")
                time.sleep(3)
                return selection
            elif cash < total_cost:
                print("please wait while we process your payment...!")
                time.sleep(3)
                print("analizing...!")
                time.sleep(3)
                print("payment not successful, insufficient funds or cash withdrawal!")
                return cash
            else:
                cash > total_cost
                print("please wait while we process your payment...!")
                time.sleep(3)
                print("analizing...!")
                time.sleep(3)
                print("payment successful, excessive cash withdrawal!")
                balance = cash - total_cost
                time.sleep(2)
                print("getting your balance...!")
                time.sleep(4)
                print(f"here is your balance:${balance}\n"
                    "have a nice day!")
                time.sleep(3)
                return selection
        elif payment_process == 3:
            print("account no: 2239945754\n"
            'account mane: suncity eatry and bar\n'
            "bank: GT bank")
            cash = float(input("insert the amount of cash transferd to the above account here.\n"))
            time.sleep(5)
            if cash == total_cost:       
                print("please wait while we process your payment...!")
                time.sleep(3)
                print("analizing...!")
                time.sleep(3)
                print("payment successful, have a nice day!")
                time.sleep(3)
                return selection
            elif cash < total_cost:
                print("please wait while we process your payment...!")
                time.sleep(3)
                print("analizing...!")
                time.sleep(3)
                print("payment not successful, please tranfere your remaing balance!")
                balance_display = total_cost - cash
                time.sleep(3)
                print(f"here is the remaing balance to be paid:+ ${balance_display}")
                remaing_balance = float(input("enter the remaing balance transfered here.\n"))
                repay = remaing_balance + cash
                if repay == total_cost:
                    print("please wait while we process your payment...!")
                    time.sleep(3)
                    print("analizing...!")
                    time.sleep(3)
                    print("payment successful, have a nice day!")
                else:
                    print("please we can not conduct such irregular transactions. and have to contact the security management.")
                    time.sleep(2)    
                    print("calling the security management...!")
            else:
                cash > total_cost
                print("please wait while we process your payment...!")
                time.sleep(3)
                print("analizing...!")
                time.sleep(3)
                print("payment successful, excessive cash tranfer!")
                balance = cash - total_cost
                time.sleep(2)
                print("getting your balance...!")
                time.sleep(4)
                print(f"here is your balance:${balance}\n"
                    "have a nice day!")
                time.sleep(3)
                return selection
        elif not payment_process.strip():
            print("please! enter a payment option")
            return pay()
        else:
            print("please! enter a valid payment option")  
            return pay()                       
    pay()


    return       