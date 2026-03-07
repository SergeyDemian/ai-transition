def squares_of_even_numbers(items: list[int]) -> list[int]:
    return [item**2 for item in items if item % 2 == 0]


if __name__ == "__main__":
    print(squares_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
