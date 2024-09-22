def main():
    value = get_user_input()
    new_value = replace_space(value)
    print(new_value)


def get_user_input():
    return input().strip()


def replace_space(val):
    return val.replace(" ", "...")


if __name__ == "__main__":
    main()
