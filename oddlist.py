def print_odd(mylist):
    new_list = []
    k = 0
    for i in range(len(mylist)):
        if mylist[i] % 2 != 0:
            new_list.append(mylist[i])

            k+=1
    return new_list
result = print_odd([1,2,3,4,5,6,7,8,9,10])

print(result)