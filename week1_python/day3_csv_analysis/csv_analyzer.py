import csv
from collections import Counter
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.csv"
REPORT_FILE = BASE_DIR / "report.json"


def sum_by_parameter(parameter: str, rows: list[dict[str, str]]) -> int:
    return sum(int(row[parameter]) for row in rows)


def data_average(parameter: str, rows: list[dict[str, int]]) -> float:
    return round(sum_by_parameter(parameter, rows) / len(rows), 2)


def city_counter(rows: list[dict[str, int]]) -> dict[str, int]:
    return dict(Counter(row["city"] for row in rows))


def highest_paid(rows: list[dict[str, str]]) -> dict[str, str]:
    return max(rows, key=lambda x: int(x["salary"]))


def main():
    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        person = highest_paid(rows)

        highest_paid_data = {"name": person["name"], "salary": person["salary"]}
        report = {
            "total_rows": len(rows),
            "average_age": data_average("age", rows),
            "average_salary": data_average("salary", rows),
            "city_distribution": city_counter(rows),
            "highest_paid": highest_paid_data,
        }

        print(f"Total rows: {report['total_rows']}")
        print(f"Average age: {report['average_age']}")
        print(f"Average salary: {report['average_salary']}")
        print(f"Cities: {report['city_distribution']}")
        print(f"Highest paid: {report['highest_paid']})")

    with REPORT_FILE.open("w") as file:
        json.dump(report, file, indent=4)


if __name__ == "__main__":
    main()
