def main():
    names = get_names()
    for name in sorted(names):
        print(f"Hello, {name}")


def get_names():
    names = list()
    while True:
        try:
            for _ in range(int(input("how many names do you want to store: "))):
                names.append(input("enter name: "))
            return names
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
