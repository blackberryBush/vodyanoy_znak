import pandas as pd
from matplotlib import pyplot as plt


def plot_pr(df, index):
    # Создаем новый DataFrame для новых клиентов в ноябре
    new_clients_november = df[(df['2022-10-31'] == 0) & (df['2022-11-30'] == 1)]

    cut_off_date = '2022-11-30'
    df = df.loc[:, cut_off_date:]

    rates = dict()

    # Проходим по всем колонкам в df
    for column in df.columns:
        # Подсчитываем значения для каждой даты
        value = new_clients_november.index.isin(df[df[column] == 1].index).sum()

        # Добавляем значение в DataFrame
        rates[column] = value / len(new_clients_november) * 100

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(rates.keys(), rates.values(), marker='o', linestyle='-', color='b')

    plt.title('PR')
    plt.ylim(0, 105)
    plt.savefig(f'pr{index}.png')


def run_pr(index):
    df = pd.read_excel(f'{index}.xlsx', header=0, index_col=0)
    plot_pr(df, index)


if __name__ == '__main__':
    run_pr(1)
    run_pr(2)
