x = input('Insert a string here and I shall remove ALL the spaces: ')
def remove_space(word):
    l = []
    for i in range(0, len(word)):
        l.append(word[i])
        if word[i] == ' ':
            l.remove(word[i])
    s = ''
    for i in range(0, len(l)):
        s = s + l[i]
    return s
print(remove_space(x))
        
