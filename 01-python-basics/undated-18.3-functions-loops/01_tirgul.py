def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

num = (input("Enter a number: "))

print(num[::-1])
print(max(num))
print(num.count("5"))
print(min(num))
print(num.count(max(num)))
print(min(num))
print(sum(int(digit) for digit in num))
print(sum(int(digit) for digit in num) / len(num))

