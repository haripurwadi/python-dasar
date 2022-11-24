#menghitung y = akar 2x^2 + 1 dari -20 sd 20 dengan kenaikan 0.25 step dengan 2 hidden layer, layer 1 =8 neuron  dan layer 2 =4 neuron
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense #densitas (jumlah layer)
from keras.optimizers import SGD

training_data = np.arange(-20, 20, 0.25)
target_data = np.sqrt((2*training_data**2) + 1)

model = Sequential()
model.add(Dense(8, input_dim=1, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='linear'))
sgd = SGD(lr=0.001) #stochastic gradien decent dengan learning rate 0,001
model.compile(loss='mean_squared_error',
              optimizer=sgd)
              
model.fit(training_data, target_data, epochs=3000, verbose=2)
model.save("model01.h5") #menyimpan model

print(model.predict(np.array([26])))
