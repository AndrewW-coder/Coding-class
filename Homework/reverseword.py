def reverse_word(s):
    l = s.split()
    for i in range(len(l) - 1, -1, -1):
        l.append(l[i])
    for i in range(0, int(len(l)/2)):
        l.remove(l[i])
    return l

print(reverse_word('hi i like pie'))

        



