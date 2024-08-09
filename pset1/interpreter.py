user_input = input("Expression: ")

x, y, z = user_input.split(" ")

a = float(x)
b = float(z)

match y:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case _:
        print("no such operator")


