from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "titanic.csv"


def main() -> None:
    df = pd.read_csv(DATA_FILE)

    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

    df["Age"] = df["Age"].fillna(df["Age"].mean())

    df["is_child"] = (df["Age"] < 16).astype(int)

    df["fare_per_age"] = round(df["Fare"] / df["Age"], 2)

    X = df[["Pclass", "Sex", "Age", "Fare", "is_child", "fare_per_age"]]
    y = df["Survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("Accuracy:", accuracy)


if __name__ == "__main__":
    main()
