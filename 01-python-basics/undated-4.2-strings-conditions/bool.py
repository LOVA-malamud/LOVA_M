rating: int = int(input('enter your rating'))
is_valid: bool = 1 <= rating <= 5
if is_valid:
    print('in range')
    is_best: bool = rating == 5
    if is_best:
        print('highest score')
    else:
        print('not highest score ')
        is_medium: bool = 4 >= rating >= 2
        if not is_medium:
            print('score low ')
        else :
            print('score medium')
else:
    print('not in range')
num: int = int(input('enter your num '))
is_positive: bool = num > 0
print(is_positive)
is_even: bool = num % 2 == 0
if is_even:
    print('even')
else:
    print('not even')
prime_num: int = int(input('enter your prime'))


