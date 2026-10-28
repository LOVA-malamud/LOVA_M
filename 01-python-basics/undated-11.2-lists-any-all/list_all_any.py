import random
grades = []
for i in range(10):
    new_number = random.randint(0,100)
    grades.append(new_number)
print(grades)
any_above_90 = False
for grade in grades:
    if grade > 90:
        any_above_90 = True
        break
print(f'is there any garde above 90?', any_above_90)
print(any(grade > 90 for grade in grades))

all_below_equl_90 = True
for garde in grades:
    if garde > 90:
        all_below_equl_90 = False
        break
print('all garde are 90 or below?',all_below_equl_90)
print(any(grade >= 90 for grade in grades))