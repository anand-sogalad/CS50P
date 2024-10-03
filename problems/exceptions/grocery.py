def main():
    grocery_items = []
    while True:
        try:
            grocery_items.append(get_input())
        except EOFError:
            for i, j in enumerate(sorted(list(set(grocery_items)))):
                print(i + 1, j)
            break


def get_input():
    return input().strip().upper()


if __name__ == "__main__":
    main()
