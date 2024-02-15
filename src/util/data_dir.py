import os

from src.util.project_dir import get_project_dir


def get_data_dir():
    project_dir = get_project_dir()
    data_dir = str(project_dir) + 'data' + os.path.sep
    return data_dir
