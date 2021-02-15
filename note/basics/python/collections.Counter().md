# colections.Counter()

> Counter는 해시 가능한 객체를 세기 위한 dict의 하위 클래스입니다. 이것은 딕셔너리 키와 그것들의 갯수가 딕셔너리 값으로서 저장된 집합입니다. 갯수 결과는 0과 음수를 포함한 모든 정수를 사용할 수 있습니다. Counter 클래스는 다른 언어의 bags나 multisets와 비슷합니다.
> 
> [collections -- Python Documentation](https://docs.python.org/3/library/collections.html#collections.Counter)

```python
c = Counter()
c = Counter('Gallahad')
c = Counter({'red': 4, 'blue': 2})
c = Counter(cats=4, dogs=8)
```

Counter 객체는 딕셔너리 인터페이스를 가지고 있다. 하지만 찾을 수 없는 아이템이 있을때는 KeyError가 아니라 0을 반환한다.  
```python
c = Counter(['eggs', 'ham'])
```

Counter 요소 값을 0으로 지정한다 해도 해당 값이 사라지지는 않는다. del을 사용해야만 Counter에서 제거할 수 있다.
```python
c['sausage'] = 0   # sausage 값을 0으로 설정
del c['sausage']   # sausage를 Counter에서 제거
```