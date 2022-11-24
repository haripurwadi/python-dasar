#pelatihan model_mnist  ANN dari data  mnist yang sudah dipelajari untuk memprediksi  sebuah angka
#angka uji  dari 0 s/d 10000 data
import numpy as np
from keras.datasets import mnist
from keras.models import load_model
import matplotlib.pyplot as plt

(xtrain, ytrain), (xtest, ytest) = mnist.load_data()
rows, cols = 28, 28

plt.show(plt.imshow(xtest[999999])) #xtest bisa diganti 0 sd 9999
imgtest = xtest[0].reshape(1, rows, cols, 1)
imgtest = imgtest / 255

model = load_model("model_mnist.h5")
out =  model.predict(imgtest).round()
print(np.argmax(out))


          
          
