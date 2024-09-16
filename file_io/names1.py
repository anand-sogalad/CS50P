def main():
    # get names
    names = get_names()

    # write names to file
    with open("names.txt", "w") as f:
        for name in names:
            f.write(name + "\n")

    # read names from file
    with open("names.txt", "r") as f:
        for name in f:
            print(name.rstrip())


def get_names():
    names = list()
    while True:
        try:
            for _ in range(int(input("How many name do you want to enter? "))):
                names.append(input("Enter name "))
            return names
        except ValueError:
            print("Invalid Input")


if __name__ == "__main__":
    main()
