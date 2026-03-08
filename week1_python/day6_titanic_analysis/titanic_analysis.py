from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "titanic.csv"


def main() -> None:
    df = pd.read_csv(DATA_FILE)

    print("Head: ")
    print(df.head(11))

    print("\nInfo: ")
    df.info()

    print("\nDescription: ")
    print(df.describe())

    empty_values = df.isna().sum()
    print("\nEmpty values: ")
    print(empty_values)

    df["Age"] = df["Age"].fillna(df["Age"].mean())
    print("\nEmpty values: ")
    print(df.isna().sum())

    survived = df["Survived"].mean()
    print(f"\nSurvived: {survived}")

    survived_by_sex = df.groupby("Sex")["Survived"].mean()
    print("\nSurvived by sex: ")
    print(survived_by_sex)

    survived_by_class = df.groupby("Pclass")["Survived"].mean()
    print("\nSurvived by class: ")
    print(survived_by_class)

    average_age = df["Age"].mean()
    print(f"\nAverage by age: {average_age}")

    most_expensive = df.sort_values("Fare", ascending=False).head(1)
    print("\nMost expensive ticket: ")
    print(most_expensive)

    df["fare_per_age"] = df["Fare"] / df["Age"]
    print("Head: ")
    print(df.head(11))


if __name__ == "__main__":
    main()
