
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

iris = load_iris()
#print(iris)
print(iris.feature_names)
print(iris.target_names)
X,y=iris.data,iris.target
print(X[:10],y[:10])
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=42)
nb=GaussianNB()
nb.fit(X_train, y_train)
y_pred = nb.predict(X_test)
print("accuracy_score:", accuracy_score(y_test, y_pred))
