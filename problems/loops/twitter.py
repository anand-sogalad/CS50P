def main():
    string = input("Input: ").strip()
    print(f"Output: {remove_owels(string)}")


def remove_owels(s):
    return "".join(c for c in s if c not in "aeiou")


if __name__ == "__main__":
    main()
