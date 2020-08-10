def pascal(numRows):
    result = []
    if numRows == 0:
        return 0
    r = 2
    pascal = [1]
    result.append(pascal)
    
    while r <= numRows:
        pascal_old = pascal
        pascal = [1]
        for i in range(0, r - 2):
            pascal.append(pascal_old[i] + pascal_old[i+1])
        pascal.append(1)
        result.append(pascal)
        r +=1
    return result
print(pascal(5))