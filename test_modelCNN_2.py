#pelatihan model_mnist  ANN dari data  mnist yang sudah dipelajari untuk mencari tingkat kegagalan
import numpy as np
from keras.datasets import mnist
from keras.models import load_model
import matplotlib.pyplot as plt
import keras

(xtrain, ytrain), (xtest, ytest) = mnist.load_data()
rows, cols = 28, 28

xtest = xtest.reshape(xtest.shape[0], rows, cols, 1)
xtest = xtest / 255 #NORMALISASI
ytest =keras.utils.to_categorical(ytest, 10)

model = load_model("model_mnist.h5")
                                  
score =model.evaluate (xtest, ytest)

print("tes mse gagal (loss) : ", score [0])
print("tes akurasi: ", score [1])                                 


          
          

