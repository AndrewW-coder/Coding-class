def romanToInt(s):
    sum = 0
    for i in range(0, len(s)-1):
        if s[i] == 'I':
            sum += 1
            i += 1
        if s[i] == 'V':
            sum += 5
            i += 1
        if s[i] == 'X':
            sum += 10
            i += 1
        if s[i] == 'L':
            sum += 50
            i += 1
        if s[i] == 'C':
            sum += 100
            i += 1
        if s[i] == 'D':
            sum += 500
            i += 1
        if s[i] == 'M':
            sum += 1000
            i += 1
    for i in range(0, len(s) - 2):
        if s[i] == 'I' and s[i + 1] == "V" or s[i + 1] == 'X':
            sum-= 1
        if s[i] == 'X' and s[i + 1] == "L" or s[i + 1] == 'C':
            sum-= 10
        if s[i] == 'C' and s[i + 1] == "D" or s[i + 1] == 'M':
            sum-= 100           
    return sum
print(romanToInt('IV'))