from sklearn import datasets
iris = datasets.load_iris()

from sklearn.model_selection import train_test_split

X = iris['data']
y = iris['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=4)

from kNN import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=6) # k = 6
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print(y_pred)

from sklearn import metrics
scores = metrics.accuracy_score(y_test, y_pred)
print(scores)
