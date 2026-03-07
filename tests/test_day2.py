from week1_python.day2_collections import (
    squares_of_even_numbers,
    dictionary_for_word_len,
    sorted_list_of_words,
    multiplication_by_ten,
    remove_empty_strings,
)


def test_squares_of_even_numbers():
    assert squares_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [4, 16, 36, 64]


def test_dictionary_for_word_len():
    assert dictionary_for_word_len(
        ["apple", "banana", "kiwi", "pear", "watermelon"]
    ) == {"apple": 5, "banana": 6, "kiwi": 4, "pear": 4, "watermelon": 10}


def test_sorted_list_of_words():
    assert sorted_list_of_words(["cat", "elephant", "dog", "hippopotamus"]) == [
        "cat",
        "dog",
        "elephant",
        "hippopotamus",
    ]


def test_multiplication_by_ten():
    assert multiplication_by_ten([1, 2, 3, 4, 5]) == [10, 20, 30, 40, 50]


def test_remove_empty_strings():
    assert remove_empty_strings(["AI", "ML", "", "Python", "", "Data"]) == [
        "AI",
        "ML",
        "Python",
        "Data",
    ]


if __name__ == "__main__":
    test_squares_of_even_numbers()
    test_dictionary_for_word_len()
    test_sorted_list_of_words()
    test_multiplication_by_ten()
    test_remove_empty_strings()
    print("Everything passed")
