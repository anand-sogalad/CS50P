import time


def main():
    name = input("Enter your first name: ")
    st = time.perf_counter()
    your_last_name(name)
    et = time.perf_counter()
    print(et - st)

    st = time.perf_counter()
    your_last_name_if(name)
    et = time.perf_counter()
    print(et - st)


def your_last_name(name):
    match name:
        case "Harry" | "Ron" | "Hermione":
            print("Your last name is Gryffindor")
        case "Draco":
            print("Your last name is Slytherin")
        case _:
            print("Your last name is unknown")


def your_last_name_if(name):
    if name in ("Harry", "Ron", "Hermione"):
        print("Your last name is Gryffindor")
    elif name == "Draco":
        print("Your last name is Slytherin")
    else:
        print("Your last name is unknown")


if __name__ == "__main__":
    main()
