def main():
    try:
        number = int(input("Enter a number: "))
        print(square(number))
    except ValueError:
        print("Invalid input")


def square(number):
    return number * number


if __name__ == "__main__":
    main()
