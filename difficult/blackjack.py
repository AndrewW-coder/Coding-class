import random


your_decision = 0
###########################################
Ace = 1
King = 10
Queen = 10
Jack = 10
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]

card1 = random.randint(1, 10)
card2 = random.randint(1, 10)
card3 = random.randint(1, 10)
card4 = random.randint(1, 10)


your_value = card1 + card3
dealer_value = card2 + card4

print('You got 2 cards and your value is currently ' + str(your_value))
print('The dealer got 2 cards and one of them was a ' + str(card2))



for i in range(0, 5):
    your_decision = input('Do you wish to hit or stand? ').lower()
    if your_decision == 'hit':
        n = random.randint(0, len(l)-1)
        your_value += l[n]
        while dealer_value <= 15:
            d = random.randint(0, len(l)-1)
            dealer_value += l[d]
    
    
        print('The card you have recieved is ' + str(l[n]))
        print('This now brings you up to a total of ' + str(your_value))
    else:
        while dealer_value <= 15:
            d = random.randint(0, len(l)-1)
            dealer_value += l[d]
        your_value = your_value
        print('Your final total is ' + str(your_value))
        print('The dealers value is ' + str(dealer_value))
        if your_value > dealer_value:
            print('Congratulations! You beat the dealer! Thanks for playing!')
            break
        elif your_value < dealer_value:
            print('Sorry, looks like the dealer beat you. Try again next time!')
            break
        else:
            print('Looks like you have a draw! How suprising!')
            break
    if your_value > 21 and dealer_value <= 21:
        print('The dealer had ' + str(dealer_value))
        print("Sorry, looks like you busted and the dealer didn't. You lost. Try again next time!")
        break
    elif your_value <= 21 and dealer_value > 21:
        print('The dealer has ' + str(dealer_value))
        print("The dealer busted! You win!")
        break
    elif your_value > 21 and dealer_value > 21:
        print('Looks like you both busted. RIP!')
        break
    if your_value > 21 and dealer_value <= 21:
        print('The dealers total is ' + str(dealer_value))
        print("Sorry, looks like you busted and the dealer didn't. You lost. Try again next time!")
        break
    elif your_value <= 21 and dealer_value > 21:
        print('The dealers total is ' + str(dealer_value))
        print("The dealer busted! You win!")
        break
    elif your_value > 21 and dealer_value > 21:
        print('The dealers total is ' + str(dealer_value))
        print('Looks like you both busted. RIP!')
        break