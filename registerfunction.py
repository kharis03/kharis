def register():
    account_name = input("Enter Account Name")
    process = True
    while process:
        pin = int(input("Enter 4 digit pin: "))
        if pin not in range (1000, 10000):
            print("Invalid Pin")
            print(f'Please try again!')
        else:
            print("Registration Successful! \n")
            process = False
            return account_name, pin 
        

        name, pin = register()
        print(name)
        print(pin)