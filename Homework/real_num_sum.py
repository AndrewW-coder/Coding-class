l = [1, 2, 3, 4, 5]
def num_sum(li, target):
    lis = []
    for i in range(0, len(l)):
        if l[i] + l[i] == target:
            lis.append(i)
    return lis
print(num_sum(l, 9))

            