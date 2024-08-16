
def main():
    while True:
        try:
            x = input("Fraction: ")
            print(f"{gauge(convert(x))}")
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def convert(fraction):
    while True:
        #Split the string by '/'
        a,b = fraction.split('/')
        num = int(a)
        dem = int(b)
        # Check if the numerator is greater than the denominator
        if num > dem:
                # If numerator is greater, ask for input again
            fraction = input("Fraction: ")
            continue
        else:
            result = round((num / dem)*100)
            return result

def gauge(percentage):

    if percentage <= 1:
        return "E"  # Almost empty
    elif percentage >= 99:
        return "F"  # Full
    else:
        return f"{percentage}%" # Print the percentage


if __name__ =="__main__":
    main()
