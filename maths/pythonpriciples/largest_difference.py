def largest_difference(l):
    l.sort()
    d = l[-1] - l[0]
    return d
l = [1, 3, 2, 4, 5]
print(largest_difference(l))