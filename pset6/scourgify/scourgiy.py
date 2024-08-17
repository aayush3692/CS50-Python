import csv
import sys

def main():
    write_csv()

def write_csv():

    length = len(sys.argv)
    if length < 3:
        sys.exit("Too few command-line arguments")
    elif length > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            with open(sys.argv[1], "r") as read, open(sys.argv[2], "w") as write:

                reader = csv.DictReader(read)
                writer = csv.DictWriter(write,fieldnames=["first", "last", "house"])
                writer.writeheader()

                for row in reader:
                    last_name, first_name = row["name"].split(',')
                    last = last_name.strip()

                    first = first_name.strip()

                    writer.writerow({"first":first, "last":last, "house":row['house']})


        except FileNotFoundError:
            sys.exit("Could not read invalid_file.csv")

if __name__ == "__main__":
    main()
