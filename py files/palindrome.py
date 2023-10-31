def is_palindrome_string(input_string):
    cleaned_string = ''.join(c for c in input_string if c.isalnum()).lower()
    return cleaned_string == cleaned_string[::-1]

def is_palindrome_number(input_number):
    return str(input_number) == str(input_number)[::-1]

while True:
    print("Palindrome Checker Menu:")
    print("1. Check if a string is a palindrome")
    print("2. Check if a number is a palindrome")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        input_string = input("Enter a string: ")
        if is_palindrome_string(input_string):
            print(f"'{input_string}' is a palindrome.")
        else:
            print(f"'{input_string}' is not a palindrome.")

    elif choice == '2':
        try:
            input_number = int(input("Enter a number: "))
            if is_palindrome_number(input_number):
                print(f"{input_number} is a palindrome.")
            else:
                print(f"{input_number} is not a palindrome.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
