def main():
    print_price()


def print_price():
    total = 0.00
    while True:
        try:
            user_input = input("Item: ")
            item = user_input.title()
            menu = {
                "Baja Taco": 4.25,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
            }
            # Check if user_input is in the menu
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")

        except EOFError:
            # Handle end-of-file error to break the loop and exit
            print("\n")
            break


if __name__ == "__main__":
    main()
