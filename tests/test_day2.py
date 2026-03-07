from week1_python.day2_collections import squares_of_even_numbers


def test_squares_of_even_numbers():
    assert squares_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [4, 16, 36, 64]


if __name__ == "__main__":
    test_squares_of_even_numbers()
    print("Everything passed")
