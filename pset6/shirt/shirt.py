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
            # Open the "shirt.png" image, which will be used as an overlay
            shirt = Image.open("shirt.png")
            
            # Open the input image specified by the user
            input_image = Image.open(sys.argv[1])

            # Resize the input image to match the size of the "shirt.png" image
            input_image = ImageOps.fit(input_image, shirt.size)

            # Paste the "shirt.png" image onto the resized input image
            input_image.paste(shirt, shirt)

            # Save the modified image to the output file specified by the user
            input_image.save(sys.argv[2])

        except FileNotFoundError:
            # Handle the case where the input image file does not exist
            sys.exit("Input does not exist")



if __name__ == "__main__":
    main()
