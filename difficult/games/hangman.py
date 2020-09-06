import time
from time import sleep


letters = []
print('This is Hangman!')
sleep(1)
print('(a 2 player game)')
sleep(1)
word = input('What word do you want the opponent to guess?: ')
l = []
for i in range(0, len(word)):
    l += '_'
guess = 6
print('You have ' + str(guess) + ' guesses left.')
    
for j in range(0, 26):
    letter = input("What letter do you guess: ")
    if letter in word:
        for i in range(0, len(word)):
            if word[i] == letter:
                l[i] = letter
                guess = guess
    elif letter not in word:
        print('That letter is not in the word.')
        sleep(0.5)
        guess -= 1
        print('You have %s guesses left.' %guess)
        letters.append(letter)
    s = ''.join(l)
    if s.count('_') == 0:
        print(l)
        print('Congratualations, you have guessed the word!')
        break
    print(l)
    print('The letters you cannot guess are:')
    print(letters)