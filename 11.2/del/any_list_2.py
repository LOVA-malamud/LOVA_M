sleeping = [True, True, False, False, True,]
print(any(sleep == True for sleep in sleeping))
print(any(sleep for sleep in sleeping))
numbers = [ 2, 4, 8, 10, 200]
print(any(numbes))
numbers = [ 1, 3, 5, 7, 9, 10]
print(all(number % 2 == 1 for number in numbers))
numbers = [ 1, 3, 5, 7, 9,]
print(all(number % 2 == 1 for number in numbers))
print(all(number % 2 != 0 for number in numbers))
