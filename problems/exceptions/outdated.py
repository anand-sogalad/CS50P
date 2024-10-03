import re


def main():
    date_formatted = False
    while not date_formatted:
        date = get_input("Date: ")
        date = validate_date(date)
        if date:
            date_formatted = True
    print(date)


def get_input(msg: str):
    return input(msg).strip()


def validate_date(date_str: str):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    # Check for MM/DD/YYYY format
    match = re.match(r"^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/(\d{4})$", date_str)
    if match:
        month, day, year = match.groups()
        return f"{year}-{int(month):02d}-{int(day):02d}"

    # Check for Month Day, Year format
    match = re.match(r"^(\w+) (\d{1,2}), (\d{4})$", date_str)
    if match:
        month, day, year = match.groups()
        if month in months:
            month_index = months.index(month) + 1
            return f"{year}-{month_index:02d}-{int(day):02d}"

    return None


if __name__ == "__main__":
    main()
