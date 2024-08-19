import sys

def main():
    count_lines()

def count_lines():
    length = len(sys.argv)
    if length < 2:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        try:
            # Open the Python file specified by the user
            with open(sys.argv[1]) as file:
                
                # Count and print the number of lines that are not empty or comments
                print(
                    sum(
                        1 for line in file 
                        if line.strip() and not line.lstrip().startswith('#')
                    )
                )

        except FileNotFoundError:
            # Handle the case where the specified file does not exist
            sys.exit("File does not exist")



if __name__ == "__main__":
    main()
