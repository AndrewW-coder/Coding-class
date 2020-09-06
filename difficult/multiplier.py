import random
import time
from time import sleep


#Gets all the multipliers
num_multipliers = int(input('How many multipliers do you want: '))
multipliers = []
for i in range(0, num_multipliers):
    n = random.randint(0, 9)
    multipliers.append(n)
#count score
c = 0
while True:
    #Gets the random numbers
    code = []
    for i in range(0, len(multipliers)):
        n = random.randint(-5, 9)
        code.append(n)

    #Tells them what the code is
    print('The code is currently:')
    sleep(0.5)
    print(code)
    sleep(0.5)

    #Get their guesses
    guess = input('What are your guesses for the multipliers(please use commas): ')
    guesses = guess.split(',')

    #calculate the sum and target
    player_sum = 0
    for i in range(0, len(guesses)):
        player_sum += int(guesses[i]) * code[i]

    target_sum = 0
    for i in range(0, len(multipliers)):
        target_sum += int(multipliers[i]) * code[i]

    #tell Them 
    print('Your total was: ' + str(player_sum))
    sleep(0.5)
    print('The target was: ' + str(target_sum))
    #consequences and check range
    if target_sum in range(player_sum-3, player_sum+4):
        c += 1
    else:
        c = 0
        #checks if bigger or smaller
        if target_sum > player_sum:
            print('Your sum is to small.')
        else:
            print('Your sum is too big.')
    sleep(1)
    #Tells you how many you have in a row
    print('You currently have ' + str(c) + ' in a row')
    #YOU WIN
    if c == 3:
        print('Congratulations, you won!')
        sleep(0.5)
        print('Your guess was: ')
        sleep(0.5)
        print(guesses)
        sleep(0.5)
        print('The actual multipliers was: ')
        sleep(0.5)
        print(multipliers)
        break
