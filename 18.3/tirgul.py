def tirgul(input):
    for i in range(1, input + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(input - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    return input
user_input = int(input("Enter your number:"))
tirgul(user_input)