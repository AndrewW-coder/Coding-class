# x = input('Do you want to (a)convert binary to base 10 or (b)convert base 10 to binary: ').lower()
# if x == 'b':
num = int(input('What number do you want to convert to binary: '))
b = ''
l = []

for j in range(num + 1, 0, -1):
    if 2 ** j <= num:
        m = j
        break
b += str(1)

while m > 0:
    num -= 2 ** m
    m -= 1
    if 2 ** m > num:
        b += str(0)
    else:
        b += str(1)
        num -= 2 ** m
print(b)












    

    
        



