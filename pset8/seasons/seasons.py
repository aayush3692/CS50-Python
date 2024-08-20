from datetime import date
import sys
import inflect


def get_total_minutes(birth_date, today):
    # Calculate the difference in days between today and the birth date, then convert to minutes
    return (today - birth_date).days * 24 * 60


def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid input!")
    # Get the current date and calculate the total number of minutes since the birth date
    total_minutes = get_total_minutes(birth_date, date.today())

    # Initialize the inflect engine for converting numbers to words
    p = inflect.engine()
    # Convert the total number of minutes to words and print the result, ensuring proper pluralization
    print(f"{p.number_to_words(total_minutes, andword="").capitalize()} {p.plural('minute')}")


if __name__ == "__main__":
    main()
