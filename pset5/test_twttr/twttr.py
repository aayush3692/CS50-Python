import string
def main():
    user_input = input("Input: ")
    short = shorten(user_input)
    print(short)


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']#, 'A', 'E', 'I', 'O', 'U']
    short_word = ""
    for char in word:
        if char not in vowels: #and char not in string.digits and char not in string.punctuation:
            short_word += char
    return short_word



if __name__ == "__main__":
    main()
