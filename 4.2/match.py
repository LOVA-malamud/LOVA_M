rating: int = int(input('enter your rating num'))
match rating:
    case 5 :
        print('vary good')
    case 4:
        print('very good ')
    case 3:
        print('good')
    case 2:
        print('need improvement')
    case 1:
        print('relly needs imporvement')
    case _:
        print('not in range')