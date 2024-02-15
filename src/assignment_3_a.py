import matplotlib.pyplot as plt
import numpy as np

from src.read_data import read_csv_data
from src.util.plot_dir import get_plot_dir


def calculate_descriptive_statistics(crab_data):
    mean = crab_data['FL'].mean()
    min_val = crab_data['FL'].min()
    q1 = crab_data['FL'].quantile(0.25)
    median = crab_data['FL'].median()
    q3 = crab_data['FL'].quantile(0.75)
    max_val = crab_data['FL'].max()
    iqr = q3 - q1
    std_dev = crab_data['FL'].std()
    data_range = max_val - min_val
    return {
        'mean': mean,
        'min': min_val,
        'q1': q1,
        'median': median,
        'q3': q3,
        'max': max_val,
        'IQR': iqr,
        'std_dev': std_dev,
        'range': data_range
    }


def plot_histograms(blue_crabs, orange_crabs):
    bin_width = 2
    bins = np.arange(start=min(blue_crabs['FL'].min(), orange_crabs['FL'].min()),
                     stop=max(blue_crabs['FL'].max(), orange_crabs['FL'].max()) + bin_width,
                     step=bin_width)

    fig, axs = plt.subplots(2, 1, figsize=(10, 12))

    bin_labels = [f"[{int(bins[i])}, {int(bins[i + 1])})" for i in range(len(bins) - 1)]

    axs[0].hist(blue_crabs['FL'], bins=bins, alpha=0.5, label='Blue Crabs', color='blue')
    axs[0].set_title('Histogram of Frontal Lobe Sizes for Blue Crabs')
    axs[0].set_ylabel('Frequency')
    axs[0].legend()
    axs[0].set_xlabel('Frontal Lobe Size (mm) Interval')
    axs[0].set_xticks(bins[:-1] + bin_width / 2)
    axs[0].set_xticklabels(bin_labels)

    axs[1].hist(orange_crabs['FL'], bins=bins, alpha=0.5, label='Orange Crabs', color='orange')
    axs[1].set_title('Histogram of Frontal Lobe Sizes for Orange Crabs')
    axs[1].set_ylabel('Frequency')
    axs[1].legend()
    axs[1].set_xlabel('Frontal Lobe Size (mm) Interval')
    axs[1].set_xticks(bins[:-1] + bin_width / 2)
    axs[1].set_xticklabels(bin_labels)

    plt.tight_layout()
    plt.savefig(get_plot_dir() + 'histogram.png', format='png', dpi=600)
    plt.show()


def plot_box_plots(blue_crabs, orange_crabs):
    plt.figure(figsize=(8, 6))
    plt.boxplot([blue_crabs['FL'], orange_crabs['FL']], labels=['Blue Crabs', 'Orange Crabs'])
    plt.title('Box Plot of Frontal Lobe Sizes')
    plt.ylabel('Frontal Lobe Size (mm)')
    plt.savefig(get_plot_dir() + 'boxplot.png', format='png', dpi=600)
    plt.show()


def perform_assignment_3_a():
    df = read_csv_data()
    # code could be refactored to specify ['FL'] here
    blue_crabs = df[df['color'] == 'B']
    orange_crabs = df[df['color'] == 'O']

    # ********** DESCRIPTIVE STATISTICS REPORTING CHECKED **********

    blue_stats = calculate_descriptive_statistics(blue_crabs)
    orange_stats = calculate_descriptive_statistics(orange_crabs)

    print("Descriptive Statistics for Blue Crabs:", blue_stats)
    print("Descriptive Statistics for Orange Crabs:", orange_stats)

    plot_histograms(blue_crabs, orange_crabs)
    plot_box_plots(blue_crabs, orange_crabs)
