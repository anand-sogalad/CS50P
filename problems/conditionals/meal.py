# breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
def main():
    time = get_input()
    meal_time(time)


def get_input():
    return input("What time is it? ").strip()


def meal_time(time):
    h, m = time.split(":")
    if (int(h) == 7 and 0 <= int(m) <= 59) or (int(h) == 8 and 0 == int(m)):
        print("breakfast time")
    elif (int(h) == 12 and 0 <= int(m) <= 59) or (int(h) == 13 and 0 == int(m)):
        print("lunch time")
    elif (int(h) == 18 and 0 <= int(m) <= 59) or (int(h) == 19 and 0 == int(m)):
        print("dinner time")


if __name__ == "__main__":
    main()
