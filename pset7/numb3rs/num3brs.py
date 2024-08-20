import re

def main():
    # Prompt the user to input an IPv4 address and print whether it's valid
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Define a regex pattern to match a valid IPv4 address
    # Each section of the IP (octet) must be between 0 and 255
    # The pattern checks for four groups of numbers separated by dots
    if re.search(
        r"^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
        r"([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
        r"([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
        r"([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip):
        return True  # Return True if the IP address matches the pattern
    else:
        return False  # Return False if the IP address does not match the pattern

if __name__ == "__main__":
    main()
