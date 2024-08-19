from tabulate import tabulate
import sys
import csv

def main():
    make_table()

def make_table():
    length = len(sys.argv)
    # Initialize an empty list to store pizza data (not used directly here)
    pizza = []
    if length < 2:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")
    # Check if the provided file has a ".csv" extension    
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    else:
        try:
            # Attempt to open the specified CSV file
            with open(sys.argv[1]) as file:
                # Read the CSV file and print it as a formatted table using tabulate
                print(tabulate(csv.DictReader(file), headers="keys", tablefmt="grid"))

        # Handle the case where the specified file does not exist
        except FileNotFoundError:
            sys.exit("File does not exist")



main()
