def calc_statistics(grades: list,oper: str) -> int:
    '''
    get a list and operation, returns the operation result
    :param grades: list of grades
    :param oper: 'max' or 'min' or len or 'avg'
    :return: the result of the operation on the list
    '''
    if oper == 'maximum':
        return max(grades)
    elif oper == 'minimum':
        return min(grades)
    elif oper == 'length':
        return len(grades)
    elif oper == 'average':
        return sum(grades) / len(grades)
    elif oper == 'sum':
        return sum(grades)
    else:
        return 'invalid operation'
print(calc_statistics([40, 50, 60], 'maximum'))
print(calc_statistics([40, 50, 60], 'minimum'))
print(calc_statistics([40, 50, 60], 'length'))
print(calc_statistics([40, 50, 60], 'sum'))
print(calc_statistics([40, 50, 60], 'average'))
