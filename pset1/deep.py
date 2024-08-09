answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

# Normalize the input by converting to lowercase and stripping spaces
normalized_answer = answer.lower().strip()

if normalized_answer == "42" or normalized_answer == "forty-two" or normalized_answer == "forty two":
    print("Yes")
else:
    print("No")
