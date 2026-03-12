from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "customer_churn.csv"


def print_metrix(name: str, y_true, predictions) -> None:
    print(f"\n{name}")
    print("y_test and predictions: ")
    print(f"\n{y_true} and {predictions}")
    print("Accuracy:", accuracy_score(y_true, predictions))
    print("Precision:", precision_score(y_true, predictions, zero_division=0))
    print("Recall:", recall_score(y_true, predictions, zero_division=0))
    print("F1:", f1_score(y_true, predictions, zero_division=0))
    print("Confusion matrix [[TN, FP], [FN, TP]]:")
    print(confusion_matrix(y_true, predictions))


def main() -> None:
    df = pd.read_csv(DATA_FILE)

    print("Head: ")
    print(df.head())

    print("\nInfo: ")
    df.info()

    print("\nDescription: ")
    print(df.describe())

    print("\nEmpty values: ")
    print(df.isna().sum())

    average_age = round(df["age"].mean(), 2)
    average_monthly_charge = round(df["monthly_charges"].mean(), 2)
    churn_clients = (df["churn"] == 1).sum()
    churn_rate_by_gender = round(df.groupby("gender")["churn"].mean(), 2)

    df["tenure_group"] = np.where(
        df["tenure"] < 6, "new", np.where(df["tenure"] > 24, "loyal", "medium")
    )
    df["charges_per_month"] = df["total_charges"] / df["tenure"]
    df["high_support"] = (df["support_calls"] > 3).astype(int)

    df["gender"] = df["gender"].map({"female": 0, "male": 1})
    df["contract_type"] = df["contract_type"].map(
        {"month-to-month": 0, "one-year": 1, "two-year": 2}
    )
    df["tenure_group"] = df["tenure_group"].map({"new": 0, "medium": 1, "loyal": 2})

    print(f"\nAverage age: {average_age}")
    print(f"\nAverage monthly charge: {average_monthly_charge}")
    print(f"\nChurn clients: {churn_clients}")
    print(f"\nChurn rate by gender: {churn_rate_by_gender}")

    X = df[
        [
            "age",
            "gender",
            "tenure",
            "monthly_charges",
            "support_calls",
            "charges_per_month",
            "high_support",
            "contract_type",
            "tenure_group",
        ]
    ]

    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = LogisticRegression()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print_metrix("Model LogisticRegression", y_test, predictions)

    model_dt = DecisionTreeClassifier()

    model_dt.fit(X_train, y_train)

    predictions_dt = model_dt.predict(X_test)

    print_metrix("Model DecisionTreeRegressor", y_test, predictions_dt)


if __name__ == "__main__":
    main()
