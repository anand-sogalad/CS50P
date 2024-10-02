def main():
    snake_case(get_input())


def get_input():
    return input("camelCase: ").strip()


def snake_case(s):
    for letter in s:
        if letter.isupper():
            s = s.replace(letter, "_" + letter.lower())
    print(f"snake_case: {s}")


if __name__ == "__main__":
    main()
