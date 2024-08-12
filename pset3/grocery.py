def main():
    check_grocery()

def check_grocery():
    data = {}  # Dictionary to store counts of each value

    while True:
        try:
            # Prompt for user input
            value = input("").strip()  # Strip any extra whitespace

            # Convert value to uppercase
            upper_value = value.upper()


            # Update the count of the value in the dictionary
            if upper_value in data:
                data[upper_value] += 1
            else:
                data[upper_value] = 1



        except EOFError:
            # Handle end-of-file error to break the loop and exit
            print("\n")
            break

    sorted_list = sorted(data.items())
    # Print all values and their counts
    for item, count in sorted_list:
        print(f"{count} {item}")

if __name__ == "__main__":
    main()
