import random


def flip(coin):
    return random.choice(coin)


def choice(a, b):
    return random.randint(a, b)


def shuffle(arr):
    random.shuffle(arr)


def main():
    coin = ["Heads", "Tails"]
    print(flip(coin))

    print(choice(1, 10))

    arr = [1, 2, 3, 4, 5]
    shuffle(arr)
    print(arr)


if __name__ == "__main__":
    main()
