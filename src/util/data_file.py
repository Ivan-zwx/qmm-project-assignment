from src.util.data_dir import get_data_dir


def get_data_file():
    data_dir = get_data_dir()
    data_file = str(data_dir) + 'crabs.csv'
    return data_file
