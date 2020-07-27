import random

J = 11
Q = 12
K = 13
A = 14
bigJoker = 100
smallJoker = 99

cards = [3,3,3,3,4,4,4,4,5,5,5,5,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,J,J,J,J,Q,Q,Q,Q,K,K,K,K,A,A,A,A,2,2,2,2,bigJoker,smallJoker]
player1 = []
player2 = []
player3 = []
for i in range(0, 17):
    n = random.randint(0, len(cards) - 1)
    player1.append(cards[n])
    cards.remove(cards[n])
    n = random.randint(0, len(cards) - 1)
    player2.append(cards[n])
    cards.remove(cards[n])
    n = random.randint(0, len(cards) - 1)
    player3.append(cards[n])
    cards.remove(cards[n])
player1.sort()
player2.sort()
player3.sort()
print(player1)
print(player2)


