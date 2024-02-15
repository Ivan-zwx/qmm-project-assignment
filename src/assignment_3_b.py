from scipy.stats import shapiro, norm
import matplotlib.pyplot as plt
import numpy as np

from src.read_data import read_csv_data
from src.util.plot_dir import get_plot_dir


def test_normality(sample):
    stat, p_value = shapiro(sample)
    return stat, p_value


def plot_normality_tests(blue_crabs, orange_crabs):
    bin_width = 2
    bins = np.arange(start=min(blue_crabs['FL'].min(), orange_crabs['FL'].min()),
                     stop=max(blue_crabs['FL'].max(), orange_crabs['FL'].max()) + bin_width,
                     step=bin_width)

    fig, axs = plt.subplots(2, 1, figsize=(10, 12))

    mu_blue, std_blue = norm.fit(blue_crabs['FL'])
    mu_orange, std_orange = norm.fit(orange_crabs['FL'])

    x_blue = np.linspace(min(blue_crabs['FL']), max(blue_crabs['FL']), 100)
    y_blue = norm.pdf(x_blue, mu_blue, std_blue)

    x_orange = np.linspace(min(orange_crabs['FL']), max(orange_crabs['FL']), 100)
    y_orange = norm.pdf(x_orange, mu_orange, std_orange)

    bin_labels = [f"[{int(bins[i])}, {int(bins[i + 1])})" for i in range(len(bins) - 1)]

    axs[0].hist(blue_crabs['FL'], bins=bins, alpha=0.5, label='Blue Crabs', color='blue', density=True)
    axs[0].plot(x_blue, y_blue, 'r--', label='Normal Distribution')
    axs[0].set_title('Normality Test of Frontal Lobe Sizes for Blue Crabs')
    axs[0].set_ylabel('Density')
    axs[0].legend()
    axs[0].set_xlabel('Frontal Lobe Size (mm) Interval')
    axs[0].set_xticks(bins[:-1] + bin_width / 2)
    axs[0].set_xticklabels(bin_labels)

    axs[1].hist(orange_crabs['FL'], bins=bins, alpha=0.5, label='Orange Crabs', color='orange', density=True)
    axs[1].plot(x_orange, y_orange, 'r--', label='Normal Distribution')
    axs[1].set_title('Normality Test of Frontal Lobe Sizes for Orange Crabs')
    axs[1].set_ylabel('Density')
    axs[1].legend()
    axs[1].set_xlabel('Frontal Lobe Size (mm) Interval')
    axs[1].set_xticks(bins[:-1] + bin_width / 2)
    axs[1].set_xticklabels(bin_labels)

    plt.tight_layout()
    plt.savefig(get_plot_dir() + 'normality.png', format='png', dpi=600)
    plt.show()


def perform_assignment_3_b():
    df = read_csv_data()
    # code could be refactored to specify ['FL'] here
    blue_crabs = df[df['color'] == 'B']
    orange_crabs = df[df['color'] == 'O']

    # ********** NORMALITY TEST REPORTING CHECKED **********

    stat_blue, p_blue = test_normality(blue_crabs['FL'])
    print(f"Blue Crabs: Shapiro-Wilk Test Stat: {stat_blue:.3f}, p-value: {p_blue:.3f}")
    if p_blue > 0.05:
        print("The frontal lobe sizes of blue crabs appear to be normally distributed (fail to reject the null hypothesis).")
    else:
        print("The frontal lobe sizes of blue crabs do not appear to be normally distributed (reject the null hypothesis).")

    stat_orange, p_orange = test_normality(orange_crabs['FL'])
    print(f"Orange Crabs: Shapiro-Wilk Test Stat: {stat_orange:.3f}, p-value: {p_orange:.3f}")
    if p_orange > 0.05:
        print("The frontal lobe sizes of orange crabs appear to be normally distributed (fail to reject the null hypothesis).")
    else:
        print("The frontal lobe sizes of orange crabs do not appear to be normally distributed (reject the null hypothesis).")

    plot_normality_tests(blue_crabs, orange_crabs)
