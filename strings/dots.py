def add_dots(word):
    l = []
    for i in range(0, len(word)):
        l.append(word[i])
    for i in range(1, len(l) * 2 - 1, 2):
        l.insert(i, '.')
    s = ''.join(l)
    return s
#print(add_dots('hello'))

def remove_dots(string):
    l = []
    for i in range(0, len(string)):
        l.append(string[i])
    num = l.count('.')
    for i in range(0, num):
        l.remove('.')
    s = ''.join(l)
    return s
print(remove_dots('h.e.l.l.o'))

remove_dots(add_dots('test'))



