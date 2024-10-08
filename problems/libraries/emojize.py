from emoji import emojize


def main():
    ...
    # get input from user
    user_input = get_input()
    # emojize it
    emojized_input = emojize_input(user_input)
    # print it
    print(emojized_input)


def get_input():
    return input("Input: ")


def emojize_input(input):
    return emojize(input)


if __name__ == "__main__":
    main()
