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
            # Open the input CSV file for reading and the output CSV file for writing
            with open(sys.argv[1], "r") as read, open(sys.argv[2], "w") as write:

                # Create a DictReader to read the input CSV file as a dictionary
                reader = csv.DictReader(read)

                # Create a DictWriter to write to the output CSV file with specified fieldnames
                writer = csv.DictWriter(write, fieldnames=["first", "last", "house"])

                # Write the header row to the output CSV file
                writer.writeheader()

                # Iterate over each row in the input CSV file
                for row in reader:
                    # Split the "name" field into last name and first name
                    last_name, first_name = row["name"].split(',')
                    
                    # Strip any leading/trailing whitespace from the last name
                    last = last_name.strip()

                    # Strip any leading/trailing whitespace from the first name
                    first = first_name.strip()

                    # Write the formatted row to the output CSV file
                    writer.writerow({"first": first, "last": last, "house": row['house']})

        except FileNotFoundError:
            # Handle the case where the input CSV file does not exist
            sys.exit("Could not read invalid_file.csv")


if __name__ == "__main__":
    main()
