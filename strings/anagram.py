def is_anagram(str1, str2):
    r = 0
    for i in range(0, len(str1) - 1):
        if ''.join(sorted(str1))[i] == ''.join(sorted(str2))[i]:
            r = True
        else:
            r = False
    return r
    
print(is_anagram('hi', 'hi'))



