import pyfiglet
import sys
import random


def main():

    figlet = pyfiglet.Figlet()

    if len(sys.argv) == 0:
        figlet.setFont(font=random.choice(figlet.getFonts()))
    elif len(sys.argv) == 3:
        if check_f(sys.argv[1]) and check_font(sys.argv[2]):
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print("Output:\n", figlet.renderText(text))


def check_font(font):
    return font in pyfiglet.Figlet().getFonts()


def check_f(str):
    return str == "-f" or str == "--font"

if __name__ == "__main__":
    main()
