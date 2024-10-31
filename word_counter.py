import re
def word_count(sen):
    sen_dict = {}
    sen_list = re.sub(r'[^a-zA-Z0-9]', ' ', sen.lower())    # replace all symbols with space
    sen_list = re.sub(r'\s+', ' ', sen_list)    # remove multiple spaces with a single space
    sen_list = re.split(r' ', sen_list)  # separating words by space or comma
    sen_list.remove('') if '' in sen_list else None
    for i in sen_list:
        if i in sen_dict:
            sen_dict[i] += 1
        else:
            sen_dict.update({i: 1})
    return sen_dict

x = input("Enter the sentence:\n")
print("\n", word_count(x))
