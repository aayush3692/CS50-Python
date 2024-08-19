import validators  # Import the validators module for email validation

def main():
    # Prompt the user for their email address and print the validation result
    print(validate(input("What's your email address? ")))

def validate(s):
    # Check if the provided string is a valid email address
    if validators.email(s):
        return "Valid"   # Return "Valid" if the email address is valid
    else:
        return "Invalid" # Return "Invalid" if the email address is not valid

if __name__ == "__main__":
    main()
