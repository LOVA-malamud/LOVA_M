# 1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2 ,5]
for _ in list1:
    if _ in list2:
        list1.remove(_)
print(list1)

# 2
list1 = [1, 2, 9, 88, 0]
list2 = [3, 4, -3]
list3 = [5, 6, 55]
list4 = []
for _ in list1:
    list4.append(_)
for _ in list2:
    list4.append(_)
for _ in list3:
    list4.append(_)
print(list4)
# 3
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2 ,5]
for _ in list1:
    if not _ in list2:
        print(_)