import random

random_nums = []
for i in range(30):
    num = random.randint(1, 10)
    random_nums.append(num)

print(random_nums)

unique_nums = sorted(set(random_nums))

for num in unique_nums:
    count = random_nums.count(num)
    print(f"# {num}: {count}-times")
