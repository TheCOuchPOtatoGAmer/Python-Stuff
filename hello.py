'''
Ask user for their name
Remove whitespace from str
Capitalises first letter
'''
name = input("What's your name? ")
name = name.strip().capitalize()
name = name.title()

# Printing Message
def print_message(message):
    print(message)

# Print Result
string_to_print = f"Hello {name}"
print_message(string_to_print) 