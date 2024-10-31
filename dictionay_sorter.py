from ast import literal_eval

def dict_sort(dict1):
    temp = literal_eval(dict1)
    temp = list(dict1)
    temp.sort()
    sorted_dict = {i: dict1[i] for i in temp}
    return sorted_dict

try:
    x = input("Enter the entire dictionary with braces:\n")
    in_dict = literal_eval(x)
    print(dict_sort(x))
except ValueError:
    print("Enter a valid response.")
    print("Eg:  {'name': 'John'}")
