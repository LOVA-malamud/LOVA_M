import random
grades = []
for i in range(50):
    new_numbers = random.randint(0,100)
    grades.append(new_numbers)
print(grades)
count_high_grades = 0
for gardes in grades:
    count_high_grades += (gardes >= 90)

print(f' 90 count {count_high_grades} time')

