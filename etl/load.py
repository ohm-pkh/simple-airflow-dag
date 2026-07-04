import pandas as pd


def load():
    df = pd.read_csv("/opt/airflow/data/transformed.csv")

    print(df)