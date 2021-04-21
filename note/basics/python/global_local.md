# 전역과 지역

## 전역 변수를 명시하지 않았으나 사용하고자 할 때
### 전역 변수 재할당
```python
arr = [True for i in range(4)]
def f(x):
    arr[x] = False
f(0)
```

```python
arr = [True for i in range(4)]
def f(x):
    arr = False
f(0)

UnboundLocalError: local variable 'arr' referenced before assignment
```

함수를 정의하기 이전에 선언한 `arr`의 자료형은 리스트이다. 하지만 `arr = False`는 arr에 부울 자료형을 삽입하고자 하게 되고, 파이썬은 이를 전역 변수를 재할당하는 것이 아니라 지역 변수를 사용하고자 한 것으로 인식한다.

### 할당연산자
```python
arr = [i for i in range(4)]
def f(x):
    arr.append(x)
f(0)
```

```python
arr = [i for i in range(4)]
def f(x):
    arr += [x]
f(0)

UnboundLocalError: local variable 'arr' referenced before assignment
```