def main():
    check_tank()

def check_tank():
    while True:
        try:
            x = input("Fraction: ")
            #Split the string by '/'
            a,b = x.split('/')
            num = int(a)
            dem = int(b)
            # Check if the numerator is greater than the denominator
            if num > dem:
                # If numerator is greater, ask for input again
                continue
            else:
                result = round((num / dem)*100)
                if result <= 1:
                    print("E")  # Almost empty
                elif result >= 99:
                    print("F")  # Full
                else:
                    print(f"{result}%") # Print the percentage
        except ValueError:
            # Handle the case where the input cannot be converted to integers
            pass
        except ZeroDivisionError:
             # Handle the case where the denominator is zero
            pass
        else:
             # Exit the loop if no exceptions occurred and input is valid
            break

if __name__ =="__main__":
    main()
