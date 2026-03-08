from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "titanic.csv"


def main() -> None:
    df = pd.read_csv(DATA_FILE)

    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

    df["Age"] = df["Age"].fillna(df["Age"].mean())

    X = df[["Pclass", "Sex", "Age", "Fare"]]
    y = df["Survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print(predictions)

    accuracy = accuracy_score(y_test, predictions)

    print("Accuracy:", accuracy)


if __name__ == "__main__":
    main()
