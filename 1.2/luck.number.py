attempts: int = 0
import random
lucky_num: int = random.randint(1,100)
num: int = int(input('enter your number'))
if num == lucky_num:
    print('bingo')
else:
    print('worng number')
    attempts += 1
    while attempts <= 7:
        num: int =  int(input('enter your num again'))
        if num < lucky_num:
            print('guess higher')
            attempts += 1
        elif num > lucky_num:
            print('guess lower')
            attempts += 1
        else:
            print('bingo')