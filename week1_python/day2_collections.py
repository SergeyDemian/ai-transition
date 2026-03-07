def squares_of_even_numbers(items: list[int]) -> list[int]:
    return [item**2 for item in items if item % 2 == 0]


def dictionary_for_word_len(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

def sorted_list_of_words(items: list[str]) -> list[str]:
    return sorted(items, key=len)

def multiplication_by_ten(items: list[int]) -> list[int]:
    return list(map(lambda item: item * 10, items))


if __name__ == "__main__":
    print(squares_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(dictionary_for_word_len(["apple","banana","kiwi","pear","watermelon"]))
    print(sorted_list_of_words(["cat","elephant","dog","hippopotamus"]))
    print(multiplication_by_ten([1,2,3,4,5]))
