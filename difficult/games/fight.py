import random
import time
from time import sleep

player1hp = 100
player2hp = 100

print('Welcome to player 1v1!')
sleep(0.5)
print('In this game you can either defend, attack, or shield.')
sleep(0.5)
print('If you attack, it will do 0 - 25 damage.')
sleep(0.5)
print('If you defend, it will have a 75% probablity of reducing your opponents next attack.')
sleep(0.5)
print('''If you shield, it will give a 10% probability of making you invincible.''')
sleep(1)
moves = 1

if moves % 2 == 1:

    move = input('What do you choose to do: ').lower()
    if move == 'defend': 
        print('You have chosen to defend.')
        n = random.randint(0, 3)
        if n != 0:
            print('You have successfully sheilded! If your opponent shoots you the next turn.')
            sleep(0.5)
            n = random.randint(0, 75)
        else:
            print('Sorry, looks like your shield failed.')
            

    elif move == 'attack':
        print('You have chosen to attack!')
        n = random.randint(0, 25)
        player2hp -= n 
        print('You have done %s damage and now his health is at %s' %(n, player2hp))

    
