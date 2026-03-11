import random
dict_numbers = {}
random_number = random.randint(1, 100)
dict_numbers[random_number] = 'Bingo!'
for i in range(1, random_number):
    dict_numbers[i] = 'to low'
for i in range(random_number + 1, 101):
    dict_numbers[i] = 'to high'
print(dict_numbers)
while True:
    guess = int(input('guess number?'))
    print(dict_numbers[guess])
    if dict_numbers[guess] == 'Bingo!':
        break