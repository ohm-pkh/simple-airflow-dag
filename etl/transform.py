import pandas as pd


def transform():
    df = pd.read_csv("/opt/airflow/data/raw.csv")

    df["department"] = df["department"].str.upper()
    df = df[df["salary"] >= 50000]
    df["bonus"] = df["salary"] * 0.1

    df.to_csv("/opt/airflow/data/transformed.csv", index=False)