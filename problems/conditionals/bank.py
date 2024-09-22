def main():
    val = get_user_input()
    new_val = validate_greeting(val)
    print(new_val)


def get_user_input():
    return input("Greeting: ").strip().lower()


def validate_greeting(val: str):
    if val.startswith("hello"):
        return "$0"
    elif val.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
