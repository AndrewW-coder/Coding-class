import random

l = [1, 2, 3, 4, 5, 6]
for i in range(0,2):
    r = random.randint(0, len(l)-1)
    
    print(' __')
    print('|' + str(l[r]) + ' |')
    print(' ```')