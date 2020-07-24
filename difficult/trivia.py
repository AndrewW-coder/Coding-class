import time

print('This is Triviaaaaa!')
time.sleep(2)
print('Time for your questions!')
time.sleep(2)
t = 3
score = 0
for i in range(0, 3):
    print(t)
    time.sleep(1)
    t -= 1
    if t == 0:
        print('GO!')
print('What is the fear of being tickled by feathers?')
print("(a)Astraphobia, (b)Cynophobia, (c)Pteronophobia, (d)Trypanophobia")
answer = input().lower()
if answer == 'c':
    score += 1

print('What is a flock of crows known as?')
print("(a)Cyclone, (b)Murder, (c)Pack, (d)Flock")
answer = input().lower()
if answer == 'b':
    score += 1

print('What day is May 29th?')
print("(a)Put your pillow on your fridge day, (b)Eat breakfast for all meals day, (c)Give someone a hug day")
answer = input().lower()
if answer == 'a':
    score += 1
