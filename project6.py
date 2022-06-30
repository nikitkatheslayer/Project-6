import scipy.stats as sps
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#1 проверить, что стандартизация не меняет распределений
print('{:^72s}'.format("Задание 1"))
data = sps.norm.rvs(size=500)  # выборка размера 500
grid = np.linspace(-3, 3, 1000)  # сетка для построения графика
print(data)
#построение гистограммы
plt.figure(figsize=(16, 7))
plt.hist(data, bins=30, density=True, 
         alpha=0.6, label='Гистограмма') 
plt.plot(grid, sps.norm.pdf(grid), color='red', 
         lw=5, label='Плотность') 
plt.title(r'Данные нормального распределения(Зад. 1)', fontsize=20)
plt.legend(fontsize=14, loc=1)
plt.grid(ls=':')
plt.show()
#стандартизация данных
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data.reshape(-1,1))
#гистограмма стандартизированных данных
plt.figure(figsize=(16, 7))
plt.hist(scaled_data, bins=30, density=True, 
         alpha=0.6, label='Гистограмма') 
plt.plot(grid, sps.norm.pdf(grid), color='red', 
         lw=5, label='Плотность') 
plt.title(r'Стандартизированные данные(Зад. 1)', fontsize=20)
plt.legend(fontsize=14, loc=1)
plt.grid(ls=':')
plt.show()

#3 Доказательство центральной тредельной теоремы
print('{:^72s}'.format("Задание 3"))
from sklearn.utils import shuffle
df = shuffle(data)
df1 = df[0:100]
df2 = df[0:200]
df3 = df[0:300]
df4 = df[0:400]
df5 = df[0:500]

frame = pd.DataFrame({' ': ['0-100', '0-200', '0-300', '0-400', '0-500'], 'Среднее значение': [df1.mean(), df2.mean(), df3.mean(), df4.mean(), df5.mean()], 'Стандартное отклонение': [df1.std(ddof=0), df2.std(ddof=0), df3.std(ddof=0), df4.std(ddof=0), df5.std(ddof=0)]})
print(frame)

#гистограмма 0-100
plt.figure(figsize=(16, 7))
plt.hist(df1, bins=30, density=True, 
         alpha=0.6, label='Гистограмма') 
plt.plot(grid, sps.norm.pdf(grid), color='red', 
         lw=5, label='Плотность') 
plt.title(r'0-100(Зад. 3)', fontsize=20)
plt.legend(fontsize=14, loc=1)
plt.grid(ls=':')
plt.show()

#гистограмма 0-200
plt.figure(figsize=(16, 7))
plt.hist(df2, bins=30, density=True, 
         alpha=0.6, label='Гистограмма') 
plt.plot(grid, sps.norm.pdf(grid), color='red', 
         lw=5, label='Плотность') 
plt.title(r'0-200(Зад. 3)', fontsize=20)
plt.legend(fontsize=14, loc=1)
plt.grid(ls=':')
plt.show()

#гистограмма 0-300
plt.figure(figsize=(16, 7))
plt.hist(df3, bins=30, density=True, 
         alpha=0.6, label='Гистограмма') 
plt.plot(grid, sps.norm.pdf(grid), color='red', 
         lw=5, label='Плотность') 
plt.title(r'0-300(Зад. 3)', fontsize=20)
plt.legend(fontsize=14, loc=1)
plt.grid(ls=':')
plt.show()

#гистограмма 0-400
plt.figure(figsize=(16, 7))
plt.hist(df4, bins=30, density=True, 
         alpha=0.6, label='Гистограмма') 
plt.plot(grid, sps.norm.pdf(grid), color='red', 
         lw=5, label='Плотность') 
plt.title(r'0-400(Зад. 3)', fontsize=20)
plt.legend(fontsize=14, loc=1)
plt.grid(ls=':')
plt.show()

#гистограмма 0-500
plt.figure(figsize=(16, 7))
plt.hist(df5, bins=30, density=True, 
         alpha=0.6, label='Гистограмма') 
plt.plot(grid, sps.norm.pdf(grid), color='red', 
         lw=5, label='Плотность') 
plt.title(r'0-500(Зад. 3)', fontsize=20)
plt.legend(fontsize=14, loc=1)
plt.grid(ls=':')
plt.show()

#2 программа
#Ввод данных
print('{:^72s}'.format("Задание 2"))
print('{:^72s}'.format("Введите m(среднее)"))
m = input()
print("Вы ввели:" + m)
print('{:^72s}'.format("Введите sd(стандартное отклонение)"))
sd = input()
print("Вы ввели:" + sd)
print('{:^72s}'.format("Введите число k"))
k = input()
print("Вы ввели:" + k)

if k > m:
    xc = ((float(k) - float(m)) / float(sd))
    print("Результат:" + str(xc))
    print("Для ответа в виде процентов, смотри: <Таблицу нормального распределения>")
    print("Пример: z=0.2, тогда по данным из табл. ответ в процентах = 5.7%")
else:
    print("Результат: Введите другие данные")

