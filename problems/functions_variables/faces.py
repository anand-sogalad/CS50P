def main():
    value = take_user_input()
    new_val = convert(value)
    print(new_val)


def take_user_input():
    return input()


def convert(val):
    emoji = {
        ":)": "😊",
        ":(": "😢",
        ":D": "😄",
        ";)": "😉",
        ":'(": "😭",
        ":P": "😜"
    }
    return val.replace(":)", emoji.get(":)")).replace(":(", emoji.get(":("))


if __name__ == "__main__":
    main()
