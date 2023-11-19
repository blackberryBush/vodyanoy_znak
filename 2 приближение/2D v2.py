import sys

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr, kendalltau
from sklearn.linear_model import LinearRegression


def read_excel_data(file_path):
    return pd.read_excel(file_path, header=0, index_col=0)


def compute_correlations(x, y):
    pearson_corr, _ = pearsonr(x, y)
    spearman_corr, _ = spearmanr(x, y)
    kendall_corr, _ = kendalltau(x, y)
    covariance = np.cov(x, y)[0, 1]

    x_reshaped = x.reshape(-1, 1)
    model = LinearRegression().fit(x_reshaped, y)
    r_squared = model.score(x_reshaped, y)

    return pearson_corr, spearman_corr, kendall_corr, covariance, r_squared


def plot_correlations(correlation_methods, correlation_values):
    plt.figure(figsize=(10, 5))
    sns.barplot(x=correlation_methods, y=correlation_values)
    plt.title('Взаимная корреляция')
    plt.ylabel('Значение корреляции')
    plt.ylim(-1, 1)
    plt.savefig('2dd.png')


def main():
    arg1 = sys.argv[1]

    # Чтение данных из Excel
    df = read_excel_data('3.xlsx')
    x = df.loc[arg1].values
    df = read_excel_data('4.xlsx')
    y = df.loc[arg1].values
    if np.all(x == 0) or np.all(x == 1) or np.all(y == 0) or np.all(y == 1):
        print("All values are 0 or 1.")
        return

    min_length = min(len(x), len(y))
    x = x[:min_length]
    y = y[:min_length]
    print(x)
    print(y)

    # Вычисление корреляций
    correlations = compute_correlations(x, y)

    # Отрисовка
    correlation_methods = ['Pearson', 'Spearman', 'Kendall', 'covariance', 'R^2']
    plot_correlations(correlation_methods, correlations)


if __name__ == "__main__":
    main()
