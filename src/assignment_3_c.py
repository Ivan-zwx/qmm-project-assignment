from scipy.stats import t, chi2
import numpy as np

from src.read_data import read_csv_data


def compute_confidence_interval_mean(sample):
    n = len(sample)
    mean = np.mean(sample)
    std = np.std(sample, ddof=1)
    se = std / np.sqrt(n)

    confidence_level = 0.95
    alpha = 1 - confidence_level
    t_critical = t.ppf(1 - alpha / 2, n - 1)

    # always symmetrical
    margin_of_error = t_critical * se
    ci_lower = mean - margin_of_error
    ci_upper = mean + margin_of_error

    return mean, margin_of_error


def compute_confidence_interval_std(sample):
    n = len(sample)
    variance = np.var(sample, ddof=1)
    confidence_level = 0.95
    alpha = 1 - confidence_level
    chi2_lower = chi2.ppf(alpha / 2, n - 1)
    chi2_upper = chi2.ppf(1 - alpha / 2, n - 1)

    # not always symmetrical
    ci_lower = np.sqrt((n - 1) * variance / chi2_upper)
    ci_upper = np.sqrt((n - 1) * variance / chi2_lower)

    std = np.sqrt(variance)

    return std, ci_lower, ci_upper


def perform_assignment_3_c():
    df = read_csv_data()
    blue_crabs = df[df['color'] == 'B']['FL'].values
    orange_crabs = df[df['color'] == 'O']['FL'].values

    # ********** CONFIDENCE INTERVAL REPORTING CHECKED **********

    # mean, margin of error (symmetrical)
    mean_blue, moe_mean_blue = compute_confidence_interval_mean(blue_crabs)
    mean_orange, moe_mean_orange = compute_confidence_interval_mean(orange_crabs)

    # standard deviation, lower, upper (asymmetrical)
    std_blue, ci_lower_std_blue, ci_upper_std_blue = compute_confidence_interval_std(blue_crabs)
    std_orange, ci_lower_std_orange, ci_upper_std_orange = compute_confidence_interval_std(orange_crabs)

    print(f"Mean frontal lobe size of blue crabs: {mean_blue:.2f} (±{moe_mean_blue:.2f})")
    print(f"Mean frontal lobe size of orange crabs: {mean_orange:.2f} (±{moe_mean_orange:.2f})")

    print(f"Standard deviation of frontal lobe size of blue crabs: {std_blue:.2f} ({ci_lower_std_blue:.2f}, {ci_upper_std_blue:.2f})")
    print(f"Standard deviation of frontal lobe size of orange crabs: {std_orange:.2f} ({ci_lower_std_orange:.2f}, {ci_upper_std_orange:.2f})")
