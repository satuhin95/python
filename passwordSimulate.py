password_bank ={'Sam':123,'Mamun':456123,'Roni':123456}

matched = False
x = 0
print("Enter your name ")

while x < 5:
    name = input()
    if name in password_bank:
        for i in range(0,3):
            print("Enter Your Password ")
            password = input()
            if int(password) in password_bank.values():
                matched = True
                print('Access Grantd')
                break
            else:
                print('Wrong Password. Enter again ' + ' You have '+str(2-i)+' tries left' )
    else:
        print('There is no such name') 
    x = x + 1

    if matched:
        break               
             