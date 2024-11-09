from ast import literal_eval

def dict_sort(dict1):
    sorted_dict = {i: dict1[i] for i in sorted(dict1)}
    return sorted_dict

try:
    x = input("Enter the entire dictionary with braces:\n")
    in_dict = literal_eval(x)
    print(dict_sort(in_dict))
except ValueError:
    print("Enter a valid response.")
    print("Eg:  {'name': 'John'}")
