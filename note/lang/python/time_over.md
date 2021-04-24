# Time Over
백준 시간 초과의 원인들..

## input()
## if ~ in []
> list에 in을 하는 것은 리스트 전체를 순회해야 합니다. 내부적으로 결국 반복문이 하나 더 있는 것과 마찬가지입니다.  
> - [[파이썬3] 시간 초과 질문 있습니다](https://www.acmicpc.net/board/view/50605)

```python
if 'a' in ['a', 'b', 'c', 'd', 'e']: # 'a'부터 'e'까지 순차적으로 탐색
    print('a')
```