import random

moves = ['Rock', 'Paper', 'Scissors', 'Gun']

x = input('What do you choose? Rock, Paper, or Scissors: ').lower()

r = random.randint(0, len(moves)-2)

a = moves[r].lower()
print('You have chosen to play ' + x)
print('The computer has chosen to play ' + a)

if a == x:
    print('Tie!')

if a == 'rock' and x == 'paper':
    print('You won!')
if x == 'rock' and a == 'paper':
    print('You lost.')
if a == 'rock' and x == 'scissors':
    print('You lost.')
if x == 'rock' and a == 'scissors':
    print('You won!')
if a == 'paper' and x == 'scissors':
    print('You won!')
if x == 'paper' and a == 'scissors':
    print('You lost.')
if x == 'gun':
    print('You have found the secret weapon. Your opponent is amazed to death. YOU WIN!')