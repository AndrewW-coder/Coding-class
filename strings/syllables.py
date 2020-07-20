x = input('Insert word here: ')
def syllable(word):
    vowels = 'aeiou'
    syl = 0
    for i in range(0, len(word)-1):
        for j in range(0, len(vowels)-1):
            if word[i] == vowels[j]:
            syl += 1
    if word[int(len(word)-1)] == 'e':
        syl -= 1
    return syl
    print(syl)
syllable(x)


