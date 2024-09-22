def main():
    value = get_input_from_user()
    lower_case = convert_to_lower(value)
    print(lower_case)


def get_input_from_user():
    return input().strip()


def convert_to_lower(val):
    return val.lower()


if __name__ == "__main__":
    main()
