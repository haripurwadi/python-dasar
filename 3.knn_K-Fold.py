#machine learning KNN k-fold croos-validation

from sklearn import datasets  # import dataset bunya iris 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC 
from sklearn.model_selection import train_test_split # data uji dan data tes di acak
from sklearn import model_selection
import numpy as np

iris = datasets.load_iris() #150 data set bunga iris
X = iris.data # p dan L kelopak, P dan L putik
Y = iris.target # sepesies / jenis bungan iris

#xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size=0.2, random_state=10) #random tes dan uji
scores = []
knn = KNeighborsClassifier()
kfold = model_selection.KFold(n_splits=10, random_state=10)
for train_index, test_index in kfold.split(X):
    xtrain, xtest, ytrain, ytest = X[train_index], X[test_index], Y[train_index], Y[test_index]
    knn.fit(xtrain, ytrain)
    scores.append(knn.score(xtest, ytest))
    
    print("KNN K-Fold: ", np.mean(scores))
                  
    
#tarining KNN

knn.fit(xtrain,ytrain)  # membangun model
score = knn.score(xtest, ytest)
print ("KNN : ", score)

clf = SVC(gamma='auto')
clf.fit(xtrain, ytrain)
score = clf.score(xtest, ytest)
print ("SVC: ", score)


