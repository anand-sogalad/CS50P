def main():
    while True:
        try:
            x, y = get_input("Fraction: ")
            fuel_level = get_fuel_level(x, y)
            print(
                f"{int(fuel_level)}%"
                if fuel_level != "E" and fuel_level != "F"
                else fuel_level
            )
            break
        except (ValueError, ZeroDivisionError):
            continue


def get_fuel_level(x, y):
    if x > y:
        raise ValueError()

    percentage = (x / y) * 100

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return percentage


def get_input(string):
    return tuple(map(int, input(string).strip().split("/")))


if __name__ == "__main__":
    main()
