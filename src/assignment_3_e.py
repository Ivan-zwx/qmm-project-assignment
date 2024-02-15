from scipy.stats import t
import numpy as np

from src.read_data import read_csv_data


# This test makes several assumptions (based on earlier tests):
# The data is normally distributed (checked in b) -> necessary assumption
# The variances are equal (checked in d) -> unnecessary assumption


def welchs_t_test_and_p_value(sample1, sample2):
    mean1, mean2 = np.mean(sample1), np.mean(sample2)
    var1, var2 = np.var(sample1, ddof=1), np.var(sample2, ddof=1)
    n1, n2 = len(sample1), len(sample2)

    # t-statistic
    t_statistic = (mean1 - mean2) / np.sqrt(var1 / n1 + var2 / n2)

    # degrees of freedom
    df = ((var1 / n1 + var2 / n2) ** 2) / (((var1 / n1) ** 2) / (n1 - 1) + ((var2 / n2) ** 2) / (n2 - 1))

    # p-value for the two-tailed test
    p_value = 2 * t.sf(np.abs(t_statistic), df)

    return t_statistic, df, p_value


def perform_assignment_3_e():
    df = read_csv_data()
    blue_crabs = df[df['color'] == 'B']['FL'].values
    orange_crabs = df[df['color'] == 'O']['FL'].values

    # ********** HYPOTHESIS TEST REPORTING CHECKED **********

    t_statistic, df, p_value = welchs_t_test_and_p_value(blue_crabs, orange_crabs)

    print(f"Testing for a difference in means between blue and orange crabs using Welch's t-test:")
    print(f"t-statistic: {t_statistic:.4f}, Degrees of freedom: {df:.2f}, p-value: {p_value:.4f}")

    if p_value < 0.05:
        print("Conclusion: There is a significant difference in means between the groups (reject the null hypothesis).")
    else:
        print("Conclusion: There is no significant difference in means between the groups (fail to reject the null hypothesis).")
