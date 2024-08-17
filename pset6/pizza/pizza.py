from tabulate import tabulate
import sys
import csv

def main():
    make_table()

def make_table():
    length = len(sys.argv)
    pizza = []
    if length < 2:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    else:
        try:
            with open(sys.argv[1]) as file:
                 print(tabulate(csv.DictReader(file), headers="keys", tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exist")



main()
