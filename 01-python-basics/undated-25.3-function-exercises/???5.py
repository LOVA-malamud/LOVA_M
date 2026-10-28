def camel_to_snake(name: str) -> str:
    snake_name = ""
    for i in name:
        if i.isupper():
            snake_name += '_' + i.lower()
        else:
            snake_name += i.lower()
    return snake_name
print(camel_to_snake("lovaMalamudKingOfTheWorld"))