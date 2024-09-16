def compare(number):
    if number >= 90:
        print("A")
    elif number >= 80:
        print("B")
    elif number >= 70:
        print("C")
    else:
        print("F")


def main():
    score = int(input("Enter score: "))
    compare(score)


if __name__ == "__main__":
    main()
