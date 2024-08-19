import re
import sys

def main():
    # Prompt the user to input a text and print the number of times "um" occurs
    print(count(input("Text: ")))

def count(s):
    # Define a regex pattern to match the word "um" as a whole word
    # \b is a word boundary, ensuring "um" is matched as a separate word
    regex = r"\bum\b"

    # Use re.findall to find all occurrences of "um" in the text, ignoring case
    # len(re.findall(...)) returns the total count of matches
    return len(re.findall(regex, s, re.IGNORECASE))

if __name__ == "__main__":
    main()
