def main():
    number = int(input("Enter a number: "))
    if is_even(number):
        print("Number is even")
    else:
        print("Number is odd")


def is_even(number):
    return number % 2 == 0


if __name__ == "__main__":
    main()
