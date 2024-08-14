import inflect

def main():
    print_adieu()

def print_adieu():
    p = inflect.engine()
    name_list = []
    while True:
        try:
            name = input("name:").strip().title()
            name_list.append(name)

        except EOFError:
            print()
            print("Adieu, adieu, to", p.join(name_list))
            break


if __name__ == "__main__":
    main()


