import random
num = random.randint(1, 100)
x = int(input("I have chosen a number form 1 to 100. Guess: "))
for i in range(15):
    
    if x > num:
        print('My number is smaller.')
        x = int(input('Guess again: '))
    elif x < num:
        print('My number is bigger.')
        x = int(input('Guess again: '))
    else:
        print('That is my number! Congratulations!')
        break