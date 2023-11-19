import pandas as pd
from matplotlib import pyplot as plt


def calculate_growth_rate(c1, c2):
    return ((c2 - c1) / c1) * 100


def plot_cr(df, index):
    growth_rates = pd.DataFrame()

    clients_by_month = df.sum(axis=0)

    for i in range(1, len(clients_by_month)):
        c1 = clients_by_month.iloc[i - 1]
        c2 = clients_by_month.iloc[i]
        growth_rates.loc[clients_by_month.index[i], 'Rate'] = calculate_growth_rate(c1, c2)

    plot_graph(growth_rates, 'CR', f'cr{index}.png')


def plot_graph(df, title, filename, ylim=None):
    plt.clf()
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Rate'], marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel('Период')
    plt.ylabel('%')
    plt.ylim(ylim)
    plt.grid(True)
    plt.savefig(filename)


def run_cr(index):
    df = pd.read_excel(f'{index}.xlsx', header=0, index_col=0)
    plot_cr(df, index)


if __name__ == '__main__':
    run_cr(1)
    run_cr(2)
