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

symbol1 = 'X'
symbol2 = 'O'
x = input('What symbol do you want to be, X or O? ').upper()

for i in range(0, 10):
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


    if x == 'X':
        x = symbol1
    else:
        x = symbol2

    if x == symbol1:
        if turn % 2 == 1:
            pen = x
        else:
            pen = symbol2

    if x == symbol2:
        if turn % 2 ==1:
            pen = x
        else:
            pen = symbol1

    place = int(input('Insert the number you want to place your token in: '))
    if place == 1:
        board1 = pen
    if place == 2:
        board2 = pen
    if place == 3:
        board3 = pen
    if place == 4:
        board4 = pen
    if place == 5:
        board5 = pen
    if place == 6:
        board6 = pen
    if place == 7:
        board7 = pen
    if place == 8:
        board8 = pen
    if place == 9:
        board9 = pen
    turn += 1
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    c = random.randint(0, len(l)-1)
    if l[c] == 1:
        if board1 == 1:
            board1 = pen
        else:
            l.remove(1)
            c = random.randint(0, len(l)-1)
    if l[c] == 2:
        if board2 == 2:
            board2 = pen
        else:
            l.remove(2)
            c = random.randint(0, len(l)-1)
    if l[c] == 3:
        if board3 == 3:
            board3 = pen
        else:
            l.remove(3)
            c = random.randint(0, len(l)-1)
    if l[c] == 4:
        if board4 == 4:
            board4 = pen
        else:
            l.remove(4)
            c = random.randint(0, len(l)-1)
    if l[c] == 5:
        if board5 == 5:
            board5 = pen
        else:
            l.remove(5)
            c = random.randint(0, len(l)-1)
    if l[c] == 6:
        if board6 == 6:
            board6 = pen
        else:
            l.remove(6)
            c = random.randint(0, len(l)-1)
    if l[c] == 7:
        if board7 == 7:
            board7 = pen
        else:
            l.remove(7)
            c = random.randint(0, len(l)-1)
    if l[c] == 8:
        if board1 == 8:
            board8 = pen
        else:
            l.remove(8)
            c = random.randint(0, len(l)-1)
    if l[c] == 9:
        if board9 == 9:
            board9 = pen
        else:
            l.remove(9)
            c = random.randint(0, len(l)-1)
    turn += 1
    
    
    

