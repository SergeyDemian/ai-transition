import re
from collections import Counter


def word_counter(text: str) -> dict[str, int]:
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))


def remove_duplicates(items: list) -> list[int]:
    check_set = set()
    unique_list = []

    for i in items:
        if i not in check_set:
            unique_list.append(i)
            check_set.add(i)

    return unique_list


def top_three_elements(items: list) -> list[int]:
    counter = Counter(items)
    return [item for item, _ in counter.most_common(3)]


def reverse_dict(data: dict[str, int]) -> dict[int, str]:
    return {v: k for k, v in data.items()}


def group_by_letter(items: list[str]) -> dict[str, list[str]]:
    grouped = {}
    for item in items:
        first_letter = item[0].lower()
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(item)
    return grouped


if __name__ == '__main__':
    print(word_counter("Привет, как у тебя дела? Привет, хорошо. Хорошо, это хорошо, когда хорошо."))
    print(remove_duplicates([1, 2, 4, 4, 5, 5, 5, 6, 1, 3, 6, 8, 8]))
    print(top_three_elements([1, 2, 4, 4, 5, 5, 5, 6, 1, 3, 6, 6, 6, 8]))
    print(reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
    print(group_by_letter(
        ['Привет', 'как,', 'у', 'тебя', 'дела', 'Привет', 'хорошо', 'Хорошо', 'это', 'хорошо', 'когда', 'хорошо']))
