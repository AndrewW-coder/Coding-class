import time

t = 10

print('T - 10')
while t >= 0:
    time.sleep(1)
    t -= 1
    print(t)
    if t == 0:
        print('BLAST OFF!!')

