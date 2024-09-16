def main():
    names = get_names()
    write_to_file("students.csv", names)
    read_from_file("students.csv")


def get_names():
    names = []
    while True:
        try:
            for _ in range(int(input("How many name do you need? "))):
                names.append(input("Enter your full name (comma seperated) "))
            return names
        except ValueError:
            print("Invalid Input")


def write_to_file(file_path, list_content):
    with open(file_path, "w") as file:
        for content in list_content:
            file.write(content + "\n")


def read_from_file(file_path):
    with open(file_path, "r") as file:
        for content in file:
            print(content.rstrip())


if __name__ == '__main__':
    main()
