# l = [1]
# print(l)
# for x in range(1, 10):
#     l = [1, 1]
    
#     print(l) 
def pascal():
    row = [1]
    while True:
        yield row
        row = [i + j for i, j in zip(row + [0], [0] + row)]
pascal()
