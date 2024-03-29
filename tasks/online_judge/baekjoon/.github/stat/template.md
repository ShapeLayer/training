# Baekjoon Online Judge

[![ShapeLayer's solved.ac stats](https://github-readme-solvedac.hyp3rflow.vercel.app/api/?handle=belline0124)](https://www.acmicpc.net/user/belline0124)

## 알고리즘 개념 정리

* 정렬
  * 위상정렬 - [1766 문제집](https://www.acmicpc.net/problem/1766), [(답안)](./python/1766.py)
    * [Jin Hur, [위상 정렬] 개념과 예제 문제: 문제집_백준](https://velog.io/@jinh2352/%EC%9C%84%EC%83%81-%EC%A0%95%EB%A0%AC)
* 경로탐색
  * 플로이드-워셜 - [17182 우주 탐사선](https://www.acmicpc.net/problem/17182), [(답안)](./python/17182.py)
    * [ChanBLOG, 알고리즘 - 플로이드-워셜(Floyd-Warshall) 알고리즘](https://chanhuiseok.github.io/posts/algo-50/)
* 다이나믹 프로그래밍
  * 배낭 문제 - [17845 수강 과목](https://www.acmicpc.net/problem/17845), [(답안)](./python/17845.py)
    * [ChanBLOG, [알고리즘 트레이닝] 5장 - 동적계획법과 냅색(Knapsack) (백준 12865번 평범한 배낭 문제로 살펴보기)](https://chanhuiseok.github.io/posts/improve-6/)
* 트리
  * 가장 가까운 공통 조상
    * [하눤석, (Python/파이썬) - 백준(BOJ) 3584번 : 가장 가까운 공통 조상](https://recordofwonseok.tistory.com/422)
    * [EVEerNew, [백준] No.11438 - LCA 2 (C++, 최소 공통 조상)](https://everenew.tistory.com/94)
  * 세그먼트 트리 - [2042 구간 합 구하기](https://www.acmicpc.net/problem/2042), [(답안)](./python/2042.py)
    * [BOJ book, 세그먼트 트리 (Segment Tree)](https://book.acmicpc.net/ds/segment-tree)
    * [kimdukbae, [자료구조] 세그먼트 트리 (Segment Tree), 2021.](https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%84%B8%EA%B7%B8%EB%A8%BC%ED%8A%B8-%ED%8A%B8%EB%A6%AC-Segment-Tree)
  * 레이지 세그먼트 트리 - [10999 구간 합 구하기 2](https://www.acmicpc.net/problem/10999), [(답안)](./rust/10999.rs)
    * [BOJ Book, 느리게 갱신되는 세그먼트 트리 (Segment Tree with Lazy Propagation)](https://book.acmicpc.net/ds/segment-tree-lazy-propagation)
* 문자열
  * KMP - [1786 찾기](https://www.acmicpc.net/problem/1786), [(답안)](./python/1786.py)
    * [까만화면, [알고리즘 공부] KMP Algorithm (문자열 검색 알고리즘), 2021.](https://bblackscene21.tistory.com/2)
  * Manacher - [13275 가장 긴 팰린드롬 부분 문자열](https://www.acmicpc.net/problem/13275), [(답안)](./python/13275.1.py)
    * [JoonDev, Manacher 알고리즘](https://kangminjun.tistory.com/entry/Manacher-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)
    * [Crocus, Manacher 알고리즘(Manacher's Algorithm)](https://www.crocus.co.kr/1075)
* 기하학
  * 선분 교차 - [17386 선분 교차 1](https://www.acmicpc.net/problem/17386), [(답안)](./swift/17386.swift)
  * 볼록 껍질 - [1708 볼록 껍질](https://www.acmicpc.net/problem/1708), [(답안)](./python/1708.py)

## 파일명 컨벤션

`<문제 번호>.(<답안 #N>).(<채점 상태>).<확장자>`  

* 통과한 코드는 파일명에 `(<채점 상태>)` 생략
* 답안이 유일하다면 `(<답안 #N>)` 생략

| `<채점 상태>` | 설명 |
| :-: | :-: |
| `wa` | 틀렸습니다! |
| `ud`, `undone` | 답안 미완성 |
| `rte` | 런타임 에러 |
| `to` | 시간 초과 |
| `oom` | 메모리 초과 |
| `nj` | 채점 안함 |

## 풀이

{statis_table}
