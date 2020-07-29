import random
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
s = ['♠️', '♥️', '♣️', '♦️']
for i in range(0, 4):
    suit = random.randint(0, len(s)-1)
    n = random.randint(0, len(l)-1)
    print(' ____')
    if l[n] < 10:
        print('|' + str(l[n]) + s[suit] + '  |')
    else:
        print('|' + str(l[n]) + s[suit] + ' |')
    print('|' + '    |')
    print(' `````') 
    
    