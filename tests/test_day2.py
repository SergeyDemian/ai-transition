from week1_python.day2_collections import (
    squares_of_even_numbers,
    dictionary_for_word_len,
)


def test_squares_of_even_numbers():
    assert squares_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [4, 16, 36, 64]


def test_dictionary_for_word_len():
    assert dictionary_for_word_len(
        ["apple", "banana", "kiwi", "pear", "watermelon"]
    ) == {"apple": 5, "banana": 6, "kiwi": 4, "pear": 4, "watermelon": 10}


if __name__ == "__main__":
    test_squares_of_even_numbers()
    test_dictionary_for_word_len()
    print("Everything passed")
