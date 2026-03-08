import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "dataset.csv"


def main() -> None:
    df = pd.read_csv(DATA_FILE)

    print("Head: ")
    print(df.head())

    print("\nInfo: ")
    df.info()

    print("\nDescription: ")
    print(df.describe())

    average_age = df["age"].mean()
    average_salary = df["salary"].mean()
    high_salary = df[df["salary"] > 65000]
    high_experience = df[df["experience"] > 5]
    city_salary = df.groupby("city")["salary"].mean()
    top_salary = df.sort_values("salary", ascending=False).head(3)

    df["salary_per_experience"] = df["salary"] / df["experience"]

    print(f"\nAverage age: {average_age}")
    print(f"\nAverage salary: {average_salary}")

    print(f"\nSalary > 65000: {high_salary}")
    print(f"\nExperience > 5: {high_experience}")
    print(f"\nAverage salary by city: {city_salary}")
    print(f"\nTop 3 salary: {top_salary}")
    print("\nDataset with salary_per_experience:")
    print(df)


if __name__ == "__main__":
    main()
