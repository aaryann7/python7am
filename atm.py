amount = 10000
pin = 123


pinCheck = int(input("Enter PIN"))
while pinCheck != pin:
    print("Incorrect PIN")
    pinCheck = int(input("Enter PIN"))

while True:
     
    if pinCheck == pin:
        print("\nAvailable Options")
        print("1.Withdraw Money")
        print("2.Check Balance")
        print("3.Exit")

        option = int(input("Select an option: "))
        if option == 1:
            input_money = int(input("Enter the amount you want to withdraw"))
            if input_money <= amount:
                amount -= input_money
                print(f"{input_money} withdrawn successfully")
            else:
                print("Amount exceeds balance")

    
        elif option == 2:
            print(f"Your current balance is {amount}")
        
        elif option == 3:
            print("Exited Successfully")
            break

    else:
        print("Enter a valid number")










