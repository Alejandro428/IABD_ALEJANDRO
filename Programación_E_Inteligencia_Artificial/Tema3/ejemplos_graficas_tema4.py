import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris

iris = load_iris()

print(np.unique(iris.target[0:99]))
print(np.unique(iris.target[0]))

resultados = [
    ['2, 4, 2', 20, 0.5156, 0.5121, 0.27],
    ['2, 6, 2', 30, 0.6234, 0.6102, 0.23],
    ['2, 8, 2', 40, 0.7125, 0.6850, 0.19],
    ['2, 10, 2', 50, 0.7850, 0.7623, 0.17],
    ['2, 12, 2', 60, 0.8253, 0.8011, 0.15]
]

# resultados[:,4] recoge de todos los resultados la fila 4 (en este caso, sería el tiempo

tiempos = np.array(resultados[:,4], dtype=np.float64)

tiempo_min = np.min(tiempos)
index_tiempo_min = np.argmin(tiempos)

red=resultados[index_tiempo_min, 0]
epocas=resultados[index_tiempo_min, 1]

print(tabulate(resultados, headers=['Red', 'Épocas', 'Result 1', 'Result 2', 'Tiempo(s)']))

print(f"Tiempo mínimo:{tiempo_min}")

