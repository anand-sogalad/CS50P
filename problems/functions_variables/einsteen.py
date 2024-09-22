def main():
    mass = get_user_input()
    energy = calculate_energy(mass)
    print(energy)


def get_user_input():
    return int(input())


def calculate_energy(m):
    return m * 300000000 ** 2


if __name__ == "__main__":
    main()
