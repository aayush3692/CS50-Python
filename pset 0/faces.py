def main():

    phrase = input()
    answer = convert(phrase)
    print(answer)

def convert(word):
    word = word.replace(':)', '🙂')
    word = word.replace(':(', '🙁')
    return word

main()




