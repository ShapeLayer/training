# 인공지능 과제 \#1

> HW#01  
> kNN을 구현하여 python 코드를 제출하시오.  
> 
> 기한: 3월 27일 (수) 오후 1시  

## 시작하기

### 의존성 설치

* numpy >= 1.24.3
* scikit-learn >= 1.3.0

```bash
pip install -r requirements
```

### 구현체 설명

* `app.py` - kNN 구현체 활용 및 성능 평가
* `kNN.py` - kNN 구현체

* 구현체에서 채택한 처리법: X_test의 각 요소에 대해서, X_trained에 빼기 연산 수행; 연산 결과의 절댓값을 취한 후 합산; 합산한 결과를 오름차순으로 정렬

**성능 실험 결과**   
| 방식 | `sklearn.metrices.accuracy_score()` |
| :-: | :-: |
| `sklearn.neighbors.KNeighborsClassifier` 사용 | $0.9666666666666667$ |
| X_test의 각 요소에 대해서, X_trained에 빼기 연산 수행; 연산 결과의 절댓값을 취한 후 합산; 합산한 결과를 오름차순으로 정렬 | $0.9333333333333333$ |
| X_test의 각 요소에 대해서, X_trained에 빼기 연산 수행; 연산 결과 단순 합산; 합산한 결과를 오름차순으로 정렬 | $0.5333333333333333$ |
