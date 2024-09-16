def meow_while(count):
    i = 0
    while i < count:
        print("meow")
        i += 1


def meow_for(count):
    for _ in range(count):
        print("meow")


def main():
    number = get_input()
    meow_while(number)
    meow_for(number)


def get_input():
    while True:
        try:
            n = int(input("How many times should I say meow? "))
            if n > 0:
                return n
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a number.")
            # continue


if __name__ == '__main__':
    main()
