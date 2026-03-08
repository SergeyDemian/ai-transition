import csv
from collections import Counter
import json


def sum_by_parameter(parameter: str, rows: list[dict[str, int]]) -> int:
    return sum([int(row[parameter]) for row in rows])


def data_average(parameter: str, rows: list[dict[str, int]]) -> float:
    return round(sum_by_parameter(parameter, rows) / len(rows), 2)


def city_counter(rows: list[dict[str, int]]) -> dict[str, int]:
    return dict(Counter(list([row["city"] for row in rows])))


def highest_paid(rows: list[dict[str, str]]) -> dict[str, str]:
    return max(rows, key=lambda x: int(x["salary"]))


def main():
    with open("data.csv") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        dict_highest_paid = {
            k: v for k, v in highest_paid(rows).items() if k == "name" or k == "salary"
        }
        rows_length = len(rows)
        average_age = data_average("age", rows)
        average_salary = data_average("salary", rows)
        cities = city_counter(rows)

        print(f"Total rows: {rows_length}")
        print(f"Average age: {average_age}")
        print(f"Average salary: {average_salary}")
        print(f"Cities: {cities}")
        print(
            f"Highest paid: {dict_highest_paid['name']} ({dict_highest_paid['salary']})"
        )

        data = {
            "total_rows": rows_length,
            "average_age": average_age,
            "average_salary": average_salary,
            "city_distribution": cities,
            "highest_paid": dict_highest_paid,
        }

        with open("report.json", "w") as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()
