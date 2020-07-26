def mysplit(str1, sym):
    l = []
    t = 0  
    l1 = []  
    str1list = []
    # for i in range(len(str1)):
    #     str1list.append(str1[i])
    for i in range(0, str1.count(sym) + 1):
        while str1[t] != sym:
            l1.append(str1[t])
            t = t + 1
        l.append(l1)
        # if str1[t] == sym and str1[t + 1] == ' ':
        #     t = t + 2
        # elif str1[t] == sym and str1[t] != ' ':
        #     t = t + 1


            

    return l
    
    
print(mysplit('hello, i, am cool', ','))

            