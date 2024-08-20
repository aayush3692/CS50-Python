import re

def main():
    # Prompt the user to input an IPv4 address and print whether it's valid
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Check if the input matches the IPv4 format: four groups of 1 to 3 digits separated by periods
    if not re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return False
    
    # Split the IP address into its four components and validate each one
    for num in ip.split("."):
        # Convert the component to an integer and check if it's in the valid range (0 to 255)
        if int(num) < 0 or int(num) > 255:
            return False
    
    # If all components are valid, return True
    return True

if __name__ == "__main__":
    main()
