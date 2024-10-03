def main():
    total = 0
    while True:
        try:
            item = get_input("Item: ")
            price = get_price(item)
            if price:
                total += price
                print(f"Total: {total:.2f}")
        except EOFError:
            break


def get_price(item):
    items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    return items.get(item, None)


def get_input(string):
    return input(string)


if __name__ == "__main__":
    main()
