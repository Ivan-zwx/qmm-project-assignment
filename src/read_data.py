import pandas as pd

from src.util.data_file import get_data_file


def read_csv_data():
    return pd.read_csv(get_data_file(), delimiter=';')
