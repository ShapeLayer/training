# Binary Search
이진 탐색

이진 탐색은 오름차순 리스트 상에서 특정 수가 존재하는지 확인하는 알고리즘이다.

## 개념
리스트를 반씩 갈라서 빠르게 검색 대상 수가 있는 범위로 접근하여 조사한다.

```
[1, 2, 3, 4, 5, 6, 7, 8, 9] 에서 2를 찾으려면

1. 5를 기준으로 리스트를 반으로 가르면 2는 5보다 작다.
[1, 2, 3, 4]

2. 3(= 4//2번째 요소)을 기준으로 3은 2보다 작다.
[1, 2]

3. 2(= 2//2번째 요소)는 2이다. 검색 끝
```

## 예시 코드
[binary_search.py](./binary_search.py)

## 관련 문제
 * [수 찾기](https://www.acmicpc.net/problem/1920) - 백준 1920번 문제