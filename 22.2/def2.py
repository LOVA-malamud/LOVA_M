grade_input = int(input('grade'))

def get_grade_value(grade: int) -> str:
    """
    :param grade: grade between 1-100
    :return: description based on the grade
    """
    if 0 <= grade <= 40:
        return "fail"
    elif 40 < grade <= 60:
        return "need improvement"
    elif 60 < grade <= 80:
        return "not bad"
    elif 80 < grade <= 100:
        return "very good!"
    else:
        return "invalid grade"
print(get_grade_value(grade_input))