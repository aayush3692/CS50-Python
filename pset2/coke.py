def main():
    accepted_coins = [25, 10, 5]
    total_amount = 0
    price = 50

    print(f"Amount Due: {price}")

    while total_amount < price:
        # Prompt user to insert a coin
        coin = int(input("Insert Coin: "))

        # Check if the coin is accepted
        if coin in accepted_coins:
            total_amount += coin
            amount_due = price - total_amount

            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
            else:
                print("Amount Due: 0 cents")
        else:
            # When an invalid coin is inserted, re-display the amount due
            print(f"Amount Due: {price - total_amount}")

    # Calculate and display change
    change = total_amount - price
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()
