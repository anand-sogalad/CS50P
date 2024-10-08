import sys

from pyfiglet import Figlet


def main():
    figlet = check_argv()
    reder_figlet(get_input(), figlet)
    ...


def check_argv():
    if not (1 < len(sys.argv) < 3 or len(sys.argv) > 3):
        if (
            len(sys.argv) == 3
            and sys.argv[1] in ("-f", "--font")
            and sys.argv[2] in Figlet().getFonts()
        ):
            return Figlet(font=sys.argv[2])
        return Figlet()
    sys.exit("Invalid usage")


def get_input():
    return input("Input: ")


def reder_figlet(input, figlet):
    print(figlet.renderText(input))


if __name__ == "__main__":
    main()
