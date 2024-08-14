def main():
    change_date()

def change_date():
    while True:
        try:
            date_input = input("Date: ")

            if '/' in date_input:
                month, day, year = date_input.split('/')
                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= day <= 31 and 1 <= month <= 12:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

            elif ',' in date_input:
                month_day, year = date_input.split(',')
                year = int(year)
                month_name, day = month_day.split()
                day = int(day)
                months =   [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December"
                ]

                if month_name in months and 1 <= day <= 31:
                    month = months.index(month_name) + 1
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

        except ValueError:
            pass





if __name__  == "__main__":
    main()
