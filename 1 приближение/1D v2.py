import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller


def load_data(file_path):
    data = pd.read_excel(file_path, header=0, index_col=0)
    return data


def calculate_statistics(data):
    # Математическое ожидание (среднее значение)
    mean_value = np.mean(data)

    # Дисперсия
    variance_value = np.var(data)

    # Среднеквадратическое отклонение
    std_deviation_value = np.sqrt(variance_value)

    result = (
            f"{mean_value}\n" +  # Математическое ожидание (среднее значение)
            f"{variance_value}\n" +  # Дисперсия
            f"{std_deviation_value}")  # Среднеквадратическое отклонение
    return result


def calculate_autocorrelation(data):
    # Вычисление автокорреляционной функции
    autocorr = np.correlate(data, data, mode='full') / np.max(np.correlate(data, data, mode='full'))
    return autocorr


def perform_adf_test(data):
    # Check if all values is 0
    if np.all(data == 0) or np.all(data == 1):
        print("All values are 0 or 1. Cannot perform ADF test.")
        return f'{-1}\n{-1}\n{-1}'

    # Тест на стационарность (ADF тест)
    results = adfuller(data)
    result = f'{results[0]}\n{results[1]}'  # ADF статистика, p-value
    for key, value in results[4].items():  # Critical Values
        result += f'\n{key}: {value}'
    return result


def write_results_to_file(file_path, values):
    with open(file_path, 'w+') as file:
        file.write(f"{values}\n")


def process_file(file_path, arg1):
    df = load_data(file_path)
    client_data = df.loc[arg1].values

    statistics = calculate_statistics(client_data)
    adf_test_result = perform_adf_test(client_data)
    print(statistics)
    print(adf_test_result)
    write_results_to_file(f'results_{arg1}.txt', statistics + '\n' + adf_test_result)


if __name__ == "__main__":
    # arg1 = sys.argv[1]
    arg1 = 'client_5138'

    process_file('1.xlsx', arg1)
    process_file('2.xlsx', arg1)
