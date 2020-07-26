x = input('Do you want to (a)convert binary to base 10 or (b)convert base 10 to binary: ').lower()
if x == 'b':
    num = int(input('What number do you want to convert to binary: '))
    b = ''
    while num > 0:
        b = str(num % 2) + b
        
    print(b)
    

    
        



