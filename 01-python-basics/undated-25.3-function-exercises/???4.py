def fuel_status() -> str:
    while True:
        user_input = input("Fraction: ")
        try:
            x_str, y_str = user_input.split("/")
            x = int(x_str)
            y = int(y_str)

            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            percentage = round((x / y) * 100)

            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"

        except (ValueError, ZeroDivisionError):
            pass


print(fuel_status())
