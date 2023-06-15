contact_no = {'saif':123456,'Mamun':12354,'Hasan':456123}
x =0

while x <  5:
    print('Enter Your Name(press ENTER to exit): ')
    name = input()

    if name == '':
        break

    if name in contact_no:
        print("The Contact number of "+name+' is '+ str(contact_no[name]))
    else:
        print('There is no such name in the phone book. Do you want to add it?')
        desc = input()

        if desc == 'yes':
            print('Enter the number')
            num = input()
            contact_no[name] = num
            print("Dictonary Updated")
        elif desc == 'no':
            print('Do you want to quit?')
            desc = input()
            if desc == 'yes':
                break  
            else:
                print('Keep searching')

    x+=1                  