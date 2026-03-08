import numpy as np


def min_max_normalization(scores: np.ndarray) -> np.ndarray:
    return (scores - np.min(scores)) / (np.max(scores) - np.min(scores))


def main() -> None:
    scores = np.array([78, 92, 85, 67, 90, 73, 88, 95, 64, 82])

    print(f"Mean score: {np.mean(scores)}")
    print(f"Median score: {np.median(scores)}")
    print(f"Std: {np.std(scores)}")
    print(f"Min: {np.min(scores)}")
    print(f"Max: {np.max(scores)}")

    print(f"Scores > 85: {scores[scores > 85]}")
    print(f"Scores < 70: {scores[scores < 70]}")
    print(f"Normalized scores: {min_max_normalization(scores)}")

    print(f"Best student index: {np.argmax(scores)}")
    matrix = scores.reshape(2, 5)
    print(f"Matrix: \n{matrix}")
    print(f"Group averages: {np.mean(matrix, axis=1)}")


if __name__ == "__main__":
    main()
