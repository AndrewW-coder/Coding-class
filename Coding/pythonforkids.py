import random
num = random.randint(1,100)
while True:
    i = int(input('Enter a number here: '))
    if i == num:
        print('You guessed right!')
        break
    elif i < num:
        print('Try higher')
    elif i > num:
        print('Try lower')

