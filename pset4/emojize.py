import emoji

def main():
    know_emoji()

def know_emoji():
    user_input = input("Input: ")
   # print(emoji.emojize('Output: :red_heart:'))

    print(emoji.emojize(f'Output: {user_input}', language='alias'))

if __name__ == "__main__":
    main()
