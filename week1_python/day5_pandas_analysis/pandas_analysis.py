import pandas as pd


def main() -> None:
    df = pd.read_csv("dataset.csv")
    print(df)

    print(df.head())
    print(df.info())
    print(df.describe())

    print(df["age"].mean())
    print(df["salary"].mean())

    print(df[df["salary"] > 65000])
    print(df[df["experience"] > 5])
    print(df.groupby("city")["salary"].mean())
    print(df.sort_values("salary", ascending=False).head(3))
    df["salary_per_experience"] = df["salary"] / df["experience"]
    print(df)


if __name__ == "__main__":
    main()
