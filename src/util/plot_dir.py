import os

from src.util.project_dir import get_project_dir


def get_plot_dir():
    project_dir = get_project_dir()
    plot_dir = str(project_dir) + 'plot' + os.path.sep
    return plot_dir
