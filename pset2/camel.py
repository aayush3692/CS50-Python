user_input = input("camelCase: ")
snake_case = []

for char in user_input:
    if char.isupper():
       if snake_case:
           snake_case.append('_')
       snake_case.append(char.lower())
    else:
        snake_case.append(char)

snake_case_string = ''.join(snake_case)


print("snake_case: "+snake_case_string)



