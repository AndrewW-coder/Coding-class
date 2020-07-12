x = int(input('Insert number here: '))
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(j, '*', i, '=', i * j, end = '     ') 
    print('\n', end = '')
       
