# print hello world
def hello_world():
    print("Hello, world!")


# say hello to user
def hello(user):
    print(f"Hello, {user}")


def string_methods(string):
    # remove whitespace from string
    # string = input("Enter a string: ")
    print(f"sttring after removing leading and trailing white spaces: {string.strip()}")

    # capitalize the fitst letter of a string
    # string = input("Enter a string: ")
    print(f"string after capitalizing first letter of a string: {string.capitalize()}")

    # captitalize first letter of every word in a string
    # string = input("Enter a string: ")
    print(f"string after capitalizing first letter of every word: {string.title()}")

    # split a string into a list
    # string = input("Enter a string: ")
    print(f"string after splitting into a list: {string.split()}")


def main():
    # print hello world
    hello_world()

    # take input from user & print hello to user
    name = input("What is your name? ")
    hello(name)

    # string methods
    string = input("Enter a string: ")
    string_methods(string)


if __name__ == "__main__":
    main()
