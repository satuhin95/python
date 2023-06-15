def centered_avg(mylist):
    sum = 0
    count =0

    for i in range(1,len(mylist)-1):
        sum+=mylist[i]
        count+=1

    return sum/count

result = int(centered_avg([1,2,3,4,5]))

print(result)