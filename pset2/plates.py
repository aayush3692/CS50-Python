def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    length = len(s)

    # Requirement 1: Plate length must be between 2 and 6 characters
    if length < 2 or length > 6:
        return False

    ###All vanity plates must start with at least two letters.”
    if not s[:2].isalpha():
        return False

    #Numbers cannot be used in the middle of a plate; they must come at the end. For example,
    # AAA222 would be an acceptable … vanity plate;
    # AAA22A would not be acceptable. The first number used cannot be a ‘0’.
    # Identify the start index of numbers, if any
    first_number_index = len(s)
    for i in range(length):
        if s[i].isdigit():
            first_number_index = i
            break

    # Requirement 3: Numbers cannot be in the middle and the first number cannot be '0'
    if first_number_index < length:
        # Check if there are non-letters before the first number index
        for i in range(first_number_index):
            if not s[i].isalpha():
                return False
        # Check if the first number is '0'
        if s[first_number_index] == '0':
            return False

        # Ensure all characters after the first number index are digits
        for i in range(first_number_index + 1, length):
            if not s[i].isdigit():
                return False

    return True

main()

