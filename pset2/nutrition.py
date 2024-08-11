def main():
    user_input = input("Item: ")

    fruits = [
        {"fruit": "apple", "calories": "130"},
        {"fruit": "Avocado", "calories": "50"},
        {"fruit": "banana", "calories": "110"},
        {"fruit": "cantaloupe", "calories": "50"},
        {"fruit": "grapefruit", "calories": "60"},
        {"fruit": "grapes", "calories": "90"},
        {"fruit": "honeydew melon", "calories": "50"},
        {"fruit": "Kiwifruit", "calories": "90"},
        {"fruit": "lemon", "calories": "15"},
        {"fruit": "lime", "calories": "20"},
        {"fruit": "nectarine", "calories": "60"},
        {"fruit": "orange", "calories": "80"},
        {"fruit": "peach", "calories": "60"},
        {"fruit": "pear", "calories": "100"},
        {"fruit": "plums", "calories": "50"},
        {"fruit": "pineapple", "calories": "50"},
        {"fruit": "strawberries", "calories": "50"},
        {"fruit": "Sweet Cherries", "calories": "100"},
        {"fruit": "tangerine", "calories": "50"},
        {"fruit": "watermelon", "calories": "80"},
    ]

    for fruit in fruits:
        if fruit["fruit"] == user_input:
            print("Calories: "+fruit["calories"])


main()

