def main():
    value = get_user_input()
    answer = validate_input(value)
    print(answer)


def get_user_input():
    return input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()


def validate_input(value):
    return "Yes" if value == "42" or value.lower() == "forty two" or value.lower() == "forty-two" else "No"


if __name__ == "__main__":
    main()
