from pathlib import Path

import pandas as pd
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "titanic.csv"


def print_metrics(name: str, y_true, predictions) -> None:
    print(f"\n{name}")
    print("y_test and predictions: ")
    print("y_test:")
    print(y_true.values)
    print("predictions:")
    print(predictions)
    print("Accuracy:", accuracy_score(y_true, predictions))
    print("Precision:", precision_score(y_true, predictions, zero_division=0))
    print("Recall:", recall_score(y_true, predictions, zero_division=0))
    print("F1:", f1_score(y_true, predictions, zero_division=0))
    print("Confusion matrix [[TN, FP], [FN, TP]]:")
    print(confusion_matrix(y_true, predictions))


def print_data_info(df: DataFrame) -> None:
    print("Head: ")
    print(df.head())

    print("\nInfo: ")
    df.info()

    print("\nDescription: ")
    print(df.describe())


def calc_scores(name: str, model, X: DataFrame, y: DataFrame) -> None:
    scores = cross_val_score(model, X, y, cv=5)
    print(f"\n{name}")
    print("Scores: ")
    print(scores)
    print("Mean scores: ")
    print(scores.mean())


def evaluate_model(name: str, X_train, X_test, y_train, y_test) -> object:
    model = create_model(name)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print_metrics(f"Model {name}", y_test, predictions)
    return model


def create_model(name: str) -> object:
    match name:
        case "LogisticRegression":
            model = LogisticRegression(max_iter=1000)
        case "DecisionTreeClassifier":
            model = DecisionTreeClassifier(random_state=42, max_depth=4)
        case "RandomForestClassifier":
            model = RandomForestClassifier(n_estimators=100, random_state=42)
        case _:
            raise ValueError(f"Unknown model: {name}")
    return model


def main() -> None:
    df = pd.read_csv(DATA_FILE)

    print_data_info(df)

    print("Print empty values: ")
    print(df.isna().sum())

    df["family_size"] = df["SibSp"] + df["Parch"] + 1
    df["is_alone"] = (df["family_size"] == 1).astype(int)
    df["fare_per_person"] = df["Fare"] / df["family_size"]
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].fillna("S")
    df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

    df["Age"] = df["Age"].fillna(df["Age"].median())

    X = df[
        [
            "Pclass",
            "Sex",
            "Age",
            "SibSp",
            "Parch",
            "Fare",
            "Embarked",
            "family_size",
            "is_alone",
            "fare_per_person",
        ]
    ]

    y = df["Survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model_lr = evaluate_model("LogisticRegression", X_train, X_test, y_train, y_test)
    model_dtc = evaluate_model(
        "DecisionTreeClassifier", X_train, X_test, y_train, y_test
    )
    model_rfc = evaluate_model(
        "RandomForestClassifier", X_train, X_test, y_train, y_test
    )

    calc_scores("LogisticRegression", model_lr, X, y)
    calc_scores("DecisionTreeClassifier", model_dtc, X, y)
    calc_scores("RandomForestClassifier", model_rfc, X, y)


if __name__ == "__main__":
    main()
