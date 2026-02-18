polidrom = [1, 2, 3, 4, 3, 2, 1]
for i in range(len(polidrom)//2):
    if polidrom[i] != polidrom[-i-1]:
        print('not polidrom')
        break
else:
    print('polidrom')