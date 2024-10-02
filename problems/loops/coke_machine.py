def main():
    coke_price = 50
    recieved_money = 0
    while recieved_money <= coke_price:
        check_due(coke_price, recieved_money)
        recieved_money += get_coin()
    get_change(coke_price, recieved_money)


def check_due(price, amount):
    due = price - amount
    due = due if due > 0 else 0
    print(f"Amout Due: {due}")


def get_coin():
    coin = int(input("Insert Coin: ").strip())
    match coin:
        case 5 | 10 | 25:
            return coin
        case _:
            return 0


def get_change(price, amount):
    change = amount - price
    print(f"Change Owed: {change}")


if __name__ == "__main__":
    main()
