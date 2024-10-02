def main():
    plate = input("Plate: ")
    if check_vanity_plate(plate):
        print("Valid")
    else:
        print("Invalid")


def check_vanity_plate(plate):
    # incase only 2 chars present in the string
    if len(plate) == 2:
        return plate.isalpha()
    # incase string is in range 2 & 6
    elif 2 < len(plate) <= 6:
        # check if special chars are present in the string
        if any(l in plate for l in ". !"):
            return False
        # check if first two chars are alphabets
        if not plate[:2].isalpha():
            return False
        # check if numbers are not in the middle of the string
        if plate[-1].isalpha() and any(c.isdigit() for c in plate[2:-1]):
            return False
        # check if first digit is 0
        first_digit = 0
        for l in plate:
            if l.isdigit():
                first_digit += 1
            if first_digit == 1 and l == "0":
                return False
        return True

    return False


if __name__ == "__main__":
    main()
