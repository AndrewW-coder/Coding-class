def reverse_word(s):
    l = s.split()
    
    for i in range(len(l) - 1, -1, -1):
        l.append(l[i])
    
    for i in range(0, int(len(l)/2)):
        l.remove(l[i])
    s = ' '.join(l)
    return s

x = input('Insert a string: ')
print(reverse_word(x))

        



