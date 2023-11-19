from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from category_encoders import TargetEncoder


# Загрузка данных в DataFrame (data - ваши данные)
data = pd.read_csv("ИТОГ.csv",sep=';', encoding='cp1251')
data=data.drop(data.columns[0],axis=1)
# Разделение на признаки и целевой атрибут
X = data.drop('Причина ухода', axis=1)  # Признаки
y = data['Причина ухода']  # Целевой атрибут

# Инициализация модели случайного леса
model = RandomForestClassifier()

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
for i in X.columns:
    e_x = label_encoder.fit_transform(X[i].astype(str))
    X[i] = e_x
hashing_enc = TargetEncoder(cols=X.columns, smoothing=8, min_samples_leaf=5).fit(X, y)

X = hashing_enc.transform(X.reset_index(drop=True))
X=pd.DataFrame(data=X,columns=X.columns)

TOP3=[]
for i in y.unique():
    labels = []
    for j in y:
        if j==i:
            labels.append(1)
        else:
            labels.append(0)

    # Тренировка модели
    model.fit(X, labels)

    # Оценка важности признаков для каждого кластера
    feature_importance = pd.DataFrame(model.feature_importances_, index=X.columns, columns=['Importance'])
    feature_importance=feature_importance.sort_values('Importance', ascending=False)
    TOP3.append(feature_importance[:3].index.to_list())


DFFF = pd.DataFrame(data=TOP3)
DFFF.to_excel('TOP3.xlsx')
print('!')
