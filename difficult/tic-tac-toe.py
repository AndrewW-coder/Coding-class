import random

board1 = '1'
board2 = '2'
board3 = '3'
board4 = '4'
board5 = '5'
board6 = '6'
board7 = '7'
board8 = '8'
board9 = '9'
turn = 1
pen = 0

print('Welcome to tic-tac-toe!')
print('   |   |')
print(' ' + board7 + ' | ' + board8 + ' | ' + board9)
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board4 + ' | ' + board5 + ' | ' + board6)
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board1 + ' | ' + board2 + ' | ' + board3)
print('   |   |')


symbol1 = 'X'
symbol2 = 'O'
x = input('What symbol do you want to be, X or O? ').upper()
if x == 'X':
    x = symbol1
else:
    x = symbol2

if x == symbol1:
    if turn % 2 == 1:
        pen = x
if x == symbol2:
    if turn % 2 ==1:
        pen = x
place = int(input('Insert the number you want to place your token in: '))
if place == 1:
    place = board1
if place == 2:
    place = board2
if place == 3:
    place = board3
if place == 4:
    place = board4
if place == 5:
    place = board5
if place == 6:
    place = board6
if place == 7:
    place = board7
if place == 8:
    pen = board8
if place == 9:
    board9 = pen
print(pen)

print('   |   |')
print(' ' + board7 + ' | ' + board8 + ' | ' + board9)
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board4 + ' | ' + board5 + ' | ' + board6)
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board1 + ' | ' + board2 + ' | ' + board3)
print('   |   |')




