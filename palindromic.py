f= open('NUMBER','w+')
f.write('123321')
f.close()

f = open('NUMBER','r+')
myList = list(f.read())
f.close()

is_palindromic = True

for i in range(int(len(myList)/2)):
    if myList[i] != myList[len(myList)-i-1]:
        is_palindromic = False

if is_palindromic:
    f = open('NUMBER','a')
    f.write('Yes')
    f.close()
else:
    f = open('NUMBER','w')
    for i in range(len(myList)):
        f.write('0')            
      
