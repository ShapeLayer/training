'''
김찬수 교수님 문제풀이
'''

import numpy as np

def NeighborsClassifier(n_neighbors, X_train, y_train, X_test):
    y_test = np.zeros(len(X_test))
    for i in range(len(X_test)):
        dist = np.linalg.norm(X_train - X_test[i], axis=1)
        idx = np.argsort(dist)[:n_neighbors]
        label_list = y_train[idx].tolist()
        y_test[i] = max(label_list, key=label_list.count)
    return y_test
