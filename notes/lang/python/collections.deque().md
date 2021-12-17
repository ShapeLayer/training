# collections.deque()

> deque는 스택과 큐를 일반화한 것입니다.
>
> [collections -- Python Documentation](https://docs.python.org/ko/3/library/collections.html#deque-objects)

## append
```python
append(x)
```
deque의 오른쪽에 x를 추가합니다.

## appendleft
```python
appendleft(x)
```
deque의 왼쪽에 x를 추가합니다.

## clear
```python
clear()
```
deque에서 모든 요소를 제거하고 길이가 0인 상태로 만듭니다.

## copy
```python
copy()
```
deque의 복사본을 만듭니다.

## count
```python
count(x)
```
x와 같은 deque 요소의 개수를 셉니다.

## extend
```python
extend(iterable)
```
iterable 요소를 추가하여 deque의 오른쪽을 확장합니다.

## extendleft
```python
extendleft(iterable)
```
iterable 요소를 추가하여 deque의 왼쪽을 확장합니다.

## index
```python
index(x[, start[, stop]])
```
deque에 있는 x의 위치를 반환합니다. (start 이후와 stop 이전을 범위로 검색할 수 있습니다.)  
결과를 찾을 수 없으면 ValueError를 발생시킵니다.

## insert
```python
insert(i, x)
```
x를 deque의 i번째 위치에 추가합니다.  
이로 인해 제한된 길이의 deque가 maxlen 이상으로 커지면 IndexError를 발생시킵니다.  

## pop()
```python
pop()
```
deque의 오른쪽에서 요소를 제거하고 반환합니다.  
요소가 없으면 IndexError를 발생시킵니다.

## popleft()
```python
popleft()
```
deque의 왼쪽에서 요소를 제거하고 반환합니다.  
요소가 없으면 IndexError를 발생시킵니다.  

## remove
```python
remove(value)
```
deque의 요소들 중 첫번째 value를 제거합니다.  
요소가 없으면 IndexError를 발생시킵니다.  

## reverse
```python
reverse()
```
deque 요소들의 순서를 뒤집고 None을 반환합니다.

## rotate
```python
rotate(n=1)
```
deque를 n단계 오른쪽으로 회전합니다. n이 음수이면 왼쪽으로 회전합니다.  
