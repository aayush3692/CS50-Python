import random


def main():
    eqn = 10
    chances = 3
    score = 0
    n = get_level()

    while eqn != 0:
        if chances == 3:
            x,y = generate_integer(n)
        try:
            choice = int(input(f"{x} + {y} = "))
            sum = x+y
            if choice == sum:
                eqn -= 1
                score += 1
                chances = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances -= 1
            pass
        if chances == 0:
            print(f"{x} + {y} = {sum}")
            eqn -= 1
            chances = 3
            continue
    print(f"score = {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x,y



if __name__ == "__main__":
    main()
