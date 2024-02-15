from scipy.stats import f
import numpy as np

from src.read_data import read_csv_data


def compute_f_statistic_and_p_value(sample1, sample2):
    var1, var2 = np.var(sample1, ddof=1), np.var(sample2, ddof=1)
    F = max(var1, var2) / min(var1, var2)
    n1, n2 = len(sample1), len(sample2)

    df1, df2 = n1 - 1, n2 - 1

    p_value = 1 - f.cdf(F, df1, df2)

    return F, df1, df2, p_value


def perform_assignment_3_d():
    df = read_csv_data()
    blue_crabs = df[df['color'] == 'B']['FL'].values
    orange_crabs = df[df['color'] == 'O']['FL'].values

    # ********** HYPOTHESIS TEST REPORTING CHECKED **********

    # f statistic, degrees of freedom for sample 1, degrees of freedom for sample 2, p value
    F_statistic, df1, df2, p_value = compute_f_statistic_and_p_value(blue_crabs, orange_crabs)

    print(f"Testing for equality of variances between blue and orange crabs using the F-test:")
    print(f"F-statistic: {F_statistic:.4f}, Degrees of freedom: {df1}, {df2}, p-value: {p_value:.4f}")

    if p_value < 0.05:
        print("Conclusion: There is a significant difference in variances between the groups (reject the null hypothesis).")
    else:
        print("Conclusion: There is no significant difference in variances between the groups (fail to reject the null hypothesis).")
