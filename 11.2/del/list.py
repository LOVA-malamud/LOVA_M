list1 = [90, 80, 100, 55, 90, 100, 90]
indices_of_90 = []
for i in range (len(list1)):
    if list1[i] == 90:
        indices_of_90.append(i)

print(len(indices_of_90))
print(indices_of_90)


list1 = [90, 80, 100, 55, 90, 100, 90]
indices_of_90 = []
for i, numbers in enumerate (list1):
    if numbers == 90:
        indices_of_90.append(i)

print(len(indices_of_90))
print(indices_of_90)

list1[4, 4, 4, 4, -9, 12, 4]
print(f'appears {list1.count(4)} times.' )