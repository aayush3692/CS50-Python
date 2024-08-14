from pyfiglet import Figlet
import sys
import random

def main():
    print_input()

def print_input():
    figlet = Figlet()

    if len(sys.argv) == 1:
            # No arguments: use a random font
            figlet.setFont(font= random.choice(figlet.getFonts()))
            user_input = input("Input: ")
            print(figlet.renderText(f"{user_input}"))

    elif len(sys.argv) == 3:
        if sys.argv[1] in ['-f', '--font']:
            font = sys.argv[2]
            if font in figlet.getFonts():
                figlet.setFont(font=font)
                user_input = input("Input: ")
                print(figlet.renderText(f"{user_input}"))
            else:
                 sys.exit("Invalid usage")
        else:
             sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
