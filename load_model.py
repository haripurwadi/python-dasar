#menghitung y = akar 2x^2 + 1 dari -20 sd 20 dengan kenaikan 0.25 step dengan 2 hidden layer, layer 1 =8 neuron  dan layer 2 =4 neuron
import numpy as np
from keras.models import load_model


model = load_model("model01.h5") #pangil model

print(model.predict(np.array([26]))) #tampilkan hasil prediksi

