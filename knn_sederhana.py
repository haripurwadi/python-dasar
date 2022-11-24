# K-Nearest Neighbours
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

Model = KNeighborsClassifier(n_neighbors=7) #Inisialisasi model Machine Learning yang digunakan.
Model.fit(x_train, y_train) #Proses training hanya 1 baris ini saja.
y_pred = Model.predict(x_test)

print(classification_report(y_test, y_pred))  # Mencetak Summary 
print(confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1))) # Mencetak Conf Matrix
print('accuracy is',accuracy_score(y_pred,y_test)) # Mencetak Accuracy score
