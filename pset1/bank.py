word = input("Greeting: ")

greetings = word.lower()

if 'hello' in greetings:
   print("$0")
elif greetings.startswith('h'):
   print("$20")
else:
   print("$100")
