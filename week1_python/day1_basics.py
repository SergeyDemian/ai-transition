import re

def word_counter():
    frase = "Привет, как у тебя дела? Привет, хорошо. Хорошо, это хорошо, когда хорошо."
    words = re.findall(r'\b\w+\b', frase.lower())
    return dict((i, words.count(i)) for i in words)

def remove_duplicates():
    original_list = [1, 2, 4, 4, 5, 5, 5, 6, 1, 3, 6, 8, 8]
    check_set = set()
    unique_list = []
    for i in original_list:
        if i not in check_set:
            unique_list.append(i)
            check_set.add(i)

    return unique_list

def three_elements():
    original_list = [1, 2, 4, 4, 5, 5, 5, 6, 1, 3, 6, 6, 6, 8]
    dictionary = dict((i, original_list.count(i)) for i in original_list)
    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True) [:3])
    return list(sorted_dictionary)


def revers_dict():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    reversed_dict = {v: k for k, v in my_dict.items()}
    return reversed_dict

def group_by_letter():
    origin_list = ['Привет', 'как,', 'у', 'тебя', 'дела', 'Привет', 'хорошо', 'Хорошо', 'это', 'хорошо', 'когда', 'хорошо']
    grouped = {}
    for item in origin_list:
        first_letter = item[0].lower()
        if first_letter not in grouped.keys():
            grouped[first_letter] = []

        grouped[first_letter].append(item)

    return grouped

if __name__ == '__main__':
    print(word_counter())
    print(remove_duplicates())
    print(three_elements())
    print(revers_dict())
    print(group_by_letter())