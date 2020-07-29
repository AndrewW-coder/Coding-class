x = input('Insert a string here: ')
def dub_word(x):
    l = []
    for i in range(0, len(x)):
        l.append(x[i])
    for s in range(0, len(l)-1):
        if str(l[s]) == str(l[s + 1]):
            f = 'This word has a double letter.'
            break
        else:
            f = 'This word does not have a double letter'    
    return f
    
print(dub_word(x))




