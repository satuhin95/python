import random as r

secret_age =r.randint(1,10)
flag = False

def game(guessed_age,secret):
    if guessed_age < secret:
        return 'Too Low'
    elif guessed_age > secret:
        return 'Too High'
    else:
        return 'CORRECT!'

for i in range(1,6):
    print('Take a guess. You have '+ str(6-i)+ ' guesses left')
    gess = input()
    if game(int(gess),secret_age) == 'CORRECT!':
        print('You won the game!')
        flag = True
        break   
if not flag:
    print("You lost the game")    