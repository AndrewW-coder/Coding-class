import time
import random

seconds = time.time()


type_sentences = [
    ['Today I went outside and played with my dog']
    ]
r = random.randint(0, len(type_sentences)-1)
t = 3
for i in range(0, 3):
    print(t)
    time.sleep(1)
    t -= 1
    if t == 0:
        print('GO')
print(type_sentences[r])

your_sentence = input('Type the sentence above: ')
t = 0
#
#
#Spppeeeeeeeeeeddddddddd
#
#
l = []
l2 = []
for i in range(0, len(type_sentences[r])):
    l.append(type_sentences[i])
for i in range(0, len(your_sentence)):
    l2.append(your_sentence[i])
a = 0
if len(type_sentences) > len(your_sentence):
    t = len(type_sentences)
else:
    t = len(your_sentence)

