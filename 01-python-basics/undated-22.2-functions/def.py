def biggest(a: int, b: int, c: int) -> int:
    """
    function biggest returns the biggest of 3 numbers
    :param a: number 1
    :param b: number 2
    :param c: number 3
    :return: the biggest number of a, b, c
    """
    return max(a, b, c)  # הפונקציה מחזירה את הערך המקסימלי

def smallest(a: int, b: int, c: int) -> int:
    """
    function smallest returns the smallest of 3 numbers
    :param a: number 1
    :param b: number 2
    :param c: number 3
    :return: the smallest number of a, b, c
    """
    return min(a, b, c)  # הפונקציה מחזירה את הערך המינימלי

# בדיקה
print(biggest(5, -2, 30))   # אמור להדפיס 30
print(smallest(5, -2, 30))  # אמור להדפיס -2
