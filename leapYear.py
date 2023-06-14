year = int(input('Enter the year  '))

if year % 400 == 0:
    print(year," is a leap Year")
elif year % 100 == 0:   
    print(year," is a leap Year")
elif year % 4 == 0:
    print(year," is a leap Year")
else:
    print(year," is not a leap Year")         