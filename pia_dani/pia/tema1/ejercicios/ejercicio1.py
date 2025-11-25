import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
 
iris=load_iris()
 
longitudes_petalos=iris.data[0:99,2]
anchos_petalos=iris.data[0:99,3]
flower_type=iris.target[0:99]
 
x=np.column_stack((longitudes_petalos,anchos_petalos))
y=flower_type
 
 
np.random.seed(5)
tf.random.set_seed(5)
random.seed(5)  
 
model=Sequential()
model.add(Dense(6, activation='relu',input_dim=2))
model.add(Dense(12, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy')
 
 
model.fit(x, y,epochs=100) 
 
 
print(model.predict(np.array([[1.4,0.2]])))
print(model.predict(np.array([[4.4,1.3]])))