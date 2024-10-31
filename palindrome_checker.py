def is_palindrome(string):
    string = string.lower().replace(" ", "")
    if string == string[::-1]:
        return True
    else:
        return False

x = input("Enter a string: ")
if is_palindrome(x):
    print(f"{x} is a palindrome.")
else:
    print(f"{x} is not a palindrome.")
