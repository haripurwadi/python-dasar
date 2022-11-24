#Membuar model ANN menggunakan data dari mnist
#Prograam ini akan menggunakan 90% CPU untuk proses komputasi untuk menemukan sebuah model
#sehingga membutuhkan waktu yang lama tergantung dari prosesornya, disarankan untuk menggunakan GPU
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import keras

(xtrain, ytrain), (xtest, ytest) = mnist.load_data()
rows, cols = 28, 28

xtrain = xtrain.reshape(xtrain.shape[0], rows, cols, 1) # meyusun gambar 28 x 28 menjadi satu baris (1x728)
xtest = xtest.reshape(xtest.shape[0], rows, cols, 1)

ytrain = keras.utils.to_categorical(ytrain, 10)
ytest = keras.utils.to_categorical(ytest, 10)

xtrain = xtrain / 255
xtest = xtest / 255

model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation = 'relu', input_shape = (rows, cols, 1)))
model.add(Conv2D(64, kernel_size=(3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
          
model.add(Dense(64, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(), metrics=["accuracy"])
          
model.fit(xtrain, ytrain, batch_size=128, epochs=12, verbose=1)
model.save("mnist_model.h5")
score = model.evaluate(xtest, ytest)
print ("loss: ", score[0])
print ("Accuracy: ", score[1])
          
          