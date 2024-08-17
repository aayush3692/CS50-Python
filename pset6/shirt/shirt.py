from PIL import Image, ImageOps
import sys
from os.path import splitext

def main():
    convert_image()

def convert_image():
    length = len(sys.argv)

    if length < 3:
        sys.exit("Too few command-line arguments")
    elif length > 3:
        sys.exit("Too many command-line arguments")

    elif splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")

    elif splitext(sys.argv[1])[1] not in ['.jpg', '.png', '.jpeg']:
        sys.exit("Invalid output")
    else:
        try:
            shirt = Image.open("shirt.png")
            input_image = Image.open(sys.argv[1])

            input_image = ImageOps.fit(input_image, shirt.size)

            input_image.paste(shirt, shirt)
            input_image.save(sys.argv[2])

        except FileNotFoundError:
            sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
