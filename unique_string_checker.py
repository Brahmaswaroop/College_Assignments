def has_unique_characters(s):
    s = s.lower().replace(" ", "")
    unique_chars = set()
    for char in s:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    return True

input_string = input("Enter a string: ")
print(has_unique_characters(input_string))
