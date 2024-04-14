from collections import Counter
import numpy as np

class KNeighborsClassifier:
    def __init__(self, n_neighbors: int=5):
        self.n_neighbors = n_neighbors
        self._X = None
        self._y = None

    @property
    def X(self):
        return self._X
    
    @property
    def y(self):
        return self._y

    def fit(self, X, y):
        if len(y.shape) != 1:
            raise ValueError('y Array must be 1D array.')
        self._X = X
        self._y = y

    def predict(self, x):
        results = []
        for each_row in x:
            calced = self.X - each_row
            y_idx = None
            if len(x.shape) == 2:
                y_idx = self._predict_optimize_2d_array(calced)
            else:
                y_idx = self._predict_dovish(calced)
            y = np.array([*map(lambda each: self.y[each], y_idx)])
            counter = dict(Counter(y))
            results.append(sorted([(counter[key], key) for key in counter], reverse=True)[0][1])
        return np.array(results)

    def _predict_dovish(self, x):
        '''
        `_predict_dovish`는 `predict` 메서드에 의해 호출될 것을 계획하고 작성되었습니다.
        `self.X`의 각 원소를 순회하면서 `self.X`의 원소가 매개 변수로 주어진 배열 `x`에 포함되는지 확인합니다.
        (비효율 주의) `predict`에서 이 메서드가 $len(x)$회 호출될 것으로 기대되므로, 시나리오에 따르면 최종적인 시간복잡도는 $O(len(x) len(self.X) + O(sort))$ 입니다.
        '''
        x = np.sort(x)[:self.n_neighbors]
        y_idx = []
        for i in range(self.X.shape[0]):
            each = self.X[i]
            if each in x:
                y_idx.append(i)
        return y_idx

    def _predict_optimize_2d_array(self, x):
        '''
        `_predict_optimize_2d_array`는 `predict` 메서드에 의해 호출될 것을 계획하고 작성되었습니다.
        '''
        nx = x.tolist()
        nx = [nx[i] + [i] for i in range(len(nx))]
        nx.sort(key=lambda each: sum(map(lambda x: abs(x), each)))
        return [*map(lambda each: each[-1], nx[:self.n_neighbors])]
