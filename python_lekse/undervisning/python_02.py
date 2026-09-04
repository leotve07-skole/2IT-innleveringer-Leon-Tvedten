user_input = input("Hello \n")
try:
    user_input = int(user_input)

except ValueError:
    user_input = str(user_input)

if user_input == 42:
    print("Hello")
elif user_input == 41 or user_input == 43:
    print("hello 313")
else:
    print("Hello 2")