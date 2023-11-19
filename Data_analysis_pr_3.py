import numpy as np
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.cluster import dbscan
from category_encoders import TargetEncoder
from sklearn.cluster import DBSCAN

def trend_direction(time_series):
    n = len(time_series)
    x = np.arange(n)
    # y = [float(x) for   x in time_series]
    y = np.array(time_series)
    # Вычисление коэффициентов линейной регрессии (тренда)
    A = np.vstack([x, np.ones(n)]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    # Определение направления тренда
    if m > 0:
        direction = 1
    elif m < 0:
        direction = -1
    else:
        direction = 0

    return direction, m


def func_return_prognosis(df_dohod_eq_transpose):
    list_nega_p=[]
    list_trend=[]
    for i in df_dohod_eq_transpose:
        trend, tr = trend_direction(df_dohod_eq_transpose[i].values)
        list_trend.append(tr)
        if (trend==-1):
            list_nega_p.append(i)

    return list_nega_p, list_trend



DF_eq_RSO = pd.read_csv('1_эквайринг_РСО.csv',sep=';')
DF_eq_eq = pd.read_csv('1_эквайринг_эквайринг.csv',sep=';')
DF_dohod_full = pd.read_csv('3_эквайринг_общий_доход.csv',sep=';')
DF_dohod_eq = pd.read_csv('3_эквайринг_доход_эквайринг.csv',sep=';')

DF_information = pd.read_csv('2_Профили клиентов.csv',sep=';', encoding='cp1251')
DF_information = DF_information.sort_values('client', ascending=True)
DF_information.index=DF_information['client']
DF_information = DF_information.drop('client',axis=1)



DF_eq_RSO=DF_eq_RSO.sort_values('client', ascending=True)
DF_eq_RSO.index=DF_eq_RSO['client']
DF_eq_RSO_indexes=DF_eq_RSO['client']


DF_eq_eq=DF_eq_eq.sort_values('client', ascending=True)
DF_eq_eq.index=DF_eq_eq['client']
DF_eq_eq_indexes=DF_eq_eq['client']

DF_dohod_full=DF_dohod_full.sort_values('client', ascending=True)
DF_dohod_full.index=DF_dohod_full['client']
DF_dohod_full_indexes=DF_dohod_full['client']

DF_dohod_eq=DF_dohod_eq.sort_values('client', ascending=True)
DF_dohod_eq.index=DF_dohod_eq['client']
DF_dohod_eq_indexes=DF_dohod_eq['client']


DF_eq_RSO=DF_eq_RSO.drop('client',axis=1)
DF_dohod_full=DF_dohod_full.drop('client',axis=1)
DF_eq_eq =DF_eq_eq.drop('client',axis=1)
DF_dohod_eq=DF_dohod_eq.drop('client',axis=1)


for i in DF_dohod_eq:
    new_list=[]
    for j in DF_dohod_eq[i]:
        new_list.append(j.split(',')[0])
    DF_dohod_eq[i]=new_list
    DF_dohod_eq[i] = DF_dohod_eq[i].astype(float)


'фильтруем все записи в датафреймах с клиентами, которые ушли'

'транспонируем для получения доступа к каждому клиенту'
print('этап транспонирования')
N=len(DF_eq_eq)
N=1000

DF_eq_eq_transpose = DF_eq_eq[:N].T
DF_eq_RSO_transpose = DF_eq_RSO[:N].T
DF_dohod_full_transpose = DF_dohod_full[:N].T
DF_dohod_eq_transpose = DF_dohod_eq[:N].T
DF_information_transpose = DF_information[:N].T

"заводим темп датафреймы"
DF_eq_eq_transpose_temp = DF_eq_eq_transpose
DF_eq_RSO_transpose_temp = DF_eq_RSO_transpose
DF_dohod_full_transpose_temp =  DF_dohod_full_transpose
DF_dohod_eq_transpose_temp =  DF_dohod_eq_transpose
DF_information_transpose_temp = DF_information_transpose

'фильтруем все записи в датафреймах с клиентами, которые признаны прогнозными'
names_of_clients_negative_prognosis, list_trend = func_return_prognosis(DF_dohod_full_transpose)


print('этап фильтрации по ушедшим клиентам эквайринга')
list_trend_outsiders=[i for i in range(N)]

cou=0
for i in DF_eq_RSO_indexes[:N]:
    'Если у клиента все хорошо - он еще клиент в последний месяц и при этом у него нет негативного прогноза - исключаем его'
    if (DF_eq_eq_transpose[i]['30.09.2023'])!=0 and names_of_clients_negative_prognosis.count(i)==0:
        DF_eq_eq_transpose_temp = DF_eq_eq_transpose_temp.drop(i,axis=1)
        DF_eq_RSO_transpose_temp = DF_eq_RSO_transpose_temp.drop(i,axis=1)
        DF_dohod_full_transpose_temp = DF_dohod_full_transpose_temp.drop(i,axis=1)
        DF_dohod_eq_transpose_temp = DF_dohod_eq_transpose_temp.drop(i,axis=1)
        DF_information_transpose_temp = DF_information_transpose_temp.drop(i,axis=1)
        list_trend_outsiders.remove(cou)
    cou += 1

for i in range(len(list_trend_outsiders)):
    list_trend_outsiders[i]=list_trend[i]

print('кластеризация')

# DF_eq_eq_transpose_temp = DF_eq_eq_transpose_temp.T
# DF_eq_RSO_transpose_temp = DF_eq_RSO_transpose_temp.T
# DF_dohod_full_transpose_temp = DF_dohod_full_transpose_temp.T
# DF_dohod_eq_transpose_temp = DF_dohod_eq_transpose_temp.T
DF_information_transpose_temp=DF_information_transpose_temp.T
DF_information_transpose_temp2 = DF_information_transpose_temp.values
# Кодирование информации в DF_information_transpose_temp в числа
# Получим все категориальные переменные и перекодируем их в числа

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
for i in DF_information_transpose_temp.columns:
    e_x = label_encoder.fit_transform(DF_information_transpose_temp[i].astype(str))
    DF_information_transpose_temp[i] = e_x
hashing_enc = TargetEncoder(cols=DF_information_transpose_temp.columns, smoothing=8, min_samples_leaf=5).fit(DF_information_transpose_temp, list_trend_outsiders)

DF_information_transpose_temp = hashing_enc.transform(DF_information_transpose_temp.reset_index(drop=True))
DF_information_transpose_temp2=pd.DataFrame(data=DF_information_transpose_temp2,columns=DF_information_transpose_temp.columns)


# Масштабирование данных
scaler = StandardScaler()
scaled_data_DF_eq_eq_transpose_temp = scaler.fit_transform(DF_eq_eq_transpose_temp)
scaled_data_DF_eq_RSO_transpose_temp = scaler.fit_transform(DF_eq_RSO_transpose_temp)
scaled_data_DF_dohod_full_transpose_temp = scaler.fit_transform(DF_dohod_full_transpose_temp)
scaled_data_DF_dohod_eq_transpose_temp = scaler.fit_transform(DF_dohod_eq_transpose_temp)
scaled_data_information_transpose_temp = scaler.fit_transform(DF_information_transpose_temp)

scaled_data_DF_eq_eq_transpose_temp = scaled_data_DF_eq_eq_transpose_temp.T
scaled_data_DF_eq_RSO_transpose_temp = scaled_data_DF_eq_RSO_transpose_temp.T
scaled_data_DF_dohod_full_transpose_temp = scaled_data_DF_dohod_full_transpose_temp.T
scaled_data_DF_dohod_eq_transpose_temp = scaled_data_DF_dohod_eq_transpose_temp.T
scaled_data_information_transpose_temp=scaled_data_information_transpose_temp.T


tempdf11 = pd.DataFrame(data=scaled_data_information_transpose_temp)
tempdf21 = pd.DataFrame(data=scaled_data_DF_dohod_full_transpose_temp)

tempdf1 = pd.DataFrame(data=DF_information_transpose_temp.values.T)
tempdf2 = pd.DataFrame(data=DF_dohod_full_transpose_temp.values.T)


df_merged1 = pd.concat([tempdf11, tempdf21.T], ignore_index=True, sort=False).T
df_merged = pd.concat([tempdf1, tempdf2.T], ignore_index=True, sort=False).T


# # Определение оптимального количества кластеров методом локтя
# inertia = []
# silhouette_scores = []
# max_cl = 30
# for n_clusters in range(2, max_cl ):  # Попробуем разное количество кластеров
#     kmeans = KMeans(n_clusters=n_clusters, random_state=42)
#     kmeans.fit(df_merged)
#     inertia.append(kmeans.inertia_)
#     silhouette_scores.append(silhouette_score(df_merged, kmeans.labels_))
#
# # Визуализация метода локтя
# plt.figure(figsize=(10, 5))
#
# plt.subplot(1, 2, 1)
# plt.plot(range(2, max_cl ), inertia, marker='o')
# plt.xlabel('Кол-во кластеров')
# plt.ylabel('Сумма квадратов расстояний всех точек данных до их ближайших центров кластеров')
# plt.title('Определение опт. кол-ва кластеров методом локтя')
#
# plt.subplot(1, 2, 2)
# plt.plot(range(2, max_cl ), silhouette_scores, marker='o')
# plt.xlabel('Кол-во кластеров')
# plt.ylabel('Коэффициент силлуэта')
# plt.title('Определение опт. кол-ва кластеров методом коэфф. силлуэта')
#
# plt.tight_layout()
# plt.savefig('1.png')

# Выбор оптимального количества кластеров (например, по методу локтя)
optimal_clusters = 21  # Например, выбираем оптимальное количество кластеров


# hdb = DBSCAN( eps=50, min_samples=optimal_clusters, metric='euclidean')
# hdb.fit(df_merged)
# sum(hdb.labels_)



# Применение PCA для уменьшения размерности данных
pca = PCA(n_components=2)  # Указываем количество компонентов
pca_data = pca.fit_transform(df_merged1)

# Кластеризация данных с оптимальным количеством кластеров
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
kmeans_graph = KMeans(n_clusters=optimal_clusters, random_state=42)
kmeans.fit(df_merged)
kmeans_graph.fit(pca_data)

# Визуализация результатов кластеризации
plt.figure(figsize=(12, 8))
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=kmeans_graph.labels_, cmap='viridis', alpha=0.5)
plt.scatter(kmeans_graph.cluster_centers_[:, 0], kmeans_graph.cluster_centers_[:, 1], marker='o', s=20, c='red', label='Centroids')

plt.title('Кластеризованные данные (двухмерное распределение)')
plt.xlabel('PA_1')
plt.ylabel('PA_2')
plt.legend()
plt.colorbar()
plt.savefig('2.png')


# DF_information_transpose_temp2 = DF_information_transpose_temp2.T
DF_information_transpose_temp2['Линия тренда дохода'] = list_trend_outsiders
DF_information_transpose_temp2['Причина ухода']=kmeans.labels_

DF_information_transpose_temp2.to_excel('Итоговый отток клиентов информация к описанию.xlsx')

print('!')