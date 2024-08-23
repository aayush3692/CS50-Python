import random

def main():
    guess_number()

def guess_number():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                pass # Re-prompt for a valid level
            number = random.randint(1, level)# Generate random number within the level range
            break # Exit the loop after getting a valid level
        except ValueError:
            pass


    while True:
        try:
            x = int(input("Guess: "))
            if x < number:
                print("Too small!")
            elif x > number:
                print("Too large!")
            else:
                print("Just right!")
                break # Exit the loop when the correct guess is made
        except ValueError:
            pass


if __name__ == "__main__":
    main()


