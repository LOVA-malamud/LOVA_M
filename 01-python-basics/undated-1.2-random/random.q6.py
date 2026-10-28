import random

num_one: int = int(input('Enter a number: '))
num_two: int = int(input('Enter another number: '))
num_three : int = int(input('enter you three number'))
random_num: int = random.choice([num_two, num_three,  num_one])
print(random_num)