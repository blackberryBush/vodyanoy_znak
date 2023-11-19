import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_data(file_path):
    data = pd.read_excel(file_path, header=0, index_col=0)
    return data


def plot_autocorrelation(autocorr, file_name):
    # Отрисовка автокорреляционной функции
    plt.figure(figsize=(10, 5))
    plt.stem(autocorr)
    plt.title('Одномерная автокорреляционная функция')
    plt.xlabel('Лаг')
    plt.ylabel('Значение автокорреляции')
    plt.grid(True)
    plt.savefig(f'{file_name}.png')


def calculate_autocorrelation(data):
    # Check if all values is 0
    if np.all(data == 0):
        print("All values are 0")
        return f'{0}\n{0}\n{0}'
    # Вычисление автокорреляционной функции
    autocorr = np.correlate(data, data, mode='full') / np.max(np.correlate(data, data, mode='full'))
    return autocorr


def check_constant_series(client_data):
    if np.all(client_data == 0) or np.all(client_data == 1):
        print("All values are 0 or 1.")
        return False
    return True

def process_file(arg1, path):
    df = load_data(path)
    client_data = df.loc[arg1].values
    if not check_constant_series(client_data):
        print("The series is not constant.")
        return
    autocorrelation_result = calculate_autocorrelation(client_data)
    plot_autocorrelation(autocorrelation_result, f'afc_{arg1}.png')

if __name__ == '__main__':
    arg1 = sys.argv[1]

    path1 = '3.xlsx'
    process_file(arg1, path1)

    path2 = '4.xlsx'
    process_file(arg1, path2)
