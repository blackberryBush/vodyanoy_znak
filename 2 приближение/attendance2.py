import sys

import pandas as pd
from matplotlib import pyplot as plt


def plot_attendance(row: pd.Series):
    # Convert the index to DatetimeIndex
    row_index = pd.to_datetime(row.index)

    # Convert values to strings
    values_as_strings = row.values.astype(str)

    plt.figure(figsize=(10, 5))
    plt.plot(row_index, values_as_strings, marker='o')
    plt.title(f'РКО {row.name}')
    plt.ylabel(f'Вовлеченность клиента')
    plt.xticks(rotation=30)  # Rotate x-axis labels for better readability
    plt.savefig(f'attendance2.png')


def run_attendance(arg1):
    df = pd.read_excel('4.xlsx', header=0, index_col=0)
    plot_attendance(df.loc[arg1])


if __name__ == '__main__':
    arg1 = sys.argv[1]
    run_attendance(arg1)
