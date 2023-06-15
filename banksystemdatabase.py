bank_users = {'saif':123,'mamun':12354,'arif':5000}

print('Welcome to the Bank')

while True:
    print("What do you like to do?")
    print("  "+"1. View Balance")
    print("  "+"2. View All Bank Info")
    print("  "+"3. Update Balance")
    print("  "+"4. Exit")

    desc = input()
    if desc == '1':
        print("Enter Your name, Please: ")
        k = input()
        if k in bank_users.keys():
            print(k+" Your Bank balance is "+str(bank_users[k]))
        else:
            print("The user can not found. would you like to add the user to the account?")
            desc = input()
            if desc == 'yes':
                k = input('Enter your Name please: ')
                b = input('Enter your Balance please: ')
                bank_users.update({k:b})
            else:
                print("Would you like to exit?")
                desc = input()
                if desc =='yes':
                    break
    elif desc == '2':    
        for k, v in bank_users.items():
            print('Username: '+str(k)+ " bank b=Balance: "+str(v))
    elif desc == '3':
        print('Enter your Name')
        k = input()
        if k in bank_users.keys():
            print("Do you want to add or subtract from your saving?")
            desc = input()
            if desc =='add':
                temp_balance = bank_users[k]
                extra = input("Enter the amount you want to add: ")
                bank_users[k] = temp_balance+ int(extra)
                print('Balance updated. It is: ')
                print(bank_users[k])
            elif desc =='subtract':
                temp_balance = bank_users[k]
                extra = input('Enter the amount you want to subtract: ')
                bank_users[k] = temp_balance-int(extra)
                print('Balance update. It is: ')
                print(bank_users[k])     
        else:
            print("There is no such account in the bank database")  
    elif desc == '4':
        break                                 
