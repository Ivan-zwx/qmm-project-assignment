from scipy.stats import t
import numpy as np

from src.read_data import read_csv_data


def compute_confidence_interval_for_difference_in_means(sample1, sample2):
    mean1, mean2 = np.mean(sample1), np.mean(sample2)
    var1, var2 = np.var(sample1, ddof=1), np.var(sample2, ddof=1)
    n1, n2 = len(sample1), len(sample2)

    delta = mean1 - mean2
    SE_delta = np.sqrt(var1 / n1 + var2 / n2)

    # degrees of freedom using Welch's approximation
    df = ((var1 / n1 + var2 / n2) ** 2) / (((var1 / n1) ** 2) / (n1 - 1) + ((var2 / n2) ** 2) / (n2 - 1))

    # critical value from t-distribution
    alpha = 0.05
    t_critical = t.ppf(1 - alpha / 2, df)

    # always symmetrical
    E = t_critical * SE_delta
    ci_lower = delta - E
    ci_upper = delta + E

    return delta, E, ci_lower, ci_upper, df


def perform_assignment_3_f():
    df = read_csv_data()
    blue_crabs = df[df['color'] == 'B']['FL'].values
    orange_crabs = df[df['color'] == 'O']['FL'].values

    # ********** CONFIDENCE INTERVAL REPORTING CHECKED **********

    delta, E, ci_lower, ci_upper, df = compute_confidence_interval_for_difference_in_means(blue_crabs, orange_crabs)

    # delta, margin of error (symmetrical)
    print(f"Difference in Mean Frontal Lobe Size: {delta:.3f} (±{E:.3f})")
