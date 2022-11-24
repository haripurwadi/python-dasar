#machine learning knn random tes dan uji

from sklearn import datasets  # import dataset bunga iris 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split # data uji dan data tes di acak

iris = datasets.load_iris() #150 data set bunga iris
X = iris.data # p dan L kelopak, P dan L putik
Y = iris.target # sepesies / jenis bungan iris

xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size=0.2, random_state=7) #random tes dan uji

#tarining KNN
knn = KNeighborsClassifier()
knn.fit(xtrain,ytrain)  # membangun model
score = knn.score(xtest, ytest)
print ("KNN:", score)
