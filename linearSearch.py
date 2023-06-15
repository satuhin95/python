mylist = [10,5,2,15,55,23];

n = int(input("Enter a Number "))

def linear_search(mylist, value):
    for i in range(len(mylist)):
        if mylist[i] == value:
            return "Found"

    if i == len(mylist)-1:
        return "Not Found"    
    
result = linear_search(mylist,n)

print(result)