def mid(word):
    l = []
    for i in range(0, len(word)):
        l.append(word[i])
    if len(word) % 2 == 0:
        mid_letter = ''
    else:
        x = int((len(word) - 1)/2)
        mid_letter = word[x]
    return mid_letter
print(mid('chicken'))



