import pandas as pd


def extract():
    data = {
        "id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Charlie", "David"],
        "department": ["IT", "HR", "IT", "Finance"],
        "salary": [50000, 40000, 55000, 60000],
    }

    df = pd.DataFrame(data)
    df.to_csv("/opt/airflow/data/raw.csv", index=False)