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


마지막 업데이트: 2024-05-22 15:15:36  
<table>
    <tr>
        <th>문제</th>
        <th>코드</th>
    </tr>
    <tr>
        <td><a href="https://www.acmicpc.net/problem/1000" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 1000 A+B</a></td>
        <td><a href="./java/1000.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a><br>
<a href="./kotlin/1000.kt"><img src="https://img.shields.io/badge/-%20-A97BFF?style=flat-square"/> Kotlin</a><br>
<a href="./cpp/1000.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./gleam/1000.nj.gleam"><img src="https://img.shields.io/badge/-%20-ffaff3?style=flat-square"/> Gleam</a><br>
<a href="./csharp/1000.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a><br>
<a href="./aheui/1000.aheui"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Aheui</a><br>
<a href="./rust/1000.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/1000.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./lua/1000.lua"><img src="https://img.shields.io/badge/-%20-000080?style=flat-square"/> Lua</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1001" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 1001 A-B</a></td>
        <td><a href="./java/1001.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a><br>
<a href="./cpp/1001.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./csharp/1001.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a><br>
<a href="./aheui/1001.aheui"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Aheui</a><br>
<a href="./rust/1001.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/1001.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./lua/1001.lua"><img src="https://img.shields.io/badge/-%20-000080?style=flat-square"/> Lua</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1002" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1002 터렛</a></td>
        <td><a href="./python/1002.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1003" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1003 피보나치 함수</a></td>
        <td><a href="./rust/1003.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1004" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1004 어린 왕자</a></td>
        <td><a href="./python/1004.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1005" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 1005 ACM Craft</a></td>
        <td><a href="./rust/1005.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./rust/1005.1.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1008" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 1008 A/B</a></td>
        <td><a href="./cpp/1008.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./csharp/1008.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a><br>
<a href="./rust/1008.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/1008.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./lua/1008.lua"><img src="https://img.shields.io/badge/-%20-000080?style=flat-square"/> Lua</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1009" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1009 분산처리</a></td>
        <td><a href="./python/1009.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1010" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1010 다리 놓기</a></td>
        <td><a href="./rust/1010.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1011" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 1011 Fly me to the Alpha Centauri</a></td>
        <td><a href="./python/1011.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1012" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 1012 유기농 배추</a></td>
        <td><a href="./rust/1012.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1015" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1015 수열 정렬</a></td>
        <td><a href="./python/1015.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1018" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1018 체스판 다시 칠하기</a></td>
        <td><a href="./python/1018.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1026" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1026 보물</a></td>
        <td><a href="./rust/1026.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1032" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1032 명령 프롬프트</a></td>
        <td><a href="./python/1032.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1037" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1037 약수</a></td>
        <td><a href="./python/1037.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1043" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1043 거짓말</a></td>
        <td><a href="./ruby/1043.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1049" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1049 기타줄</a></td>
        <td><a href="./rust/1049.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1051" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1051 숫자 정사각형</a></td>
        <td><a href="./python/1051.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1057" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1057 토너먼트</a></td>
        <td><a href="./python/1057.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1059" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1059 좋은 구간</a></td>
        <td><a href="./python/1059.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1063" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1063 킹</a></td>
        <td><a href="./python/1063.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1064" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1064 평행사변형</a></td>
        <td><a href="./python/1064.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1065" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1065 한수</a></td>
        <td><a href="./python/1065.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1068" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 1068 트리</a></td>
        <td><a href="./csharp/1068.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1072" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1072 게임</a></td>
        <td><a href="./python/1072.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1075" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1075 나누기</a></td>
        <td><a href="./python/1075.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1076" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1076 저항</a></td>
        <td><a href="./ruby/1076.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1080" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 1080 행렬</a></td>
        <td><a href="./python/1080.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1085" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 1085 직사각형에서 탈출</a></td>
        <td><a href="./python/1085.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1094" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1094 막대기</a></td>
        <td><a href="./python/1094.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1100" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1100 하얀 칸</a></td>
        <td><a href="./ruby/1100.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1106" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1106 호텔</a></td>
        <td><a href="./python/1106.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1110" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1110 더하기 사이클</a></td>
        <td><a href="./python/1110.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1145" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1145 적어도 대부분의 배수</a></td>
        <td><a href="./python/1145.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1149" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 1149 RGB거리</a></td>
        <td><a href="./python/1149.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1152" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1152 단어의 개수</a></td>
        <td><a href="./python/1152.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1157" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1157 단어 공부</a></td>
        <td><a href="./python/1157.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1158" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1158 요세푸스 문제</a></td>
        <td><a href="./cpp/1158.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1159" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1159 농구 경기</a></td>
        <td><a href="./c/1159.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1167" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 1167 트리의 지름</a></td>
        <td><a href="./rust/1167.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/1167.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1173" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1173 운동</a></td>
        <td><a href="./python/1173.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1181" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1181 단어 정렬</a></td>
        <td><a href="./python/1181.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1182" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 1182 부분수열의 합</a></td>
        <td><a href="./cpp/1182.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1193" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1193 분수찾기</a></td>
        <td><a href="./python/1193.1.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/1193.2.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1194" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 1194 달이 차오른다, 가자.</a></td>
        <td><a href="./python/1194.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/1194.oom.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1197" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1197 최소 스패닝 트리</a></td>
        <td><a href="./python/1197.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1202" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 1202 보석 도둑</a></td>
        <td><a href="./python/1202.hq.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/1202.to.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1212" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1212 8진수 2진수</a></td>
        <td><a href="./python/1212.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1213" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1213 팰린드롬 만들기</a></td>
        <td><a href="./python/1213.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1219" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 1219 오민식의 고민</a></td>
        <td><a href="./java/1219.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1225" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1225 이상한 곱셈</a></td>
        <td><a href="./python/1225.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1233" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1233 주사위</a></td>
        <td><a href="./python/1233.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1236" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1236 성 지키기</a></td>
        <td><a href="./python/1236.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1237" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 1237 정ㅋ벅ㅋ</a></td>
        <td><a href="./ruby/1237.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1244" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1244 스위치 켜고 끄기</a></td>
        <td><a href="./python/1244.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1246" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1246 온라인 판매</a></td>
        <td><a href="./python/1246.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1247" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 1247 부호</a></td>
        <td><a href="./python/1247.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1252" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1252 이진수 덧셈</a></td>
        <td><a href="./python/1252.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1259" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1259 팰린드롬수</a></td>
        <td><a href="./python/1259.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1260" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 1260 DFS와 BFS</a></td>
        <td><a href="./rust/1260.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/1260.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1264" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 1264 모음의 개수</a></td>
        <td><a href="./cpp/1264.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1267" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 1267 핸드폰 요금</a></td>
        <td><a href="./ruby/1267.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1268" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1268 임시 반장 정하기</a></td>
        <td><a href="./python/1268.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1269" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1269 대칭 차집합</a></td>
        <td><a href="./python/1269.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1271" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 1271 엄청난 부자2</a></td>
        <td><a href="./python/1271.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1275" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 1275 커피숍2</a></td>
        <td><a href="./python/1275.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1284" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 1284 집 주소</a></td>
        <td><a href="./ruby/1284.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1292" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1292 쉽게 푸는 문제</a></td>
        <td><a href="./python/1292.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1296" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1296 팀 이름 정하기</a></td>
        <td><a href="./python/1296.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1297" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1297 TV 크기</a></td>
        <td><a href="./ruby/1297.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1302" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1302 베스트셀러</a></td>
        <td><a href="./python/1302.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1309" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 1309 동물원</a></td>
        <td><a href="./rust/1309.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1316" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1316 그룹 단어 체커</a></td>
        <td><a href="./python/1316.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1325" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 1325 효율적인 해킹</a></td>
        <td><a href="./java/1325.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1330" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 1330 두 수 비교하기</a></td>
        <td><a href="./python/1330.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1333" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1333 부재중 전화</a></td>
        <td><a href="./python/1333.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1350" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1350 진짜 공간</a></td>
        <td><a href="./python/1350.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1351" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 1351 무한 수열</a></td>
        <td><a href="./python/1351.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1354" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 1354 무한 수열 2</a></td>
        <td><a href="./python/1354.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1357" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1357 뒤집힌 덧셈</a></td>
        <td><a href="./python/1357.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1358" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1358 하키</a></td>
        <td><a href="./c/1358.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1371" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1371 가장 많은 글자</a></td>
        <td><a href="./python/1371.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1374" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 1374 강의실</a></td>
        <td><a href="./python/1374.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1380" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1380 귀걸이</a></td>
        <td><a href="./rust/1380.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1392" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1392 노래 악보</a></td>
        <td><a href="./python/1392.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1393" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 1393 음하철도 구구팔</a></td>
        <td><a href="./rust/1393.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1402" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1402 아무래도이문제는A번난이도인것같다</a></td>
        <td><a href="./python/1402.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1408" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1408 24</a></td>
        <td><a href="./python/1408.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1417" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1417 국회의원 선거</a></td>
        <td><a href="./python/1417.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1427" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1427 소트인사이드</a></td>
        <td><a href="./python/1427.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1436" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1436 영화감독 숌</a></td>
        <td><a href="./python/1436.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1448" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1448 삼각형 만들기</a></td>
        <td><a href="./python/1448.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1453" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1453 피시방 알바</a></td>
        <td><a href="./ruby/1453.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1463" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1463 1로 만들기</a></td>
        <td><a href="./rust/1463.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1475" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1475 방 번호</a></td>
        <td><a href="./python/1475.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1476" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1476 날짜 계산</a></td>
        <td><a href="./rust/1476.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/1476.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1516" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 1516 게임 개발</a></td>
        <td><a href="./python/1516.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1535" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 1535 안녕</a></td>
        <td><a href="./rust/1535.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1543" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1543 문서 검색</a></td>
        <td><a href="./python/1543.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1546" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1546 평균</a></td>
        <td><a href="./python/1546.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1547" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 1547 공</a></td>
        <td><a href="./python/1547.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1550" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1550 16진수</a></td>
        <td><a href="./swift/1550.swift"><img src="https://img.shields.io/badge/-%20-F05138?style=flat-square"/> Swift</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1551" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1551 수열의 변화</a></td>
        <td><a href="./python/1551.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1557" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/21.svg" height="13" /> 1557 제곱 ㄴㄴ</a></td>
        <td><a href="./cpp/1557.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1562" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 1562 계단 수</a></td>
        <td><a href="./cpp/1562.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1564" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 1564 팩토리얼5</a></td>
        <td><a href="./ruby/1564.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1568" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1568 새</a></td>
        <td><a href="./python/1568.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1592" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1592 영식이와 친구들</a></td>
        <td><a href="./python/1592.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1598" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 1598 꼬리를 무는 숫자 나열</a></td>
        <td><a href="./ruby/1598.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1614" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1614 영식이의 손가락</a></td>
        <td><a href="./cpp/1614.wa.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1620" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1620 나는야 포켓몬 마스터 이다솜</a></td>
        <td><a href="./python/1620.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1629" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 1629 곱셈</a></td>
        <td><a href="./rust/1629.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1647" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1647 도시 분할 계획</a></td>
        <td><a href="./python/1647.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1668" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1668 트로피 진열</a></td>
        <td><a href="./python/1668.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1669" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 1669 멍멍이 쓰다듬기</a></td>
        <td><a href="./python/1669.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1673" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1673 치킨 쿠폰</a></td>
        <td><a href="./python/1673.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1676" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1676 팩토리얼 0의 개수</a></td>
        <td><a href="./rust/1676.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1684" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 1684 같은 나머지</a></td>
        <td><a href="./python/1684.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1697" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 1697 숨바꼭질</a></td>
        <td><a href="./rust/1697.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1703" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 1703 생장점</a></td>
        <td><a href="./python/1703.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1708" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 1708 볼록 껍질</a></td>
        <td><a href="./python/1708.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1712" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1712 손익분기점</a></td>
        <td><a href="./python/1712.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1715" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1715 카드 정렬하기</a></td>
        <td><a href="./python/1715.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1717" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 1717 집합의 표현</a></td>
        <td><a href="./c/1717.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1731" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1731 추론</a></td>
        <td><a href="./python/1731.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1747" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 1747 소수&팰린드롬</a></td>
        <td><a href="./python/1747.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1753" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1753 최단경로</a></td>
        <td><a href="./python/1753.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1759" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 1759 암호 만들기</a></td>
        <td><a href="./python/1759.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1764" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1764 듣보잡</a></td>
        <td><a href="./python/1764.2.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/1764.1.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1766" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 1766 문제집</a></td>
        <td><a href="./python/1766.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1769" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1769 3의 배수</a></td>
        <td><a href="./c/1769.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a><br>
<a href="./python/1769.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1773" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1773 폭죽쇼</a></td>
        <td><a href="./python/1773.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1774" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 1774 우주신과의 교감</a></td>
        <td><a href="./rust/1774.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1781" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 1781 컵라면</a></td>
        <td><a href="./python/1781.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1786" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 1786 찾기</a></td>
        <td><a href="./python/1786.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1789" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 1789 수들의 합</a></td>
        <td><a href="./ruby/1789.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1806" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1806 부분합</a></td>
        <td><a href="./python/1806.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1809" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 1809 Moo</a></td>
        <td><a href="./golfscript/1809.gs"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Golfscript</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1834" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1834 나머지와 몫이 같은 수</a></td>
        <td><a href="./python/1834.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1837" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 1837 암호제작</a></td>
        <td><a href="./python/1837.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1863" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1863 스카이라인 쉬운거</a></td>
        <td><a href="./python/1863.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1864" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1864 문어 숫자</a></td>
        <td><a href="./python/1864.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./ruby/1864.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1865" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 1865 웜홀</a></td>
        <td><a href="./csharp/1865.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1871" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1871 좋은 자동차 번호판</a></td>
        <td><a href="./swift/1871.swift"><img src="https://img.shields.io/badge/-%20-F05138?style=flat-square"/> Swift</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1874" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 1874 스택 수열</a></td>
        <td><a href="./rust/1874.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1890" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 1890 점프</a></td>
        <td><a href="./python/1890.to.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1904" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1904 01타일</a></td>
        <td><a href="./rust/1904.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1911" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 1911 흙길 보수하기</a></td>
        <td><a href="./python/1911.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1912" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 1912 연속합</a></td>
        <td><a href="./rust/1912.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1916" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 1916 최소비용 구하기</a></td>
        <td><a href="./python/1916.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1919" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1919 애너그램 만들기</a></td>
        <td><a href="./python/1919.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1920" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1920 수 찾기</a></td>
        <td><a href="./python/1920.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1922" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1922 네트워크 연결</a></td>
        <td><a href="./python/1922.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1924" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1924 2007년</a></td>
        <td><a href="./rust/1924.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1927" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 1927 최소 힙</a></td>
        <td><a href="./python/1927.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1929" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1929 소수 구하기</a></td>
        <td><a href="./python/1929.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1932" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 1932 정수 삼각형</a></td>
        <td><a href="./ruby/1932.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1934" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 1934 최소공배수</a></td>
        <td><a href="./python/1934.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1935" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1935 후위 표기식2</a></td>
        <td><a href="./python/1935.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1940" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 1940 주몽</a></td>
        <td><a href="./ruby/1940.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1948" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 1948 임계경로</a></td>
        <td><a href="./cpp/1948.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./python/1948.oom.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1964" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1964 오각형, 오각형, 오각형…</a></td>
        <td><a href="./ruby/1964.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1966" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 1966 프린터 큐</a></td>
        <td><a href="./rust/1966.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/1966.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1967" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1967 트리의 지름</a></td>
        <td><a href="./python/1967.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1976" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1976 여행 가자</a></td>
        <td><a href="./c/1976.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1977" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1977 완전제곱수</a></td>
        <td><a href="./python/1977.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1978" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 1978 소수 찾기</a></td>
        <td><a href="./python/1978.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/1987" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 1987 알파벳</a></td>
        <td><a href="./python/1987.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2010" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2010 플러그</a></td>
        <td><a href="./c/2010.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2013" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 2013 선그리기</a></td>
        <td><a href="./c/2013.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2028" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2028 자기복제수</a></td>
        <td><a href="./python/2028.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2042" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 2042 구간 합 구하기</a></td>
        <td><a href="./python/2042.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2052" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2052 지수연산</a></td>
        <td><a href="./python/2052.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2056" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 2056 작업</a></td>
        <td><a href="./python/2056.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2061" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2061 좋은 암호</a></td>
        <td><a href="./python/2061.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2075" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 2075 N번째 큰 수</a></td>
        <td><a href="./python/2075.oom.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2083" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 2083 럭비 클럽</a></td>
        <td><a href="./ruby/2083.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2098" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 2098 외판원 순회</a></td>
        <td><a href="./cpp/2098.undone.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2108" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 2108 통계학</a></td>
        <td><a href="./python/2108.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2139" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2139 나는 너가 살아온 날을 알고 있다</a></td>
        <td><a href="./python/2139.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2140" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 2140 지뢰찾기</a></td>
        <td><a href="./python/2140.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2141" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 2141 우체국</a></td>
        <td><a href="./python/2141.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/2141.to.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2149" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 2149 암호 해독</a></td>
        <td><a href="./python/2149.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2150" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 2150 Strongly Connected Component</a></td>
        <td><a href="./python/2150.1.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2153" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2153 소수 단어</a></td>
        <td><a href="./python/2153.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2162" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 2162 선분 그룹</a></td>
        <td><a href="./swift/2162.swift"><img src="https://img.shields.io/badge/-%20-F05138?style=flat-square"/> Swift</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2163" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 2163 초콜릿 자르기</a></td>
        <td><a href="./python/2163.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2164" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 2164 카드2</a></td>
        <td><a href="./python/2164.2.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/2164.1.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2166" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2166 다각형의 면적</a></td>
        <td><a href="./python/2166.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2170" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2170 선 긋기</a></td>
        <td><a href="./python/2170.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2174" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2174 로봇 시뮬레이션</a></td>
        <td><a href="./c/2174.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2178" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 2178 미로 탐색</a></td>
        <td><a href="./rust/2178.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2193" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 2193 이친수</a></td>
        <td><a href="./python/2193.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2206" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 2206 벽 부수고 이동하기</a></td>
        <td><a href="./rust/2206.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2212" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2212 센서</a></td>
        <td><a href="./rust/2212.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2225" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2225 합분해</a></td>
        <td><a href="./python/2225.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2229" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2229 조 짜기</a></td>
        <td><a href="./python/2229.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2231" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2231 분해합</a></td>
        <td><a href="./rust/2231.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2232" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 2232 지뢰</a></td>
        <td><a href="./rust/2232.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2239" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 2239 스도쿠</a></td>
        <td><a href="./python/2239.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2252" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 2252 줄 세우기</a></td>
        <td><a href="./rust/2252.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2254" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/17.svg" height="13" /> 2254 감옥 건설</a></td>
        <td><a href="./python/2254.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2289" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 2289 Quack</a></td>
        <td><a href="./asm_x86_64/2289.asm"><img src="https://img.shields.io/badge/-%20-6E4C13?style=flat-square"/> Assembly x86_64</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2292" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2292 벌집</a></td>
        <td><a href="./python/2292.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2293" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2293 동전 1</a></td>
        <td><a href="./rust/2293.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2302" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 2302 극장 좌석</a></td>
        <td><a href="./rust/2302.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2303" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 2303 숫자 게임</a></td>
        <td><a href="./python/2303.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2309" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 2309 일곱 난쟁이</a></td>
        <td><a href="./python/2309.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2321" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2321 Crowing</a></td>
        <td><a href="./fortran/2321.f"><img src="https://img.shields.io/badge/-%20-4d41b1?style=flat-square"/> Fortran</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2338" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2338 긴자리 계산</a></td>
        <td><a href="./java/2338.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2342" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 2342 Dance Dance Revolution</a></td>
        <td><a href="./python/2342.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2343" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 2343 기타 레슨</a></td>
        <td><a href="./python/2343.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2355" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2355 시그마</a></td>
        <td><a href="./ruby/2355.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2357" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 2357 최솟값과 최댓값</a></td>
        <td><a href="./rust/2357.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2372" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2372 Livestock Count</a></td>
        <td><a href="./ada/2372.ada"><img src="https://img.shields.io/badge/-%20-02f88c?style=flat-square"/> Ada</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2377" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2377 Pottery</a></td>
        <td><a href="./freebasic/2377.bas"><img src="https://img.shields.io/badge/-%20-141AC9?style=flat-square"/> FreeBasic</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2380" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 2380 Star</a></td>
        <td><a href="./befunge/2380.bf"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Befunge</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2386" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2386 도비의 영어 공부</a></td>
        <td><a href="./python/2386.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2387" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2387 Howl</a></td>
        <td><a href="./algol68/2387.a68"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Algol68</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2393" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2393 Rook</a></td>
        <td><a href="./python/2393.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2407" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 2407 조합</a></td>
        <td><a href="./python/2407.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2420" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2420 사파리월드</a></td>
        <td><a href="./ruby/2420.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2436" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2436 공약수</a></td>
        <td><a href="./rust/2436.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2438" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2438 별 찍기 - 1</a></td>
        <td><a href="./python/2438.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2439" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 2439 별 찍기 - 2</a></td>
        <td><a href="./python/2439.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2440" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 2440 별 찍기 - 3</a></td>
        <td><a href="./python/2440.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2441" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2441 별 찍기 - 4</a></td>
        <td><a href="./python/2441.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2442" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2442 별 찍기 - 5</a></td>
        <td><a href="./python/2442.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2443" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2443 별 찍기 - 6</a></td>
        <td><a href="./python/2443.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2444" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2444 별 찍기 - 7</a></td>
        <td><a href="./python/2444.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2445" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2445 별 찍기 - 8</a></td>
        <td><a href="./java/2445.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2446" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2446 별 찍기 - 9</a></td>
        <td><a href="./java/2446.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2455" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2455 지능형 기차</a></td>
        <td><a href="./java/2455.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2460" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2460 지능형 기차 2</a></td>
        <td><a href="./java/2460.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2467" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2467 용액</a></td>
        <td><a href="./python/2467.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2470" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2470 두 용액</a></td>
        <td><a href="./python/2470.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2473" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 2473 세 용액</a></td>
        <td><a href="./python/2473.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2475" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2475 검증수</a></td>
        <td><a href="./python/2475.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2476" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2476 주사위 게임</a></td>
        <td><a href="./python/2476.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2480" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 2480 주사위 세개</a></td>
        <td><a href="./python/2480.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2484" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2484 주사위 네개</a></td>
        <td><a href="./python/2484.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2485" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 2485 가로수</a></td>
        <td><a href="./python/2485.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2490" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2490 윷놀이</a></td>
        <td><a href="./java/2490.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2493" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2493 탑</a></td>
        <td><a href="./python/2493.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2495" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2495 연속구간</a></td>
        <td><a href="./python/2495.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2501" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2501 약수 구하기</a></td>
        <td><a href="./python/2501.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2504" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2504 괄호의 값</a></td>
        <td><a href="./python/2504.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2506" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2506 점수계산</a></td>
        <td><a href="./java/2506.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2511" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2511 카드놀이</a></td>
        <td><a href="./python/2511.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2512" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 2512 예산</a></td>
        <td><a href="./python/2512.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2522" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2522 별 찍기 - 12</a></td>
        <td><a href="./java/2522.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2523" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2523 별 찍기 - 13</a></td>
        <td><a href="./java/2523.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2525" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2525 오븐 시계</a></td>
        <td><a href="./python/2525.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2529" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 2529 부등호</a></td>
        <td><a href="./python/2529.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2530" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 2530 인공지능 시계</a></td>
        <td><a href="./python/2530.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2546" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 2546 경제학과 정원영</a></td>
        <td><a href="./python/2546.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2547" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2547 사탕 선생 고창영</a></td>
        <td><a href="./java/2547.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2548" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 2548 대표 자연수</a></td>
        <td><a href="./rust/2548.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2555" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 2555 생일 출력하기</a></td>
        <td><a href="./text/2555.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2557" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2557 Hello World</a></td>
        <td><a href="./asm_x86/2557.asm"><img src="https://img.shields.io/badge/-%20-6E4C13?style=flat-square"/> Assembly x86</a><br>
<a href="./java/2557.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a><br>
<a href="./c/2557.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a><br>
<a href="./cpp/2557.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./gleam/2557.nj.gleam"><img src="https://img.shields.io/badge/-%20-ffaff3?style=flat-square"/> Gleam</a><br>
<a href="./csharp/2557.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a><br>
<a href="./umm/2557.umm"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Ummjoonsik</a><br>
<a href="./text/2557.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a><br>
<a href="./aheui/2557.aheui"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Aheui</a><br>
<a href="./swift/2557.swift"><img src="https://img.shields.io/badge/-%20-F05138?style=flat-square"/> Swift</a><br>
<a href="./rust/2557.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/2557.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./ruby/2557.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a><br>
<a href="./lua/2557.lua"><img src="https://img.shields.io/badge/-%20-000080?style=flat-square"/> Lua</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2558" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2558 A+B - 2</a></td>
        <td><a href="./python/2558.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2562" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2562 최댓값</a></td>
        <td><a href="./python/2562.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2563" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 2563 색종이</a></td>
        <td><a href="./ruby/2563.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2565" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2565 전깃줄</a></td>
        <td><a href="./rust/2565.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2566" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2566 최댓값</a></td>
        <td><a href="./java/2566.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2573" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 2573 빙산</a></td>
        <td><a href="./python/2573.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2576" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2576 홀수</a></td>
        <td><a href="./python/2576.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2577" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2577 숫자의 개수</a></td>
        <td><a href="./cpp/2577.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./python/2577.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2579" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 2579 계단 오르기</a></td>
        <td><a href="./cpp/2579.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./python/2579.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2580" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 2580 스도쿠</a></td>
        <td><a href="./python/2580.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2581" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2581 소수</a></td>
        <td><a href="./cpp/2581.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./python/2581.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2583" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 2583 영역 구하기</a></td>
        <td><a href="./python/2583.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2587" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2587 대표값2</a></td>
        <td><a href="./python/2587.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2588" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2588 곱셈</a></td>
        <td><a href="./python/2588.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2592" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2592 대표값</a></td>
        <td><a href="./python/2592.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2596" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 2596 비밀편지</a></td>
        <td><a href="./python/2596.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2605" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2605 줄 세우기</a></td>
        <td><a href="./python/2605.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2606" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 2606 바이러스</a></td>
        <td><a href="./python/2606.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2608" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 2608 로마 숫자</a></td>
        <td><a href="./python/2608.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2609" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 2609 최대공약수와 최소공배수</a></td>
        <td><a href="./rust/2609.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2622" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 2622 삼각형만들기</a></td>
        <td><a href="./python/2622.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2628" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 2628 종이자르기</a></td>
        <td><a href="./python/2628.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2635" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 2635 수 이어가기</a></td>
        <td><a href="./rust/2635.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2667" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 2667 단지번호붙이기</a></td>
        <td><a href="./rust/2667.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/2667.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2669" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 2669 직사각형 네개의 합집합의 면적 구하기</a></td>
        <td><a href="./python/2669.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2675" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2675 문자열 반복</a></td>
        <td><a href="./python/2675.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2693" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 2693 N번째 큰 수</a></td>
        <td><a href="./ruby/2693.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2699" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 2699 격자점 컨벡스헐</a></td>
        <td><a href="./python/2699.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2702" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2702 초6 수학</a></td>
        <td><a href="./python/2702.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2711" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2711 오타맨 고창영</a></td>
        <td><a href="./python/2711.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2712" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2712 미국 스타일</a></td>
        <td><a href="./python/2712.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2720" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2720 세탁소 사장 동혁</a></td>
        <td><a href="./ruby/2720.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2721" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2721 삼각수의 합</a></td>
        <td><a href="./python/2721.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2738" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2738 행렬 덧셈</a></td>
        <td><a href="./python/2738.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2739" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2739 구구단</a></td>
        <td><a href="./python/2739.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2741" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2741 N 찍기</a></td>
        <td><a href="./python/2741.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2742" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 2742 기찍 N</a></td>
        <td><a href="./python/2742.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2743" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2743 단어 길이 재기</a></td>
        <td><a href="./ruby/2743.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2744" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2744 대소문자 바꾸기</a></td>
        <td><a href="./python/2744.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2745" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2745 진법 변환</a></td>
        <td><a href="./python/2745.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2747" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2747 피보나치 수</a></td>
        <td><a href="./rust/2747.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2748" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 2748 피보나치 수 2</a></td>
        <td><a href="./rust/2748.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2749" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 2749 피보나치 수 3</a></td>
        <td><a href="./cpp/2749.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2750" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2750 수 정렬하기</a></td>
        <td><a href="./python/2750.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2751" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 2751 수 정렬하기 2</a></td>
        <td><a href="./python/2751.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/2751.1.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2752" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 2752 세수정렬</a></td>
        <td><a href="./c/2752.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2753" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 2753 윤년</a></td>
        <td><a href="./python/2753.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2754" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2754 학점계산</a></td>
        <td><a href="./python/2754.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2765" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2765 자전거 속도</a></td>
        <td><a href="./python/2765.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2774" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2774 아름다운 수</a></td>
        <td><a href="./python/2774.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2775" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 2775 부녀회장이 될테야</a></td>
        <td><a href="./python/2775.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2776" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 2776 암기왕</a></td>
        <td><a href="./python/2776.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2783" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2783 삼각 김밥</a></td>
        <td><a href="./python/2783.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2789" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2789 유학 금지</a></td>
        <td><a href="./python/2789.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2798" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2798 블랙잭</a></td>
        <td><a href="./python/2798.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2805" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 2805 나무 자르기</a></td>
        <td><a href="./rust/2805.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/2805.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2822" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 2822 점수 계산</a></td>
        <td><a href="./python/2822.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2839" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 2839 설탕 배달</a></td>
        <td><a href="./python/2839.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2845" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 2845 파티가 끝나고 난 뒤</a></td>
        <td><a href="./python/2845.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2846" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 2846 오르막길</a></td>
        <td><a href="./python/2846.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2851" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 2851 슈퍼 마리오</a></td>
        <td><a href="./cpp/2851.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2857" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2857 FBI</a></td>
        <td><a href="./python/2857.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2863" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2863 이게 분수?</a></td>
        <td><a href="./java/2863.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2864" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2864 5와 6의 차이</a></td>
        <td><a href="./ruby/2864.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2869" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 2869 달팽이는 올라가고 싶다</a></td>
        <td><a href="./python/2869.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2875" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2875 대회 or 인턴</a></td>
        <td><a href="./java/2875.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2884" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2884 알람 시계</a></td>
        <td><a href="./python/2884.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2890" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 2890 카약</a></td>
        <td><a href="./python/2890.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2902" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2902 KMP는 왜 KMP일까?</a></td>
        <td><a href="./ruby/2902.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2903" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2903 중앙 이동 알고리즘</a></td>
        <td><a href="./python/2903.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2908" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2908 상수</a></td>
        <td><a href="./python/2908.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2914" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2914 저작권</a></td>
        <td><a href="./python/2914.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2920" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2920 음계</a></td>
        <td><a href="./python/2920.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2921" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2921 도미노</a></td>
        <td><a href="./python/2921.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2935" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2935 소음</a></td>
        <td><a href="./python/2935.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2941" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 2941 크로아티아 알파벳</a></td>
        <td><a href="./python/2941.2.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/2941.1.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2948" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2948 2009년</a></td>
        <td><a href="./python/2948.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2953" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2953 나는 요리사다</a></td>
        <td><a href="./python/2953.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2959" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2959 거북이</a></td>
        <td><a href="./python/2959.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2960" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 2960 에라토스테네스의 체</a></td>
        <td><a href="./python/2960.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2965" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2965 캥거루 세마리</a></td>
        <td><a href="./ruby/2965.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2966" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 2966 찍기</a></td>
        <td><a href="./python/2966.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2975" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2975 Transactions</a></td>
        <td><a href="./python/2975.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2985" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2985 세 수</a></td>
        <td><a href="./python/2985.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2991" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2991 사나운 개</a></td>
        <td><a href="./python/2991.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2993" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 2993 세 부분</a></td>
        <td><a href="./python/2993.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/2997" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 2997 네 번째 수</a></td>
        <td><a href="./python/2997.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3003" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 3003 킹, 퀸, 룩, 비숍, 나이트, 폰</a></td>
        <td><a href="./ruby/3003.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3004" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3004 체스판 조각</a></td>
        <td><a href="./ruby/3004.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3009" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3009 네 번째 점</a></td>
        <td><a href="./python/3009.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3020" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 3020 개똥벌레</a></td>
        <td><a href="./cpp/3020.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3029" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3029 경고</a></td>
        <td><a href="./python/3029.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3034" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3034 앵그리 창영</a></td>
        <td><a href="./ruby/3034.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3040" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 3040 백설 공주와 일곱 난쟁이</a></td>
        <td><a href="./java/3040.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3046" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 3046 R2</a></td>
        <td><a href="./python/3046.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3049" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 3049 다각형의 대각선</a></td>
        <td><a href="./ruby/3049.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3052" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 3052 나머지</a></td>
        <td><a href="./python/3052.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3053" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3053 택시 기하학</a></td>
        <td><a href="./python/3053.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3058" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3058 짝수를 찾아라</a></td>
        <td><a href="./python/3058.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3059" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3059 등장하지 않는 문자의 합</a></td>
        <td><a href="./python/3059.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3060" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 3060 욕심쟁이 돼지</a></td>
        <td><a href="./c/3060.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3063" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 3063 게시판</a></td>
        <td><a href="./python/3063.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3067" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 3067 Coins</a></td>
        <td><a href="./c/3067.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3077" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 3077 임진왜란</a></td>
        <td><a href="./python/3077.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3109" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 3109 빵집</a></td>
        <td><a href="./cpp/3109.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./python/3109.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3151" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 3151 합이 0</a></td>
        <td><a href="./python/3151.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3273" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 3273 두 수의 합</a></td>
        <td><a href="./python/3273.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3276" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3276 ICONS</a></td>
        <td><a href="./python/3276.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3460" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3460 이진수</a></td>
        <td><a href="./python/3460.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3507" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3507 Automated Telephone Exchange</a></td>
        <td><a href="./python/3507.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3512" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3512 Flat</a></td>
        <td><a href="./python/3512.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3578" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 3578 Holes</a></td>
        <td><a href="./python/3578.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3584" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 3584 가장 가까운 공통 조상</a></td>
        <td><a href="./csharp/3584.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3613" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 3613 Java vs C++</a></td>
        <td><a href="./python/3613.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3649" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 3649 로봇 프로젝트</a></td>
        <td><a href="./python/3649.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3679" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/17.svg" height="13" /> 3679 단순 다각형</a></td>
        <td><a href="./python/3679.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3733" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 3733 Shares</a></td>
        <td><a href="./python/3733.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3765" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 3765 Celebrity jeopardy</a></td>
        <td><a href="./python/3765.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3780" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 3780 네트워크 연결</a></td>
        <td><a href="./python/3780.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3787" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 3787 Count on Canton</a></td>
        <td><a href="./python/3787.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3830" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/18.svg" height="13" /> 3830 교수님은 기다리지 않는다</a></td>
        <td><a href="./python/3830.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/3845" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 3845 잔디깎기</a></td>
        <td><a href="./python/3845.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4101" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 4101 크냐?</a></td>
        <td><a href="./python/4101.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4153" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 4153 직각삼각형</a></td>
        <td><a href="./python/4153.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4181" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/17.svg" height="13" /> 4181 Convex Hull</a></td>
        <td><a href="./python/4181.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4195" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 4195 친구 네트워크</a></td>
        <td><a href="./python/4195.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4225" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/18.svg" height="13" /> 4225 쓰레기 슈트</a></td>
        <td><a href="./python/4225.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4299" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 4299 AFC 윔블던</a></td>
        <td><a href="./ruby/4299.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4344" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 4344 평균은 넘겠지</a></td>
        <td><a href="./python/4344.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4358" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 4358 생태학</a></td>
        <td><a href="./python/4358.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4375" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 4375 1</a></td>
        <td><a href="./python/4375.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4378" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 4378 트ㅏㅊ;</a></td>
        <td><a href="./python/4378.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4386" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 4386 별자리 만들기</a></td>
        <td><a href="./python/4386.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4458" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 4458 첫 글자를 대문자로</a></td>
        <td><a href="./python/4458.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4470" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 4470 줄번호</a></td>
        <td><a href="./ruby/4470.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4493" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 4493 가위 바위 보?</a></td>
        <td><a href="./python/4493.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4504" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 4504 배수 찾기</a></td>
        <td><a href="./python/4504.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4562" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 4562 No Brainer</a></td>
        <td><a href="./python/4562.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4589" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 4589 Gnome Sequencing</a></td>
        <td><a href="./ruby/4589.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4635" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 4635 Speed Limit</a></td>
        <td><a href="./python/4635.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4659" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 4659 비밀번호 발음하기</a></td>
        <td><a href="./python/4659.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4673" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 4673 셀프 넘버</a></td>
        <td><a href="./python/4673.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4696" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 4696 St. Ives</a></td>
        <td><a href="./ruby/4696.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4714" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 4714 Lunacy</a></td>
        <td><a href="./ruby/4714.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4766" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 4766 일반 화학 실험</a></td>
        <td><a href="./lua/4766.lua"><img src="https://img.shields.io/badge/-%20-000080?style=flat-square"/> Lua</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4796" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 4796 캠핑</a></td>
        <td><a href="./ruby/4796.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4803" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 4803 트리</a></td>
        <td><a href="./rust/4803.2.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./rust/4803.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4880" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 4880 다음수</a></td>
        <td><a href="./ruby/4880.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4892" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 4892 숫자 맞추기 게임</a></td>
        <td><a href="./python/4892.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4948" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 4948 베르트랑 공준</a></td>
        <td><a href="./python/4948.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4949" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 4949 균형잡힌 세상</a></td>
        <td><a href="./python/4949.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/4999" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 4999 아!</a></td>
        <td><a href="./python/4999.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5026" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5026 박사 과정</a></td>
        <td><a href="./python/5026.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5032" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5032 탄산 음료</a></td>
        <td><a href="./python/5032.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5046" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 5046 전국 대학생 프로그래밍 대회 동아리 연합</a></td>
        <td><a href="./python/5046.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5052" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 5052 전화번호 목록</a></td>
        <td><a href="./python/5052.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5054" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5054 주차의 신</a></td>
        <td><a href="./python/5054.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5063" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5063 TGN</a></td>
        <td><a href="./python/5063.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5073" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5073 삼각형과 세 변</a></td>
        <td><a href="./ruby/5073.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5086" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5086 배수와 약수</a></td>
        <td><a href="./python/5086.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5107" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 5107 마니또</a></td>
        <td><a href="./python/5107.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5176" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5176 대회 자리</a></td>
        <td><a href="./python/5176.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5218" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5218 알파벳 거리</a></td>
        <td><a href="./python/5218.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5300" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 5300 Fill the Rowboats!</a></td>
        <td><a href="./python/5300.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5337" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 5337 웰컴</a></td>
        <td><a href="./ruby/5337.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5338" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 5338 마이크로소프트 로고</a></td>
        <td><a href="./text/5338.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5339" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 5339 콜센터</a></td>
        <td><a href="./text/5339.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5347" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 5347 LCM</a></td>
        <td><a href="./python/5347.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5354" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5354 J박스</a></td>
        <td><a href="./java/5354.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5355" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5355 화성 수학</a></td>
        <td><a href="./python/5355.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5357" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 5357 Dedupe</a></td>
        <td><a href="./python/5357.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5358" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 5358 Football Team</a></td>
        <td><a href="./python/5358.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5361" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5361 전투 드로이드 가격</a></td>
        <td><a href="./java/5361.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5430" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 5430 AC</a></td>
        <td><a href="./python/5430.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5522" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 5522 카드 게임</a></td>
        <td><a href="./java/5522.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5523" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5523 경기 결과</a></td>
        <td><a href="./ruby/5523.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5524" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 5524 입실 관리</a></td>
        <td><a href="./ruby/5524.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5525" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 5525 IOIOI</a></td>
        <td><a href="./python/5525.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5532" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 5532 방학 숙제</a></td>
        <td><a href="./swift/5532.swift"><img src="https://img.shields.io/badge/-%20-F05138?style=flat-square"/> Swift</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5534" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 5534 간판</a></td>
        <td><a href="./python/5534.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5543" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 5543 상근날드</a></td>
        <td><a href="./ruby/5543.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5554" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 5554 심부름 가는 길</a></td>
        <td><a href="./java/5554.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5565" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5565 영수증</a></td>
        <td><a href="./python/5565.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5575" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 5575 타임 카드</a></td>
        <td><a href="./ruby/5575.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5576" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5576 콘테스트</a></td>
        <td><a href="./python/5576.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5585" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5585 거스름돈</a></td>
        <td><a href="./python/5585.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5586" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5586 JOI와 IOI</a></td>
        <td><a href="./ruby/5586.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5596" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 5596 시험 점수</a></td>
        <td><a href="./ruby/5596.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5597" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5597 과제 안 내신 분..?</a></td>
        <td><a href="./python/5597.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5598" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5598 카이사르 암호</a></td>
        <td><a href="./python/5598.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5612" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5612 터널의 입구와 출구</a></td>
        <td><a href="./python/5612.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5613" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5613 계산기 프로그램</a></td>
        <td><a href="./python/5613.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5622" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5622 다이얼</a></td>
        <td><a href="./python/5622.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5625" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 5625 페스트리</a></td>
        <td><a href="./python/5625.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5637" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 5637 가장 긴 단어</a></td>
        <td><a href="./python/5637.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5656" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 5656 비교 연산자</a></td>
        <td><a href="./python/5656.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5676" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 5676 음주 코딩</a></td>
        <td><a href="./python/5676.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5691" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5691 평균 중앙값 문제</a></td>
        <td><a href="./python/5691.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5692" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5692 팩토리얼 진법</a></td>
        <td><a href="./python/5692.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5717" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 5717 상근이의 친구들</a></td>
        <td><a href="./python/5717.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5724" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5724 파인만</a></td>
        <td><a href="./python/5724.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5766" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 5766 할아버지는 유명해!</a></td>
        <td><a href="./python/5766.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5789" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5789 한다 안한다</a></td>
        <td><a href="./python/5789.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5800" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 5800 성적 통계</a></td>
        <td><a href="./rust/5800.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5874" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 5874 소를 찾아라</a></td>
        <td><a href="./python/5874.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5889" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/19.svg" height="13" /> 5889 Cows in a Skyscraper</a></td>
        <td><a href="./python/5889.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5893" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5893 17배</a></td>
        <td><a href="./ruby/5893.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5928" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 5928 Contest Timing</a></td>
        <td><a href="./ruby/5928.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5972" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 5972 택배 배송</a></td>
        <td><a href="./python/5972.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/5988" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 5988 홀수일까 짝수일까</a></td>
        <td><a href="./python/5988.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6131" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 6131 완전 제곱수</a></td>
        <td><a href="./python/6131.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6194" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 6194 Building the Moat</a></td>
        <td><a href="./python/6194.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6219" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 6219 소수의 자격</a></td>
        <td><a href="./python/6219.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6322" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 6322 직각 삼각형의 두 변</a></td>
        <td><a href="./python/6322.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6359" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 6359 만취한 상범</a></td>
        <td><a href="./ruby/6359.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6378" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 6378 디지털 루트</a></td>
        <td><a href="./python/6378.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/6378.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6497" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 6497 전력난</a></td>
        <td><a href="./python/6497.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6603" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 6603 로또</a></td>
        <td><a href="./python/6603.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6749" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 6749 Next in line</a></td>
        <td><a href="./python/6749.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6763" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 6763 Speed fines are not fine!</a></td>
        <td><a href="./ruby/6763.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6764" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 6764 Sounds fishy!</a></td>
        <td><a href="./python/6764.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6778" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 6778 Which Alien?</a></td>
        <td><a href="./python/6778.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6810" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 6810 ISBN</a></td>
        <td><a href="./python/6810.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6825" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 6825 Body Mass Index</a></td>
        <td><a href="./python/6825.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6841" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 6841 I Speak TXTMSG</a></td>
        <td><a href="./python/6841.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6887" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 6887 Squares</a></td>
        <td><a href="./python/6887.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6888" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 6888 Terms of Office</a></td>
        <td><a href="./python/6888.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6916" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 6916 0123456789</a></td>
        <td><a href="./python/6916.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6962" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 6962 Maple Roundup</a></td>
        <td><a href="./python/6962.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/6975" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 6975 Deficient, Perfect, and Abundant</a></td>
        <td><a href="./python/6975.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7287" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 7287 등록</a></td>
        <td><a href="./python/7287.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7420" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/17.svg" height="13" /> 7420 맹독 방벽</a></td>
        <td><a href="./python/7420.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7489" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 7489 팩토리얼</a></td>
        <td><a href="./ruby/7489.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7510" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 7510 고급 수학</a></td>
        <td><a href="./python/7510.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7511" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 7511 소셜 네트워킹 어플리케이션</a></td>
        <td><a href="./python/7511.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7523" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 7523 Gauß</a></td>
        <td><a href="./python/7523.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7567" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 7567 그릇</a></td>
        <td><a href="./python/7567.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7569" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 7569 토마토</a></td>
        <td><a href="./rust/7569.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7572" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 7572 간지(干支)</a></td>
        <td><a href="./python/7572.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7576" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 7576 토마토</a></td>
        <td><a href="./rust/7576.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7581" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 7581 Cuboids</a></td>
        <td><a href="./python/7581.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7595" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 7595 Triangles</a></td>
        <td><a href="./python/7595.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7662" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 7662 이중 우선순위 큐</a></td>
        <td><a href="./python/7662.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7782" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 7782 Alien</a></td>
        <td><a href="./python/7782.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7785" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 7785 회사에 있는 사람</a></td>
        <td><a href="./python/7785.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7795" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 7795 먹을 것인가 먹힐 것인가</a></td>
        <td><a href="./python/7795.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7891" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 7891 Can you add this?</a></td>
        <td><a href="./ruby/7891.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/7947" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 7947 Koncert</a></td>
        <td><a href="./python/7947.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8320" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 8320 직사각형을 만드는 방법</a></td>
        <td><a href="./python/8320.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8370" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 8370 Plane</a></td>
        <td><a href="./ruby/8370.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8371" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 8371 Dyslexia</a></td>
        <td><a href="./python/8371.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8387" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 8387 Dyslexia</a></td>
        <td><a href="./python/8387.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8393" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 8393 합</a></td>
        <td><a href="./python/8393.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8437" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 8437 Julka</a></td>
        <td><a href="./ruby/8437.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8464" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/21.svg" height="13" /> 8464 Non-Squarefree Numbers</a></td>
        <td><a href="./cpp/8464.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8545" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 8545 Zadanie próbne</a></td>
        <td><a href="./ruby/8545.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8558" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 8558 Silnia</a></td>
        <td><a href="./ruby/8558.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8574" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 8574 Ratownik</a></td>
        <td><a href="./python/8574.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8674" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 8674 Tabliczka</a></td>
        <td><a href="./python/8674.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8710" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 8710 Koszykarz</a></td>
        <td><a href="./python/8710.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8718" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 8718 Bałwanek</a></td>
        <td><a href="./ruby/8718.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8723" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 8723 Patyki</a></td>
        <td><a href="./ruby/8723.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8760" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 8760 Schronisko</a></td>
        <td><a href="./ruby/8760.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8871" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 8871 Zadanie próbne 2</a></td>
        <td><a href="./ruby/8871.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8932" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 8932 7종 경기</a></td>
        <td><a href="./python/8932.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8958" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 8958 OX퀴즈</a></td>
        <td><a href="./python/8958.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8974" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 8974 희주의 수학시험</a></td>
        <td><a href="./python/8974.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/8979" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 8979 올림픽</a></td>
        <td><a href="./cpp/8979.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9009" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 9009 피보나치</a></td>
        <td><a href="./cpp/9009.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9012" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 9012 괄호</a></td>
        <td><a href="./python/9012.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9020" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 9020 골드바흐의 추측</a></td>
        <td><a href="./python/9020.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9025" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 9025 Widest Path</a></td>
        <td><a href="./python/9025.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9063" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9063 대지</a></td>
        <td><a href="./ruby/9063.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9076" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 9076 점수 집계</a></td>
        <td><a href="./java/9076.2.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a><br>
<a href="./java/9076.1.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9084" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 9084 동전</a></td>
        <td><a href="./c/9084.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9085" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9085 더하기</a></td>
        <td><a href="./cpp/9085.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9086" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 9086 문자열</a></td>
        <td><a href="./python/9086.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9093" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 9093 단어 뒤집기</a></td>
        <td><a href="./python/9093.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9094" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9094 수학적 호기심</a></td>
        <td><a href="./python/9094.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9095" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 9095 1, 2, 3 더하기</a></td>
        <td><a href="./rust/9095.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9184" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 9184 신나는 함수 실행</a></td>
        <td><a href="./rust/9184.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9243" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 9243 파일 완전 삭제</a></td>
        <td><a href="./ruby/9243.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9252" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 9252 LCS 2</a></td>
        <td><a href="./rust/9252.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9253" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 9253 스페셜 저지</a></td>
        <td><a href="./python/9253.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9265" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 9265 Count</a></td>
        <td><a href="./python/9265.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9297" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9297 Reducing Improper Fractions</a></td>
        <td><a href="./python/9297.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9298" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9298 Ant Entrapment</a></td>
        <td><a href="./python/9298.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9299" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9299 Math Tutoring</a></td>
        <td><a href="./python/9299.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9306" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9306 Practice: Roll Call</a></td>
        <td><a href="./python/9306.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9310" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9310 Arithmetic and Geometric Sums</a></td>
        <td><a href="./python/9310.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9316" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 9316 Hello Judge</a></td>
        <td><a href="./python/9316.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9317" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9317 Monitor DPI</a></td>
        <td><a href="./python/9317.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9322" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 9322 철벽 보안 알고리즘</a></td>
        <td><a href="./python/9322.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9325" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9325 얼마?</a></td>
        <td><a href="./python/9325.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9333" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 9333 돈 갚기</a></td>
        <td><a href="./python/9333.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9366" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9366 삼각형 분류</a></td>
        <td><a href="./python/9366.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9372" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 9372 상근이의 여행</a></td>
        <td><a href="./python/9372.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9375" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 9375 패션왕 신해빈</a></td>
        <td><a href="./python/9375.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9440" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 9440 숫자 더하기</a></td>
        <td><a href="./ruby/9440.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9461" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 9461 파도반 수열</a></td>
        <td><a href="./python/9461.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9465" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 9465 스티커</a></td>
        <td><a href="./python/9465.undone.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9469" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9469 폰 노이만</a></td>
        <td><a href="./python/9469.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9471" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 9471 피사노 주기</a></td>
        <td><a href="./cpp/9471.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9493" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9493 길면 기차, 기차는 빨라, 빠른 것은 비행기</a></td>
        <td><a href="./python/9493.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9498" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 9498 시험 성적</a></td>
        <td><a href="./python/9498.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9501" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9501 꿍의 우주여행</a></td>
        <td><a href="./python/9501.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9506" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 9506 약수들의 합</a></td>
        <td><a href="./python/9506.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9517" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9517 아이 러브 크로아티아</a></td>
        <td><a href="./python/9517.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9536" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 9536 여우는 어떻게 울지?</a></td>
        <td><a href="./python/9536.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9546" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 9546 3000번 버스</a></td>
        <td><a href="./python/9546.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9550" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9550 아이들은 사탕을 좋아해</a></td>
        <td><a href="./python/9550.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9584" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 9584 Fraud Busters</a></td>
        <td><a href="./python/9584.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9610" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9610 사분면</a></td>
        <td><a href="./python/9610.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9622" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9622 Cabin Baggage</a></td>
        <td><a href="./python/9622.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9626" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 9626 크로스워드 퍼즐</a></td>
        <td><a href="./cpp/9626.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9635" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9635 Balloons Colors</a></td>
        <td><a href="./python/9635.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9653" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 9653 스타워즈 로고</a></td>
        <td><a href="./python/9653.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9654" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 9654 나부 함대 데이터</a></td>
        <td><a href="./text/9654.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9655" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 9655 돌 게임</a></td>
        <td><a href="./rust/9655.1.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./rust/9655.2.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9656" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 9656 돌 게임 2</a></td>
        <td><a href="./python/9656.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9663" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 9663 N-Queen</a></td>
        <td><a href="./cpp/9663.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./python/9663.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9698" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9698 SAHUR & IMSA’</a></td>
        <td><a href="./python/9698.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9713" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9713 Sum of Odd Sequence</a></td>
        <td><a href="./python/9713.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9724" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9724 Perfect Cube</a></td>
        <td><a href="./python/9724.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9771" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9771 Word Searching</a></td>
        <td><a href="./python/9771.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9772" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 9772 Quadrants</a></td>
        <td><a href="./python/9772.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9773" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9773 ID Key</a></td>
        <td><a href="./python/9773.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9776" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9776 Max Volume</a></td>
        <td><a href="./python/9776.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9782" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 9782 Median</a></td>
        <td><a href="./python/9782.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9783" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9783 Easy Encryption</a></td>
        <td><a href="./python/9783.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9838" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9838 XMAS</a></td>
        <td><a href="./python/9838.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9848" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9848 Gift</a></td>
        <td><a href="./python/9848.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9907" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 9907 ID</a></td>
        <td><a href="./python/9907.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/9999" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 9999 구구</a></td>
        <td><a href="./text/9999.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10026" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 10026 적록색약</a></td>
        <td><a href="./python/10026.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10039" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 10039 평균 점수</a></td>
        <td><a href="./python/10039.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10093" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10093 숫자</a></td>
        <td><a href="./python/10093.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10101" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 10101 삼각형 외우기</a></td>
        <td><a href="./ruby/10101.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10102" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10102 개표</a></td>
        <td><a href="./python/10102.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10103" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10103 주사위 게임</a></td>
        <td><a href="./python/10103.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10156" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 10156 과자</a></td>
        <td><a href="./python/10156.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10159" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 10159 저울</a></td>
        <td><a href="./java/10159.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10162" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10162 전자레인지</a></td>
        <td><a href="./python/10162.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10170" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10170 NFC West vs North</a></td>
        <td><a href="./ruby/10170.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10171" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10171 고양이</a></td>
        <td><a href="./java/10171.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a><br>
<a href="./cpp/10171.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./rust/10171.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/10171.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10172" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10172 개</a></td>
        <td><a href="./java/10172.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a><br>
<a href="./cpp/10172.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./rust/10172.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/10172.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10173" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10173 니모를 찾아서</a></td>
        <td><a href="./python/10173.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10178" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10178 할로윈의 사탕</a></td>
        <td><a href="./python/10178.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10179" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10179 쿠폰</a></td>
        <td><a href="./ruby/10179.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10180" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10180 Ship Selection</a></td>
        <td><a href="./python/10180.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10181" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 10181 Federation Favorites</a></td>
        <td><a href="./python/10181.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10188" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 10188 Quadrilateral</a></td>
        <td><a href="./python/10188.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10189" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10189 Hook</a></td>
        <td><a href="./golfscript/10189.gs"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Golfscript</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10205" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10205 헤라클레스와 히드라</a></td>
        <td><a href="./python/10205.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10212" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 10212 Mystery</a></td>
        <td><a href="./python/10212.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10214" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10214 Baseball</a></td>
        <td><a href="./python/10214.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10216" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 10216 Count Circle Groups</a></td>
        <td><a href="./python/10216.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10250" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10250 ACM 호텔</a></td>
        <td><a href="./python/10250.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10384" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 10384 팬그램</a></td>
        <td><a href="./python/10384.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10409" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10409 서버</a></td>
        <td><a href="./python/10409.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10419" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10419 지각</a></td>
        <td><a href="./python/10419.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10430" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10430 나머지</a></td>
        <td><a href="./cpp/10430.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./python/10430.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10448" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 10448 유레카 이론</a></td>
        <td><a href="./cpp/10448.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10464" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 10464 XOR</a></td>
        <td><a href="./python/10464.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10474" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10474 분수좋아해?</a></td>
        <td><a href="./lua/10474.lua"><img src="https://img.shields.io/badge/-%20-000080?style=flat-square"/> Lua</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10480" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 10480 Oddities</a></td>
        <td><a href="./python/10480.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10569" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10569 다면체</a></td>
        <td><a href="./python/10569.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10599" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10599 페르시아의 왕들</a></td>
        <td><a href="./cpp/10599.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10610" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 10610 30</a></td>
        <td><a href="./csharp/10610.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10696" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10696 Prof. Ossama</a></td>
        <td><a href="./python/10696.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10699" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10699 오늘 날짜</a></td>
        <td><a href="./python/10699.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10707" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10707 수도요금</a></td>
        <td><a href="./c/10707.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10718" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10718 We love kriii</a></td>
        <td><a href="./java/10718.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a><br>
<a href="./cpp/10718.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./rust/10718.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/10718.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10757" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10757 큰 수 A+B</a></td>
        <td><a href="./python/10757.1.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/10757.2.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10768" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 10768 특별한 날</a></td>
        <td><a href="./ruby/10768.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10773" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 10773 제로</a></td>
        <td><a href="./python/10773.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10797" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 10797 10부제</a></td>
        <td><a href="./python/10797.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10798" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 10798 세로읽기</a></td>
        <td><a href="./java/10798.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10801" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10801 카드게임</a></td>
        <td><a href="./python/10801.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10804" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10804 카드 역배치</a></td>
        <td><a href="./python/10804.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10808" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 10808 알파벳 개수</a></td>
        <td><a href="./cpp/10808.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10809" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10809 알파벳 찾기</a></td>
        <td><a href="./python/10809.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10810" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10810 공 넣기</a></td>
        <td><a href="./python/10810.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10811" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10811 바구니 뒤집기</a></td>
        <td><a href="./python/10811.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10813" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10813 공 바꾸기</a></td>
        <td><a href="./python/10813.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10814" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 10814 나이순 정렬</a></td>
        <td><a href="./python/10814.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10815" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 10815 숫자 카드</a></td>
        <td><a href="./rust/10815.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/10815.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10816" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 10816 숫자 카드 2</a></td>
        <td><a href="./rust/10816.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10817" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10817 세 수</a></td>
        <td><a href="./python/10817.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10818" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10818 최소, 최대</a></td>
        <td><a href="./python/10818.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10819" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 10819 차이를 최대로</a></td>
        <td><a href="./python/10819.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10820" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10820 문자열 분석</a></td>
        <td><a href="./python/10820.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10821" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10821 정수의 개수</a></td>
        <td><a href="./python/10821.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10822" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10822 더하기</a></td>
        <td><a href="./python/10822.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10823" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 10823 더하기 2</a></td>
        <td><a href="./swift/10823.swift"><img src="https://img.shields.io/badge/-%20-F05138?style=flat-square"/> Swift</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10824" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10824 네 수</a></td>
        <td><a href="./python/10824.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10826" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 10826 피보나치 수 4</a></td>
        <td><a href="./rust/10826.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10828" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 10828 스택</a></td>
        <td><a href="./python/10828.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10829" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10829 이진수 변환</a></td>
        <td><a href="./python/10829.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10830" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 10830 행렬 제곱</a></td>
        <td><a href="./python/10830.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10833" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10833 사과</a></td>
        <td><a href="./python/10833.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10837" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 10837 동전 게임</a></td>
        <td><a href="./ruby/10837.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10845" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 10845 큐</a></td>
        <td><a href="./python/10845.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10865" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10865 친구 친구</a></td>
        <td><a href="./python/10865.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10866" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 10866 덱</a></td>
        <td><a href="./python/10866.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10868" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 10868 최솟값</a></td>
        <td><a href="./rust/10868.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10869" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10869 사칙연산</a></td>
        <td><a href="./cpp/10869.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./rust/10869.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/10869.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10870" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 10870 피보나치 수 5</a></td>
        <td><a href="./python/10870.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10871" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10871 X보다 작은 수</a></td>
        <td><a href="./python/10871.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10872" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10872 팩토리얼</a></td>
        <td><a href="./python/10872.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10886" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10886 0 = not cute / 1 = cute</a></td>
        <td><a href="./python/10886.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10926" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10926 ??!</a></td>
        <td><a href="./java/10926.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10942" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 10942 팰린드롬?</a></td>
        <td><a href="./python/10942.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10943" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 10943 랜덤 게임~</a></td>
        <td><a href="./text/10943.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10944" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 10944 랜덤 게임~~</a></td>
        <td><a href="./javascript/10944.1.js"><img src="https://img.shields.io/badge/-%20-f1e05a?style=flat-square"/> JavaScript</a><br>
<a href="./javascript/10944.2.js"><img src="https://img.shields.io/badge/-%20-f1e05a?style=flat-square"/> JavaScript</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10946" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 10946 랜덤 게임~~~~</a></td>
        <td><a href="./text/10946.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10947" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 10947 로또</a></td>
        <td><a href="./text/10947.wa.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10950" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10950 A+B - 3</a></td>
        <td><a href="./python/10950.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10951" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10951 A+B - 4</a></td>
        <td><a href="./python/10951.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10952" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10952 A+B - 5</a></td>
        <td><a href="./python/10952.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10953" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10953 A+B - 6</a></td>
        <td><a href="./ruby/10953.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10984" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10984 내 학점을 구해줘</a></td>
        <td><a href="./python/10984.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10987" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 10987 모음의 개수</a></td>
        <td><a href="./python/10987.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10988" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10988 팰린드롬인지 확인하기</a></td>
        <td><a href="./python/10988.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10989" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 10989 수 정렬하기 3</a></td>
        <td><a href="./c/10989.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10990" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10990 별 찍기 - 15</a></td>
        <td><a href="./python/10990.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10991" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10991 별 찍기 - 16</a></td>
        <td><a href="./python/10991.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10992" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10992 별 찍기 - 17</a></td>
        <td><a href="./python/10992.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10995" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 10995 별 찍기 - 20</a></td>
        <td><a href="./python/10995.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10998" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 10998 A×B</a></td>
        <td><a href="./cpp/10998.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./csharp/10998.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a><br>
<a href="./aheui/10998.aheui"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Aheui</a><br>
<a href="./rust/10998.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/10998.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/10999" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/17.svg" height="13" /> 10999 구간 합 구하기 2</a></td>
        <td><a href="./rust/10999.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11000" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 11000 강의실 배정</a></td>
        <td><a href="./python/11000.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11003" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 11003 최솟값 찾기</a></td>
        <td><a href="./python/11003.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11005" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 11005 진법 변환 2</a></td>
        <td><a href="./python/11005.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11006" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11006 남욱이의 닭장</a></td>
        <td><a href="./python/11006.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11021" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 11021 A+B - 7</a></td>
        <td><a href="./python/11021.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11022" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 11022 A+B - 8</a></td>
        <td><a href="./python/11022.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11023" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11023 더하기 3</a></td>
        <td><a href="./python/11023.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11024" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11024 더하기 4</a></td>
        <td><a href="./python/11024.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11034" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11034 캥거루 세마리2</a></td>
        <td><a href="./python/11034.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11046" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 11046 팰린드롬??</a></td>
        <td><a href="./python/11046.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11047" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 11047 동전 0</a></td>
        <td><a href="./rust/11047.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11048" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 11048 이동하기</a></td>
        <td><a href="./python/11048.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11050" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 11050 이항 계수 1</a></td>
        <td><a href="./python/11050.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11051" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 11051 이항 계수 2</a></td>
        <td><a href="./ruby/11051.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11053" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 11053 가장 긴 증가하는 부분 수열</a></td>
        <td><a href="./rust/11053.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11060" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 11060 점프 점프</a></td>
        <td><a href="./python/11060.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11085" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 11085 군사 이동</a></td>
        <td><a href="./python/11085.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11098" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 11098 첼시를 도와줘!</a></td>
        <td><a href="./python/11098.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11104" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 11104 Fridge of Your Dreams</a></td>
        <td><a href="./python/11104.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11109" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11109 괴짜 교수</a></td>
        <td><a href="./ruby/11109.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11121" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 11121 Communication Channels</a></td>
        <td><a href="./ruby/11121.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11134" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11134 쿠키애호가</a></td>
        <td><a href="./ruby/11134.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11170" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 11170 0의 개수</a></td>
        <td><a href="./python/11170.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11256" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 11256 사탕</a></td>
        <td><a href="./ruby/11256.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11257" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 11257 IT Passport Examination</a></td>
        <td><a href="./python/11257.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11279" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 11279 최대 힙</a></td>
        <td><a href="./python/11279.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11282" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 11282 한글</a></td>
        <td><a href="./ruby/11282.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11283" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 11283 한글 2</a></td>
        <td><a href="./python/11283.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11286" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 11286 절댓값 힙</a></td>
        <td><a href="./python/11286.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11319" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 11319 Count Me In</a></td>
        <td><a href="./python/11319.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11320" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11320 삼각 무늬 - 1</a></td>
        <td><a href="./python/11320.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11322" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 11322 Numbers are Easy</a></td>
        <td><a href="./python/11322.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11328" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 11328 Strfry</a></td>
        <td><a href="./python/11328.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11332" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 11332 시간초과</a></td>
        <td><a href="./ruby/11332.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11365" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 11365 !밀비 급일</a></td>
        <td><a href="./python/11365.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11367" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11367 Report Card Time</a></td>
        <td><a href="./python/11367.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11382" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 11382 꼬마 정민</a></td>
        <td><a href="./java/11382.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11399" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 11399 ATM</a></td>
        <td><a href="./rust/11399.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11401" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 11401 이항 계수 3</a></td>
        <td><a href="./ruby/11401.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11402" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/17.svg" height="13" /> 11402 이항 계수 4</a></td>
        <td><a href="./ruby/11402.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11437" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 11437 LCA</a></td>
        <td><a href="./rust/11437.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11478" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 11478 서로 다른 부분 문자열의 개수</a></td>
        <td><a href="./python/11478.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/11478.to.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11497" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 11497 통나무 건너뛰기</a></td>
        <td><a href="./python/11497.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11505" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 11505 구간 곱 구하기</a></td>
        <td><a href="./python/11505.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11506" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 11506 占쏙옙</a></td>
        <td><a href="./text/11506.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11508" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 11508 2+1 세일</a></td>
        <td><a href="./python/11508.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11531" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 11531 ACM 대회 채점</a></td>
        <td><a href="./python/11531.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11549" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 11549 Identifying tea</a></td>
        <td><a href="./ruby/11549.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11557" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 11557 Yangjojang of The Year</a></td>
        <td><a href="./cpp/11557.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./python/11557.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11575" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 11575 Affine Cipher</a></td>
        <td><a href="./python/11575.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11586" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11586 지영 공주님의 마법 거울</a></td>
        <td><a href="./python/11586.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11596" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 11596 Triangle</a></td>
        <td><a href="./python/11596.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11608" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 11608 Complexity</a></td>
        <td><a href="./python/11608.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11637" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 11637 인기 투표</a></td>
        <td><a href="./cpp/11637.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11648" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11648 지속</a></td>
        <td><a href="./cpp/11648.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11650" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 11650 좌표 정렬하기</a></td>
        <td><a href="./rust/11650.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/11650.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11651" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 11651 좌표 정렬하기 2</a></td>
        <td><a href="./cpp/11651.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./rust/11651.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11652" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 11652 카드</a></td>
        <td><a href="./ruby/11652.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11653" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 11653 소인수분해</a></td>
        <td><a href="./cpp/11653.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./python/11653.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11654" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 11654 아스키 코드</a></td>
        <td><a href="./python/11654.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11655" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 11655 ROT13</a></td>
        <td><a href="./python/11655.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11656" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 11656 접미사 배열</a></td>
        <td><a href="./python/11656.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11657" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 11657 타임머신</a></td>
        <td><a href="./rust/11657.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11659" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 11659 구간 합 구하기 4</a></td>
        <td><a href="./python/11659.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11660" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 11660 구간 합 구하기 5</a></td>
        <td><a href="./python/11660.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11689" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 11689 GCD(n, k) = 1</a></td>
        <td><a href="./cpp/11689.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11718" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11718 그대로 출력하기</a></td>
        <td><a href="./python/11718.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11719" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11719 그대로 출력하기 2</a></td>
        <td><a href="./python/11719.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11720" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 11720 숫자의 합</a></td>
        <td><a href="./python/11720.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11721" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11721 열 개씩 끊어 출력하기</a></td>
        <td><a href="./python/11721.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11722" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 11722 가장 긴 감소하는 부분 수열</a></td>
        <td><a href="./rust/11722.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11723" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 11723 집합</a></td>
        <td><a href="./python/11723.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11724" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 11724 연결 요소의 개수</a></td>
        <td><a href="./rust/11724.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11725" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 11725 트리의 부모 찾기</a></td>
        <td><a href="./rust/11725.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11726" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 11726 2×n 타일링</a></td>
        <td><a href="./python/11726.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11728" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 11728 배열 합치기</a></td>
        <td><a href="./python/11728.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11758" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 11758 CCW</a></td>
        <td><a href="./rust/11758.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11816" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 11816 8진수, 10진수, 16진수</a></td>
        <td><a href="./python/11816.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11866" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 11866 요세푸스 문제 0</a></td>
        <td><a href="./python/11866.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11899" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 11899 괄호 끼워넣기</a></td>
        <td><a href="./python/11899.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11908" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11908 카드</a></td>
        <td><a href="./python/11908.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11942" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 11942 고려대는 사랑입니다</a></td>
        <td><a href="./java/11942.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11943" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 11943 파일 옮기기</a></td>
        <td><a href="./ruby/11943.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11944" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 11944 NN</a></td>
        <td><a href="./python/11944.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11945" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 11945 뜨거운 붕어빵</a></td>
        <td><a href="./ruby/11945.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11948" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 11948 과목선택</a></td>
        <td><a href="./ruby/11948.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/11966" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 11966 2의 제곱인가?</a></td>
        <td><a href="./python/11966.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12018" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 12018 Yonsei TOTO</a></td>
        <td><a href="./python/12018.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12085" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 12085 Moist (Small1)</a></td>
        <td><a href="./python/12085.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12086" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 12086 Moist (Small2)</a></td>
        <td><a href="./python/12086.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12091" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 12091 이브이 진화 시키기</a></td>
        <td><a href="./python/12091.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12092" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 12092 포켓몬 GO 진화</a></td>
        <td><a href="./python/12092.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12096" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 12096 </a></td>
        <td><a href="./text/12096.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12517" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 12517 Centauri Prime (Small1)</a></td>
        <td><a href="./python/12517.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12518" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 12518 Centauri Prime (Small2)</a></td>
        <td><a href="./python/12518.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12756" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 12756 고급 여관</a></td>
        <td><a href="./python/12756.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12759" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 12759 틱! 택! 토!</a></td>
        <td><a href="./python/12759.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12760" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 12760 최후의 승자는 누구?</a></td>
        <td><a href="./csharp/12760.1.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a><br>
<a href="./csharp/12760.2.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12778" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 12778 CTP공국으로 이민 가자</a></td>
        <td><a href="./ruby/12778.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12790" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 12790 Mini Fantasy War</a></td>
        <td><a href="./python/12790.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12813" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 12813 이진수 연산</a></td>
        <td><a href="./python/12813.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12850" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 12850 본대 산책2</a></td>
        <td><a href="./python/12850.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12852" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 12852 1로 만들기 2</a></td>
        <td><a href="./python/12852.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/12865" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 12865 평범한 배낭</a></td>
        <td><a href="./rust/12865.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13118" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 13118 뉴턴과 사과</a></td>
        <td><a href="./ruby/13118.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13136" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 13136 Do Not Touch Anything</a></td>
        <td><a href="./python/13136.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13163" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 13163 닉네임에 갓 붙이기</a></td>
        <td><a href="./python/13163.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13222" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 13222 Matches</a></td>
        <td><a href="./ruby/13222.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13223" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 13223 소금 폭탄</a></td>
        <td><a href="./python/13223.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13268" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 13268 셔틀런</a></td>
        <td><a href="./python/13268.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13275" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 13275 가장 긴 팰린드롬 부분 문자열</a></td>
        <td><a href="./python/13275.2.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/13275.1.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13277" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 13277 큰 수 곱셈</a></td>
        <td><a href="./python/13277.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13300" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 13300 방 배정</a></td>
        <td><a href="./python/13300.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13306" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/17.svg" height="13" /> 13306 트리</a></td>
        <td><a href="./python/13306.pac.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13333" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 13333 Q-인덱스</a></td>
        <td><a href="./cpp/13333.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13335" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 13335 트럭</a></td>
        <td><a href="./rust/13335.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13416" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 13416 주식 투자</a></td>
        <td><a href="./python/13416.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13458" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 13458 시험 감독</a></td>
        <td><a href="./cpp/13458.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./python/13458.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13496" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 13496 The Merchant of Venice</a></td>
        <td><a href="./python/13496.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13560" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 13560 축구 게임</a></td>
        <td><a href="./rust/13560.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13565" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 13565 침투</a></td>
        <td><a href="./swift/13565.rte.swift"><img src="https://img.shields.io/badge/-%20-F05138?style=flat-square"/> Swift</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13567" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 13567 로봇</a></td>
        <td><a href="./python/13567.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13580" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 13580 Andando no tempo</a></td>
        <td><a href="./python/13580.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13597" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 13597 Tri-du</a></td>
        <td><a href="./python/13597.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13623" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 13623 Zero or One</a></td>
        <td><a href="./python/13623.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13752" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 13752 히스토그램</a></td>
        <td><a href="./python/13752.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13866" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 13866 팀 나누기</a></td>
        <td><a href="./ruby/13866.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13877" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 13877 이건 무슨 진법이지?</a></td>
        <td><a href="./cpp/13877.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13900" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 13900 순서쌍의 곱의 합</a></td>
        <td><a href="./rust/13900.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13905" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 13905 세부</a></td>
        <td><a href="./python/13905.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/13985" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 13985 Equality</a></td>
        <td><a href="./python/13985.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14038" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 14038 Tournament Selection</a></td>
        <td><a href="./python/14038.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14065" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 14065 Gorivo</a></td>
        <td><a href="./python/14065.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14173" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 14173 Square Pasture</a></td>
        <td><a href="./python/14173.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14215" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 14215 세 막대</a></td>
        <td><a href="./rust/14215.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14235" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 14235 크리스마스 선물</a></td>
        <td><a href="./python/14235.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14264" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 14264 정육각형과 삼각형</a></td>
        <td><a href="./python/14264.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14284" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 14284 간선 이어가기 2</a></td>
        <td><a href="./python/14284.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14337" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 14337 Helicopter</a></td>
        <td><a href="./visualbasic/14337.vb"><img src="https://img.shields.io/badge/-%20-945db7?style=flat-square"/> Visual Basic .NET</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14425" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 14425 문자열 집합</a></td>
        <td><a href="./python/14425.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14427" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 14427 수열과 쿼리 15</a></td>
        <td><a href="./cpp/14427.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14428" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 14428 수열과 쿼리 16</a></td>
        <td><a href="./python/14428.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14438" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 14438 수열과 쿼리 17</a></td>
        <td><a href="./rust/14438.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14443" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 14443 채점 소수 번호</a></td>
        <td><a href="./text/14443.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14444" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 14444 가장 긴 팰린드롬 부분 문자열</a></td>
        <td><a href="./python/14444.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14470" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 14470 전자레인지</a></td>
        <td><a href="./ruby/14470.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14471" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 14471 포인트 카드</a></td>
        <td><a href="./python/14471.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14487" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 14487 욱제는 효도쟁이야!!</a></td>
        <td><a href="./python/14487.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14489" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 14489 치킨 두 마리 (...)</a></td>
        <td><a href="./ruby/14489.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14490" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 14490 백대열</a></td>
        <td><a href="./rust/14490.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14491" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 14491 9진수</a></td>
        <td><a href="./python/14491.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14501" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 14501 퇴사</a></td>
        <td><a href="./rust/14501.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/14501.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14503" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 14503 로봇 청소기</a></td>
        <td><a href="./python/14503.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14517" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 14517 팰린드롬 개수 구하기 (Large)</a></td>
        <td><a href="./python/14517.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14561" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 14561 회문</a></td>
        <td><a href="./python/14561.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14567" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 14567 선수과목 (Prerequisite)</a></td>
        <td><a href="./python/14567.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14568" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 14568 2017 연세대학교 프로그래밍 경시대회</a></td>
        <td><a href="./python/14568.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14581" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 14581 팬들에게 둘러싸인 홍준</a></td>
        <td><a href="./ruby/14581.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14582" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 14582 오늘도 졌다</a></td>
        <td><a href="./python/14582.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14595" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 14595 동방 프로젝트 (Large)</a></td>
        <td><a href="./cpp/14595.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14623" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 14623 감정이입</a></td>
        <td><a href="./ruby/14623.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14624" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 14624 전북대학교</a></td>
        <td><a href="./python/14624.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14645" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 14645 와이버스 부릉부릉</a></td>
        <td><a href="./ruby/14645.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14652" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 14652 나는 행복합니다~</a></td>
        <td><a href="./ruby/14652.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14653" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 14653 너의 이름은</a></td>
        <td><a href="./python/14653.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14656" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 14656 조교는 새디스트야!!</a></td>
        <td><a href="./python/14656.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14659" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 14659 한조서열정리하고옴ㅋㅋ</a></td>
        <td><a href="./cpp/14659.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14681" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 14681 사분면 고르기</a></td>
        <td><a href="./python/14681.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14720" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 14720 우유 축제</a></td>
        <td><a href="./rust/14720.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14728" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 14728 벼락치기</a></td>
        <td><a href="./cpp/14728.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14730" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 14730 謎紛芥索紀 (Small)</a></td>
        <td><a href="./cpp/14730.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14888" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 14888 연산자 끼워넣기</a></td>
        <td><a href="./python/14888.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14889" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 14889 스타트와 링크</a></td>
        <td><a href="./cpp/14889.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14909" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 14909 양수 개수 세기</a></td>
        <td><a href="./rust/14909.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14913" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 14913 등차수열에서 항 번호 찾기</a></td>
        <td><a href="./rust/14913.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14918" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 14918 더하기</a></td>
        <td><a href="./aheui/14918.aheui"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Aheui</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14920" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 14920 3n+1 수열</a></td>
        <td><a href="./python/14920.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14924" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 14924 폰 노이만과 파리</a></td>
        <td><a href="./ruby/14924.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14928" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 14928 큰 수 (BIG)</a></td>
        <td><a href="./ruby/14928.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14929" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 14929 귀찮아 (SIB)</a></td>
        <td><a href="./rust/14929.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14935" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 14935 FA</a></td>
        <td><a href="./python/14935.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/14940" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 14940 쉬운 최단거리</a></td>
        <td><a href="./python/14940.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15000" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 15000 CAPS</a></td>
        <td><a href="./python/15000.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15025" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15025 Judging Moose</a></td>
        <td><a href="./python/15025.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15051" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15051 Máquina de café</a></td>
        <td><a href="./python/15051.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15059" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15059 Hard choice</a></td>
        <td><a href="./python/15059.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15080" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15080 Every Second Counts</a></td>
        <td><a href="./python/15080.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15128" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15128 Congruent Numbers</a></td>
        <td><a href="./python/15128.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15232" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 15232 Rectangles</a></td>
        <td><a href="./python/15232.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15236" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15236 Dominos</a></td>
        <td><a href="./python/15236.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15311" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 15311 약 팔기</a></td>
        <td><a href="./python/15311.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15372" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15372 A Simple Problem.</a></td>
        <td><a href="./python/15372.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15439" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15439 베라의 패션</a></td>
        <td><a href="./python/15439.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15474" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15474 鉛筆 (Pencils)</a></td>
        <td><a href="./python/15474.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15549" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 15549 if</a></td>
        <td><a href="./text/15549.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15550" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 15550 if 2</a></td>
        <td><a href="./text/15550.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15551" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 15551 if 3</a></td>
        <td><a href="./python/15551.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15552" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15552 빠른 A+B</a></td>
        <td><a href="./rust/15552.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a><br>
<a href="./python/15552.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15591" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 15591 MooTube (Silver)</a></td>
        <td><a href="./python/15591.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15596" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 15596 정수 N개의 합</a></td>
        <td><a href="./python/15596.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15610" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15610 Abbey Courtyard</a></td>
        <td><a href="./python/15610.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15629" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 15629 Africa</a></td>
        <td><a href="./rust/15629.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15630" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 15630 Binary Game</a></td>
        <td><a href="./aheui/15630.aheui"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Aheui</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15631" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 15631 BOJeopardy</a></td>
        <td><a href="./text/15631.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15633" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15633 Fan Death</a></td>
        <td><a href="./python/15633.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15635" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 15635 IDN Homograph Attack</a></td>
        <td><a href="./python/15635.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15636" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 15636 Linear Algebra and Group</a></td>
        <td><a href="./text/15636.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15637" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 15637 Lotto</a></td>
        <td><a href="./python/15637.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15638" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 15638 No Description</a></td>
        <td><a href="./python/15638.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15639" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 15639 Rick</a></td>
        <td><a href="./python/15639.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15640" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/17.svg" height="13" /> 15640 Satan Game</a></td>
        <td><a href="./text/15640.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a><br>
<a href="./python/15640.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15641" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 15641 SUPER SUPER BINARY SEARCH DELUXE 2.5: THE LEGEND OF THE GOLDEN MAZASSUMNIDA, EPISODE 2: THE MAZWAETL UNIVERSE, PART 2: THE PARALLEL UNIVERSE AND THE LOST MAZASSUMNIDA: GAME OF THE YEAR EDITION</a></td>
        <td><a href="./text/15641.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15643" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 15643 Yee</a></td>
        <td><a href="./text/15643.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15649" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 15649 N과 M (1)</a></td>
        <td><a href="./python/15649.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15650" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 15650 N과 M (2)</a></td>
        <td><a href="./python/15650.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15651" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 15651 N과 M (3)</a></td>
        <td><a href="./python/15651.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15652" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 15652 N과 M (4)</a></td>
        <td><a href="./python/15652.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15654" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 15654 N과 M (5)</a></td>
        <td><a href="./python/15654.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15655" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 15655 N과 M (6)</a></td>
        <td><a href="./python/15655.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15656" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 15656 N과 M (7)</a></td>
        <td><a href="./python/15656.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15657" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 15657 N과 M (8)</a></td>
        <td><a href="./python/15657.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15663" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 15663 N과 M (9)</a></td>
        <td><a href="./python/15663.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15664" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 15664 N과 M (10)</a></td>
        <td><a href="./python/15664.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15665" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 15665 N과 M (11)</a></td>
        <td><a href="./python/15665.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15666" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 15666 N과 M (12)</a></td>
        <td><a href="./ruby/15666.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15667" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15667 2018 연세대학교 프로그래밍 경진대회</a></td>
        <td><a href="./ruby/15667.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15680" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 15680 연세대학교</a></td>
        <td><a href="./java/15680.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15686" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 15686 치킨 배달</a></td>
        <td><a href="./cpp/15686.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15700" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15700 타일 채우기 4</a></td>
        <td><a href="./python/15700.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15726" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15726 이칙연산</a></td>
        <td><a href="./ruby/15726.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15727" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 15727 조별과제를 하려는데 조장이 사라졌다</a></td>
        <td><a href="./ruby/15727.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15733" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 15733 나는 누구인가</a></td>
        <td><a href="./python/15733.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15736" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 15736 청기 백기</a></td>
        <td><a href="./python/15736.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15739" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 15739 매직스퀘어</a></td>
        <td><a href="./rust/15739.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15740" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 15740 A+B - 9</a></td>
        <td><a href="./ruby/15740.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15780" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15780 멀티탭 충분하니?</a></td>
        <td><a href="./python/15780.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15781" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15781 헬멧과 조끼</a></td>
        <td><a href="./python/15781.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15784" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15784 질투진서</a></td>
        <td><a href="./python/15784.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15792" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 15792 A/B - 2</a></td>
        <td><a href="./python/15792.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15802" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 15802 타노스</a></td>
        <td><a href="./text/15802.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a><br>
<a href="./python/15802.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15809" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 15809 전국시대</a></td>
        <td><a href="./python/15809.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15818" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15818 오버플로우와 모듈러</a></td>
        <td><a href="./python/15818.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15820" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15820 맞았는데 왜 틀리죠?</a></td>
        <td><a href="./python/15820.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15829" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 15829 Hashing</a></td>
        <td><a href="./ruby/15829.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15873" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 15873 공백 없는 A+B</a></td>
        <td><a href="./ruby/15873.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15889" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 15889 호 안에 수류탄이야!!</a></td>
        <td><a href="./python/15889.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15894" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15894 수학은 체육과목 입니다</a></td>
        <td><a href="./ruby/15894.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15896" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/21.svg" height="13" /> 15896 &+ +&</a></td>
        <td><a href="./cpp/15896.rte.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./python/15896.to.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15913" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 15913 가위 바위 보 999</a></td>
        <td><a href="./text/15913.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15915" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 15915 가위 바위 보 1002</a></td>
        <td><a href="./text/15915.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15917" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15917 노솔브 방지문제야!!</a></td>
        <td><a href="./python/15917.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15921" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15921 수찬은 마린보이야!!</a></td>
        <td><a href="./lua/15921.lua"><img src="https://img.shields.io/badge/-%20-000080?style=flat-square"/> Lua</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15922" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 15922 아우으 우아으이야!!</a></td>
        <td><a href="./python/15922.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15927" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 15927 회문은 회문아니야!!</a></td>
        <td><a href="./python/15927.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15953" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 15953 상금 헌터</a></td>
        <td><a href="./ruby/15953.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15962" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 15962 새로운 시작</a></td>
        <td><a href="./ruby/15962.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15963" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 15963 CASIO</a></td>
        <td><a href="./python/15963.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15964" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 15964 이상한 기호</a></td>
        <td><a href="./java/15964.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/15969" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 15969 행복</a></td>
        <td><a href="./ruby/15969.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16017" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 16017 Telemarketer or not?</a></td>
        <td><a href="./python/16017.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16163" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 16163 #15164번_제보</a></td>
        <td><a href="./python/16163.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16170" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 16170 오늘의 날짜는?</a></td>
        <td><a href="./ruby/16170.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16171" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 16171 나는 친구가 적다 (Small)</a></td>
        <td><a href="./python/16171.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16173" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 16173 점프왕 쩰리 (Small)</a></td>
        <td><a href="./cpp/16173.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16199" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 16199 나이 계산하기</a></td>
        <td><a href="./python/16199.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16204" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 16204 카드 뽑기</a></td>
        <td><a href="./python/16204.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16394" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 16394 홍익대학교</a></td>
        <td><a href="./ruby/16394.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16395" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 16395 파스칼의 삼각형</a></td>
        <td><a href="./swift/16395.swift"><img src="https://img.shields.io/badge/-%20-F05138?style=flat-square"/> Swift</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16398" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 16398 행성 연결</a></td>
        <td><a href="./python/16398.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16430" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 16430 제리와 톰</a></td>
        <td><a href="./python/16430.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16431" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 16431 베시와 데이지</a></td>
        <td><a href="./python/16431.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16435" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 16435 스네이크버드</a></td>
        <td><a href="./python/16435.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16486" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 16486 운동장 한 바퀴</a></td>
        <td><a href="./python/16486.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16562" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 16562 친구비</a></td>
        <td><a href="./python/16562.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16570" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 16570 앞뒤가 맞는 수열</a></td>
        <td><a href="./python/16570.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16600" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 16600 Contemporary Art</a></td>
        <td><a href="./python/16600.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16673" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 16673 고려대학교에는 공식 와인이 있다</a></td>
        <td><a href="./python/16673.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16677" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 16677 악마 게임</a></td>
        <td><a href="./rust/16677.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16680" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 16680 안수빈수</a></td>
        <td><a href="./ruby/16680.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16693" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 16693 Pizza Deal</a></td>
        <td><a href="./python/16693.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16722" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 16722 결! 합!</a></td>
        <td><a href="./ruby/16722.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16724" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 16724 피리 부는 사나이</a></td>
        <td><a href="./python/16724.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16727" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 16727 ICPC</a></td>
        <td><a href="./python/16727.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16900" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 16900 이름 정하기</a></td>
        <td><a href="./python/16900.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16916" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 16916 부분 문자열</a></td>
        <td><a href="./python/16916.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16928" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 16928 뱀과 사다리 게임</a></td>
        <td><a href="./python/16928.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16953" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 16953 A → B</a></td>
        <td><a href="./rust/16953.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16967" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 16967 배열 복원하기</a></td>
        <td><a href="./python/16967.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/16969" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 16969 차량 번호판 2</a></td>
        <td><a href="./cpp/16969.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17009" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 17009 Winning Score</a></td>
        <td><a href="./java/17009.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17010" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 17010 Time to Decompress</a></td>
        <td><a href="./python/17010.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17094" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 17094 Serious Problem</a></td>
        <td><a href="./python/17094.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17113" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 17113 3분 그래프</a></td>
        <td><a href="./c/17113.1.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a><br>
<a href="./c/17113.2.c"><img src="https://img.shields.io/badge/-%20-555555?style=flat-square"/> C</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17114" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 17114 하이퍼 토마토</a></td>
        <td><a href="./python/17114.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17116" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 17116 목격자</a></td>
        <td><a href="./python/17116.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17117" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 17117 평가</a></td>
        <td><a href="./python/17117.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17118" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/20.svg" height="13" /> 17118 갓 소수</a></td>
        <td><a href="./pike/17118.pike"><img src="https://img.shields.io/badge/-%20-005390?style=flat-square"/> Pike</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17119" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 17119 오색 정리</a></td>
        <td><a href="./python/17119.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17174" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 17174 전체 계산 횟수</a></td>
        <td><a href="./python/17174.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17182" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 17182 우주 탐사선</a></td>
        <td><a href="./python/17182.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a><br>
<a href="./python/17182.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17202" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 17202 핸드폰 번호 궁합</a></td>
        <td><a href="./python/17202.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17219" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 17219 비밀번호 찾기</a></td>
        <td><a href="./python/17219.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17256" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 17256 달달함이 넘쳐흘러</a></td>
        <td><a href="./python/17256.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17263" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 17263 Sort 마스터 배지훈</a></td>
        <td><a href="./python/17263.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17266" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 17266 어두운 굴다리</a></td>
        <td><a href="./python/17266.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17295" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 17295 엔드게임 스포일러</a></td>
        <td><a href="./python/17295.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17352" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 17352 여러분의 다리가 되어 드리겠습니다!</a></td>
        <td><a href="./python/17352.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17356" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 17356 욱 제</a></td>
        <td><a href="./python/17356.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17362" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 17362 수학은 체육과목 입니다 2</a></td>
        <td><a href="./rust/17362.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17386" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 17386 선분 교차 1</a></td>
        <td><a href="./swift/17386.swift"><img src="https://img.shields.io/badge/-%20-F05138?style=flat-square"/> Swift</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17387" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 17387 선분 교차 2</a></td>
        <td><a href="./swift/17387.swift"><img src="https://img.shields.io/badge/-%20-F05138?style=flat-square"/> Swift</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17388" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 17388 와글와글 숭고한</a></td>
        <td><a href="./rust/17388.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17398" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 17398 통신망 분할</a></td>
        <td><a href="./python/17398.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17404" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 17404 RGB거리 2</a></td>
        <td><a href="./python/17404.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17496" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 17496 스타후르츠</a></td>
        <td><a href="./python/17496.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17521" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 17521 Byte Coin</a></td>
        <td><a href="./cpp/17521.2.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./cpp/17521.1.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17530" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 17530 Buffoon</a></td>
        <td><a href="./python/17530.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17548" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 17548 Greetings!</a></td>
        <td><a href="./python/17548.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17614" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 17614 369</a></td>
        <td><a href="./python/17614.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17618" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 17618 신기한 수</a></td>
        <td><a href="./python/17618.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17845" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 17845 수강 과목</a></td>
        <td><a href="./python/17845.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17863" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 17863 FYI</a></td>
        <td><a href="./python/17863.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17869" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 17869 Simple Collatz Sequence</a></td>
        <td><a href="./python/17869.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17874" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 17874 Piece of Cake!</a></td>
        <td><a href="./ruby/17874.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17903" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 17903 Counting Clauses</a></td>
        <td><a href="./ruby/17903.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17944" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 17944 퐁당퐁당 1</a></td>
        <td><a href="./python/17944.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17945" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 17945 통학의 신</a></td>
        <td><a href="./python/17945.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/17952" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 17952 과제는 끝나지 않아!</a></td>
        <td><a href="./python/17952.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18017" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 18017 총알의 속도</a></td>
        <td><a href="./python/18017.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18108" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 18108 1998년생인 내가 태국에서는 2541년생?!</a></td>
        <td><a href="./java/18108.java"><img src="https://img.shields.io/badge/-%20-b07219?style=flat-square"/> Java</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18110" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 18110 solved.ac</a></td>
        <td><a href="./python/18110.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18111" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 18111 마인크래프트</a></td>
        <td><a href="./rust/18111.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18116" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 18116 로봇 조립</a></td>
        <td><a href="./python/18116.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18185" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/21.svg" height="13" /> 18185 라면 사기 (Small)</a></td>
        <td><a href="./cpp/18185.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a><br>
<a href="./cpp/18185.2.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18186" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/22.svg" height="13" /> 18186 라면 사기 (Large)</a></td>
        <td><a href="./cpp/18186.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18198" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 18198 Basketball One-on-One</a></td>
        <td><a href="./python/18198.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18258" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 18258 큐 2</a></td>
        <td><a href="./python/18258.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18301" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 18301 Rats</a></td>
        <td><a href="./ruby/18301.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18330" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 18330 Petrol</a></td>
        <td><a href="./python/18330.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18388" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 18388 SECHT</a></td>
        <td><a href="./python/18388.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18398" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 18398 HOMWRK</a></td>
        <td><a href="./python/18398.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18408" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 18408 3 つの整数 (Three Integers)</a></td>
        <td><a href="./python/18408.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18409" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 18409 母音を数える (Counting Vowels)</a></td>
        <td><a href="./python/18409.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18411" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 18411 試験 (Exam)</a></td>
        <td><a href="./python/18411.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18414" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 18414 X に最も近い値 (The Nearest Value)</a></td>
        <td><a href="./python/18414.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18436" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/15.svg" height="13" /> 18436 수열과 쿼리 37</a></td>
        <td><a href="./rust/18436.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18691" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 18691 Pokemon Buddy</a></td>
        <td><a href="./python/18691.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18698" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 18698 The Walking Adam</a></td>
        <td><a href="./python/18698.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18765" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/19.svg" height="13" /> 18765 정*수-를+[만들자!]</a></td>
        <td><a href="./text/18765.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18822" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 18822 Beginning the Hunt</a></td>
        <td><a href="./text/18822.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18825" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 18825 눈치게임 A+B! A-B! A+B! 터렛! A+B! 피보나치 함수! A+B! A-B! A+B! 어린 왕자! A+B! ACM Craft! A+B! A-B! A+B! 습격자 초라기! A+B! 벡터 매칭! A+B! A-B! A+B! A/B! A+B! 터렛! A+B! A-B! A+B! 분산처리! A+B! A+B! 마셔라! 마셔라 마셔라! 마셔라 틀이 들어간다!</a></td>
        <td><a href="./aheui/18825.aheui"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Aheui</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18826" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 18826 A+B (MC)</a></td>
        <td><a href="./minecraft/18826.mca"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Minecraft</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18829" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 18829 0초 후에 제출할 수 있습니다.</a></td>
        <td><a href="./python/18829.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18869" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 18869 멀티버스 Ⅱ</a></td>
        <td><a href="./python/18869.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18870" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 18870 좌표 압축</a></td>
        <td><a href="./python/18870.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/18891" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 18891 제21대 국회의원 선거</a></td>
        <td><a href="./python/18891.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/19532" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 19532 수학은 비대면강의입니다</a></td>
        <td><a href="./python/19532.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/19583" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 19583 싸이버개강총회</a></td>
        <td><a href="./python/19583.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/19598" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 19598 최소 회의실 개수</a></td>
        <td><a href="./python/19598.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/19602" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 19602 Dog Treats</a></td>
        <td><a href="./python/19602.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/19617" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 19617 랜덤 게임~~~~~</a></td>
        <td><a href="./text/19617.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/19637" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 19637 IF문 좀 대신 써줘</a></td>
        <td><a href="./python/19637.to.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/19644" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 19644 좀비 떼가 기관총 진지에도 오다니</a></td>
        <td><a href="./python/19644.to.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/19698" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 19698 헛간 청약</a></td>
        <td><a href="./ruby/19698.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20040" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 20040 사이클 게임</a></td>
        <td><a href="./rust/20040.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20044" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 20044 Project Teams</a></td>
        <td><a href="./cpp/20044.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20053" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 20053 최소, 최대 2</a></td>
        <td><a href="./python/20053.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20154" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 20154 이 구역의 승자는 누구야?!</a></td>
        <td><a href="./python/20154.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20215" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 20215 Cutting Corners</a></td>
        <td><a href="./python/20215.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20232" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 20232 Archivist</a></td>
        <td><a href="./python/20232.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20233" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 20233 Bicycle</a></td>
        <td><a href="./python/20233.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20254" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 20254 Site Score</a></td>
        <td><a href="./ruby/20254.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20303" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 20303 할로윈의 양아치</a></td>
        <td><a href="./python/20303.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20332" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 20332 Divvying Up</a></td>
        <td><a href="./python/20332.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20351" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 20351 Brinkmanship</a></td>
        <td><a href="./python/20351.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20352" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 20352 Circus</a></td>
        <td><a href="./python/20352.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20353" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 20353 Atrium</a></td>
        <td><a href="./python/20353.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20492" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 20492 세금</a></td>
        <td><a href="./python/20492.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20499" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 20499 Darius님 한타 안 함?</a></td>
        <td><a href="./ruby/20499.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20500" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 20500 Ezreal 여눈부터 가네 ㅈㅈ</a></td>
        <td><a href="./python/20500.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20540" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 20540 연길이의 이상형</a></td>
        <td><a href="./python/20540.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20651" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 20651 Daisy Chains</a></td>
        <td><a href="./python/20651.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20673" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 20673 Covid-19</a></td>
        <td><a href="./ruby/20673.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20833" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 20833 Kuber</a></td>
        <td><a href="./ruby/20833.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20839" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 20839 Betygsättning</a></td>
        <td><a href="./python/20839.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20867" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 20867 Rulltrappa</a></td>
        <td><a href="./python/20867.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20920" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 20920 영단어 암기는 괴로워</a></td>
        <td><a href="./python/20920.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20955" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 20955 민서의 응급 수술</a></td>
        <td><a href="./cpp/20955.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20973" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 20973 Uddered but not Herd</a></td>
        <td><a href="./python/20973.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20975" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 20975 Just Stalling</a></td>
        <td><a href="./python/20975.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/20976" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 20976 2 番目に大きい整数 (The Second Largest Integer)</a></td>
        <td><a href="./python/20976.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21294" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 21294 와 쿼리</a></td>
        <td><a href="./python/21294.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21300" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 21300 Bottle Return</a></td>
        <td><a href="./ruby/21300.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21335" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 21335 Another Eruption</a></td>
        <td><a href="./python/21335.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21354" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 21354 Äpplen och päron</a></td>
        <td><a href="./python/21354.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21591" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 21591 Laptop Sticker</a></td>
        <td><a href="./python/21591.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21598" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 21598 SciComLove</a></td>
        <td><a href="./python/21598.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21603" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 21603 K 2K 게임</a></td>
        <td><a href="./python/21603.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21612" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 21612 Boiling Water</a></td>
        <td><a href="./python/21612.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21631" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 21631 Checkers</a></td>
        <td><a href="./python/21631.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21633" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 21633 Bank Transfer</a></td>
        <td><a href="./python/21633.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21638" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 21638 SMS from MCHS</a></td>
        <td><a href="./python/21638.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21665" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 21665 Миша и негатив</a></td>
        <td><a href="./python/21665.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21734" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 21734 SMUPC의 등장</a></td>
        <td><a href="./python/21734.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21758" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 21758 꿀 따기</a></td>
        <td><a href="./cpp/21758.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21760" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 21760 야구 시즌</a></td>
        <td><a href="./python/21760.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21866" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 21866 추첨을 통해 커피를 받자</a></td>
        <td><a href="./python/21866.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21921" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 21921 블로그</a></td>
        <td><a href="./python/21921.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21922" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 21922 학부 연구생 민상</a></td>
        <td><a href="./rust/21922.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21924" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 21924 도시 건설</a></td>
        <td><a href="./python/21924.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21939" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 21939 문제 추천 시스템 Version 1</a></td>
        <td><a href="./python/21939.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21964" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 21964 선린인터넷고등학교 교가</a></td>
        <td><a href="./python/21964.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/21966" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 21966 (중략)</a></td>
        <td><a href="./python/21966.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/22015" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 22015 金平糖 (Konpeito)</a></td>
        <td><a href="./python/22015.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/22116" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 22116 창영이와 퇴근</a></td>
        <td><a href="./python/22116.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/22155" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 22155 Простая задача</a></td>
        <td><a href="./python/22155.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/22193" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 22193 Multiply</a></td>
        <td><a href="./ruby/22193.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/22252" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 22252 정보 상인 호석</a></td>
        <td><a href="./python/22252.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/22864" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 22864 피로도</a></td>
        <td><a href="./python/22864.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/22938" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 22938 백발백준하는 명사수</a></td>
        <td><a href="./python/22938.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/22966" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 22966 가장 쉬운 문제를 찾는 문제</a></td>
        <td><a href="./python/22966.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23028" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 23028 5학년은 다니기 싫어요</a></td>
        <td><a href="./rust/23028.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23037" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 23037 5의 수난</a></td>
        <td><a href="./python/23037.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23056" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 23056 참가자 명단</a></td>
        <td><a href="./cpp/23056.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23234" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 23234 The World Responds</a></td>
        <td><a href="./ruby/23234.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23246" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 23246 Sport Climbing Combined</a></td>
        <td><a href="./python/23246.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23303" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 23303 이 문제는 D2 입니다.</a></td>
        <td><a href="./python/23303.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23324" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 23324 어려운 모든 정점 쌍 최단 거리</a></td>
        <td><a href="./cpp/23324.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23343" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 23343 JavaScript</a></td>
        <td><a href="./python/23343.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23348" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 23348 스트릿 코딩 파이터</a></td>
        <td><a href="./python/23348.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23375" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 23375 Arm Coordination</a></td>
        <td><a href="./ruby/23375.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23740" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 23740 버스 노선 개편하기</a></td>
        <td><a href="./python/23740.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23794" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 23794 골뱅이 찍기 - 정사각형</a></td>
        <td><a href="./python/23794.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23795" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 23795 사장님 도박은 재미로 하셔야 합니다</a></td>
        <td><a href="./ruby/23795.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23802" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 23802 골뱅이 찍기 - 뒤집힌 ㄱ</a></td>
        <td><a href="./python/23802.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23803" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 23803 골뱅이 찍기 - ㄴ</a></td>
        <td><a href="./python/23803.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23804" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 23804 골뱅이 찍기 - ㄷ</a></td>
        <td><a href="./python/23804.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23825" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 23825 SASA 모형을 만들어보자</a></td>
        <td><a href="./ruby/23825.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23827" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 23827 수열 (Easy)</a></td>
        <td><a href="./rust/23827.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23895" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 23895 Allocation</a></td>
        <td><a href="./rust/23895.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/23971" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 23971 ZOAC 4</a></td>
        <td><a href="./ruby/23971.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24025" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 24025 돌의 정령 줄세우기</a></td>
        <td><a href="./cpp/24025.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24057" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 24057 실수</a></td>
        <td><a href="./text/24057.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24072" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24072 帰省 (Homecoming)</a></td>
        <td><a href="./ruby/24072.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24075" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24075 計算 (Calculation)</a></td>
        <td><a href="./ruby/24075.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24078" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 24078 余り (Remainder)</a></td>
        <td><a href="./ruby/24078.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24079" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24079 移動 (Moving)</a></td>
        <td><a href="./ruby/24079.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24082" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 24082 立方体 (Cube)</a></td>
        <td><a href="./ruby/24082.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24083" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24083 短針 (Hour Hand)</a></td>
        <td><a href="./ruby/24083.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24086" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 24086 身長 (Height)</a></td>
        <td><a href="./ruby/24086.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24087" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24087 アイスクリーム (Ice Cream)</a></td>
        <td><a href="./python/24087.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24183" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24183 Affischutskicket</a></td>
        <td><a href="./python/24183.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24196" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24196 Gömda ord</a></td>
        <td><a href="./python/24196.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24262" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 24262 알고리즘 수업 - 알고리즘의 수행 시간 1</a></td>
        <td><a href="./text/24262.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24263" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24263 알고리즘 수업 - 알고리즘의 수행 시간 2</a></td>
        <td><a href="./csharp/24263.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24264" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 24264 알고리즘 수업 - 알고리즘의 수행 시간 3</a></td>
        <td><a href="./csharp/24264.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24265" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 24265 알고리즘 수업 - 알고리즘의 수행 시간 4</a></td>
        <td><a href="./csharp/24265.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24266" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 24266 알고리즘 수업 - 알고리즘의 수행 시간 5</a></td>
        <td><a href="./csharp/24266.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24267" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 24267 알고리즘 수업 - 알고리즘의 수행 시간 6</a></td>
        <td><a href="./python/24267.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24270" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 24270 미니 버킷 리스트</a></td>
        <td><a href="./python/24270.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24294" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24294 ГРАДИНА</a></td>
        <td><a href="./python/24294.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24309" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 24309 РАВЕНСТВО</a></td>
        <td><a href="./ruby/24309.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24356" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24356 ЧАСОВНИК</a></td>
        <td><a href="./python/24356.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24365" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24365 ПЧЕЛИЧКАТА МАЯ</a></td>
        <td><a href="./python/24365.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24391" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 24391 귀찮은 해강이</a></td>
        <td><a href="./cpp/24391.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24416" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 24416 알고리즘 수업 - 피보나치 수 1</a></td>
        <td><a href="./rust/24416.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24444" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 24444 알고리즘 수업 - 너비 우선 탐색 1</a></td>
        <td><a href="./rust/24444.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24445" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 24445 알고리즘 수업 - 너비 우선 탐색 2</a></td>
        <td><a href="./rust/24445.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24446" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 24446 알고리즘 수업 - 너비 우선 탐색 3</a></td>
        <td><a href="./rust/24446.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24447" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 24447 알고리즘 수업 - 너비 우선 탐색 4</a></td>
        <td><a href="./rust/24447.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24465" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 24465 데뷔의 꿈</a></td>
        <td><a href="./rust/24465.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24479" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 24479 알고리즘 수업 - 깊이 우선 탐색 1</a></td>
        <td><a href="./rust/24479.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24480" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 24480 알고리즘 수업 - 깊이 우선 탐색 2</a></td>
        <td><a href="./rust/24480.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24481" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 24481 알고리즘 수업 - 깊이 우선 탐색 3</a></td>
        <td><a href="./rust/24481.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24482" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 24482 알고리즘 수업 - 깊이 우선 탐색 4</a></td>
        <td><a href="./rust/24482.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24483" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 24483 알고리즘 수업 - 깊이 우선 탐색 5</a></td>
        <td><a href="./rust/24483.rs"><img src="https://img.shields.io/badge/-%20-dea584?style=flat-square"/> Rust</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24568" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 24568 Cupcake Party</a></td>
        <td><a href="./ruby/24568.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24723" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24723 녹색거탑</a></td>
        <td><a href="./ruby/24723.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24736" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 24736 Football Scoring</a></td>
        <td><a href="./ruby/24736.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24751" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24751 Betting</a></td>
        <td><a href="./ruby/24751.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24860" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 24860 Counting Antibodies</a></td>
        <td><a href="./ruby/24860.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24883" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 24883 자동완성</a></td>
        <td><a href="./ruby/24883.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24900" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 24900 한별 찍기</a></td>
        <td><a href="./python/24900.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24901" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 24901 Binary Game 2</a></td>
        <td><a href="./ruby/24901.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24904" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 24904 Baekjoon Wordline Judge</a></td>
        <td><a href="./text/24904.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/24905" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 24905 24905번 문제</a></td>
        <td><a href="./text/24905.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25024" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 25024 시간과 날짜</a></td>
        <td><a href="./python/25024.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25182" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 25182 청정수열 (Hard)</a></td>
        <td><a href="./ruby/25182.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25183" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 25183 인생은 한 방</a></td>
        <td><a href="./python/25183.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25191" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25191 치킨댄스를 추는 곰곰이를 본 임스</a></td>
        <td><a href="./ruby/25191.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25192" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 25192 인사성 밝은 곰곰이</a></td>
        <td><a href="./python/25192.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25193" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 25193 곰곰이의 식단 관리</a></td>
        <td><a href="./python/25193.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25206" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 25206 너의 평점은</a></td>
        <td><a href="./python/25206.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25238" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25238 가희와 방어율 무시</a></td>
        <td><a href="./ruby/25238.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25285" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 25285 심준의 병역판정검사</a></td>
        <td><a href="./python/25285.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25304" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25304 영수증</a></td>
        <td><a href="./python/25304.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25305" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 25305 커트라인</a></td>
        <td><a href="./ruby/25305.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25306" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 25306 연속 XOR</a></td>
        <td><a href="./python/25306.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25311" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 25311 UCPC에서 가장 쉬운 문제 번호는?</a></td>
        <td><a href="./ruby/25311.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25314" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 25314 코딩은 체육과목 입니다</a></td>
        <td><a href="./ruby/25314.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25323" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/16.svg" height="13" /> 25323 수 정렬하기, 근데 이제 제곱수를 곁들인</a></td>
        <td><a href="./ruby/25323.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25372" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 25372 성택이의 은밀한 비밀번호</a></td>
        <td><a href="./ruby/25372.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25377" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25377 빵</a></td>
        <td><a href="./python/25377.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25494" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25494 단순한 문제 (Small)</a></td>
        <td><a href="./ruby/25494.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25559" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 25559 패스</a></td>
        <td><a href="./ruby/25559.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25591" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25591 푸앙이와 종윤이</a></td>
        <td><a href="./python/25591.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25600" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25600 Triathlon</a></td>
        <td><a href="./python/25600.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25625" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25625 샤틀버스</a></td>
        <td><a href="./python/25625.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25628" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25628 햄버거 만들기</a></td>
        <td><a href="./python/25628.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25633" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 25633 도미노 넘어뜨리기</a></td>
        <td><a href="./python/25633.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25640" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25640 MBTI</a></td>
        <td><a href="./python/25640.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25703" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 25703 포인터 공부</a></td>
        <td><a href="./python/25703.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25704" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25704 출석 이벤트</a></td>
        <td><a href="./python/25704.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25705" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 25705 돌림판 문자열</a></td>
        <td><a href="./python/25705.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25757" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 25757 임스와 함께하는 미니게임</a></td>
        <td><a href="./python/25757.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25784" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25784 Easy-to-Solve Expressions</a></td>
        <td><a href="./python/25784.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25794" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/12.svg" height="13" /> 25794 초콜릿과 나이트 게임</a></td>
        <td><a href="./cpp/25794.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25801" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 25801 Odd/Even Strings</a></td>
        <td><a href="./python/25801.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25828" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25828 Corona Virus Testing</a></td>
        <td><a href="./python/25828.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25858" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 25858 Divide the Cash</a></td>
        <td><a href="./python/25858.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25870" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 25870 Parity of Strings</a></td>
        <td><a href="./python/25870.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25965" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 25965 미션 도네이션</a></td>
        <td><a href="./ruby/25965.rb"><img src="https://img.shields.io/badge/-%20-701516?style=flat-square"/> Ruby</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/25966" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 25966 배찬우는 배열을 좋아해</a></td>
        <td><a href="./python/25966.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26068" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 26068 치킨댄스를 추는 곰곰이를 본 임스 2</a></td>
        <td><a href="./python/26068.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26069" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 26069 붙임성 좋은 총총이</a></td>
        <td><a href="./python/26069.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26082" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 26082 WARBOY</a></td>
        <td><a href="./python/26082.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26209" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 26209 Intercepting Information</a></td>
        <td><a href="./python/26209.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26307" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 26307 Correct</a></td>
        <td><a href="./python/26307.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26489" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 26489 Gum Gum for Jay Jay</a></td>
        <td><a href="./python/26489.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26509" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 26509 Triangle</a></td>
        <td><a href="./python/26509.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26511" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 26511 Complexity</a></td>
        <td><a href="./python/26511.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26531" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 26531 Simple Sum</a></td>
        <td><a href="./python/26531.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26545" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 26545 Mathematics</a></td>
        <td><a href="./python/26545.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26574" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 26574 Copier</a></td>
        <td><a href="./python/26574.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26575" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 26575 Pups</a></td>
        <td><a href="./python/26575.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26711" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 26711 A+B</a></td>
        <td><a href="./python/26711.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26768" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 26768 H4x0r</a></td>
        <td><a href="./python/26768.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/26769" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 26769 Deski</a></td>
        <td><a href="./python/26769.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27110" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 27110 특식 배부</a></td>
        <td><a href="./python/27110.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27111" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 27111 출입 기록</a></td>
        <td><a href="./python/27111.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27182" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 27182 Rain Diary</a></td>
        <td><a href="./python/27182.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27219" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27219 Робинзон Крузо</a></td>
        <td><a href="./python/27219.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27294" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27294 몇개고?</a></td>
        <td><a href="./python/27294.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27310" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 27310 :chino_shock:</a></td>
        <td><a href="./python/27310.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27323" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27323 직사각형</a></td>
        <td><a href="./python/27323.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27324" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27324 ゾロ目 (Same Numbers)</a></td>
        <td><a href="./python/27324.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27327" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27327 時間 (Hour)</a></td>
        <td><a href="./python/27327.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27328" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27328 三方比較 (Three-Way Comparison)</a></td>
        <td><a href="./python/27328.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27331" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27331 2 桁の整数 (Two-digit Integer)</a></td>
        <td><a href="./python/27331.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27332" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 27332 11 月 (November)</a></td>
        <td><a href="./python/27332.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27389" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27389 Metronome</a></td>
        <td><a href="./python/27389.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27433" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27433 팩토리얼 2</a></td>
        <td><a href="./python/27433.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27434" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27434 팩토리얼 3</a></td>
        <td><a href="./python/27434.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27590" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 27590 Sun and Moon</a></td>
        <td><a href="./python/27590.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27836" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 27836 Paradox With Averages</a></td>
        <td><a href="./python/27836.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27865" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 27865 랜덤 게임?</a></td>
        <td><a href="./python/27865.to.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27866" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27866 문자와 문자열</a></td>
        <td><a href="./python/27866.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27885" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 27885 가희와 열리지 않는 건널목</a></td>
        <td><a href="./python/27885.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27889" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27889 특별한 학교 이름</a></td>
        <td><a href="./python/27889.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27890" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 27890 특별한 작은 분수</a></td>
        <td><a href="./python/27890.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27899" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 27899 먹었습니다!!</a></td>
        <td><a href="./text/27899.txt"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Text</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27902" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 27902 CVE: Life is Way Too Short</a></td>
        <td><a href="./python/27902.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27903" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/0.svg" height="13" /> 27903 인생</a></td>
        <td><a href="./aheui/27903.aheui"><img src="https://img.shields.io/badge/-%20-fff?style=flat-square"/> Aheui</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27918" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 27918 탁구 경기</a></td>
        <td><a href="./python/27918.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27930" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 27930 당신은 운명을 믿나요?</a></td>
        <td><a href="./python/27930.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27947" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/18.svg" height="13" /> 27947 가지 밭 게임</a></td>
        <td><a href="./python/27947.to.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27951" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 27951 옷걸이</a></td>
        <td><a href="./python/27951.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/27959" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 27959 초코바</a></td>
        <td><a href="./python/27959.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28014" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 28014 첨탑 밀어서 부수기</a></td>
        <td><a href="./python/28014.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28015" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/9.svg" height="13" /> 28015 영역 색칠</a></td>
        <td><a href="./python/28015.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28016" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 28016 경품 추첨</a></td>
        <td><a href="./python/28016.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28018" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 28018 시간이 겹칠까?</a></td>
        <td><a href="./python/28018.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28061" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 28061 레몬 따기</a></td>
        <td><a href="./python/28061.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28062" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 28062 준석이의 사탕 사기</a></td>
        <td><a href="./python/28062.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28063" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 28063 동전 복사</a></td>
        <td><a href="./python/28063.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28064" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 28064 이민희진</a></td>
        <td><a href="./python/28064.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28065" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 28065 SW 수열 구하기</a></td>
        <td><a href="./python/28065.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28074" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 28074 모비스</a></td>
        <td><a href="./python/28074.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28097" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 28097 모범생 포닉스</a></td>
        <td><a href="./python/28097.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28113" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 28113 정보섬의 대중교통</a></td>
        <td><a href="./python/28113.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28125" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/7.svg" height="13" /> 28125 2023 아주머학교 프로그래딩 정시머힌</a></td>
        <td><a href="./python/28125.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28135" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 28135 Since 1973</a></td>
        <td><a href="./python/28135.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28136" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 28136 원, 탁!</a></td>
        <td><a href="./python/28136.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28138" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 28138 재밌는 나머지 연산</a></td>
        <td><a href="./python/28138.to.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28235" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 28235 코드마스터 2023</a></td>
        <td><a href="./python/28235.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28236" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 28236 점심시간 레이스</a></td>
        <td><a href="./python/28236.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28238" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 28238 정보 선생님의 야망</a></td>
        <td><a href="./python/28238.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28281" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 28281 선물</a></td>
        <td><a href="./python/28281.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28290" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 28290 안밖? 밖안? 계단? 역계단?</a></td>
        <td><a href="./python/28290.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28295" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 28295 체육은 코딩과목 입니다</a></td>
        <td><a href="./python/28295.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28298" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/8.svg" height="13" /> 28298 더 흔한 타일 색칠 문제</a></td>
        <td><a href="./python/28298.to.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28352" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 28352 10!</a></td>
        <td><a href="./python/28352.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28444" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 28444 HI-ARC=?</a></td>
        <td><a href="./python/28444.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28691" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 28691 정보보호학부 동아리 소개</a></td>
        <td><a href="./python/28691.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/28701" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 28701 세제곱의 합</a></td>
        <td><a href="./python/28701.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/29163" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 29163 Счастье Мистера Бина</a></td>
        <td><a href="./python/29163.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/29614" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/4.svg" height="13" /> 29614 학점계산프로그램</a></td>
        <td><a href="./python/29614.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/29615" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/6.svg" height="13" /> 29615 알파빌과 베타빌</a></td>
        <td><a href="./python/29615.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/29616" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/11.svg" height="13" /> 29616 인기투표</a></td>
        <td><a href="./cpp/29616.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/29617" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/17.svg" height="13" /> 29617 동전 탑 게임</a></td>
        <td><a href="./python/29617.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/29618" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 29618 미술 시간</a></td>
        <td><a href="./python/29618.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/29699" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 29699 Welcome to SMUPC!</a></td>
        <td><a href="./python/29699.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/29725" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 29725 체스 초보 브실이</a></td>
        <td><a href="./lua/29725.lua"><img src="https://img.shields.io/badge/-%20-000080?style=flat-square"/> Lua</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/29731" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 29731 2033년 밈 투표</a></td>
        <td><a href="./python/29731.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/29736" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 29736 브실이와 친구가 되고 싶어 🤸‍♀️</a></td>
        <td><a href="./python/29736.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/29751" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 29751 삼각형</a></td>
        <td><a href="./python/29751.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30007" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 30007 라면 공식</a></td>
        <td><a href="./python/30007.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30008" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 30008 준영이의 등급</a></td>
        <td><a href="./python/30008.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30017" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 30017 치즈버거 만들기</a></td>
        <td><a href="./python/30017.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30030" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 30030 스위트콘 가격 구하기</a></td>
        <td><a href="./python/30030.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30031" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 30031 지폐 세기</a></td>
        <td><a href="./python/30031.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30087" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 30087 진흥원 세미나</a></td>
        <td><a href="./python/30087.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30214" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 30214 An Easy-Peasy Problem</a></td>
        <td><a href="./python/30214.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30224" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 30224 Lucky 7</a></td>
        <td><a href="./python/30224.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30402" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 30402 감마선을 맞은 컴퓨터</a></td>
        <td><a href="./python/30402.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30468" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 30468 호반우가 학교에 지각한 이유 1</a></td>
        <td><a href="./csharp/30468.cs"><img src="https://img.shields.io/badge/-%20-178600?style=flat-square"/> C#</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30501" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 30501 관공... 어찌하여 목만 오셨소...</a></td>
        <td><a href="./python/30501.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30676" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 30676 이 별은 무슨 색일까</a></td>
        <td><a href="./python/30676.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30794" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 30794 가희와 클럽 오디션 1</a></td>
        <td><a href="./python/30794.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30868" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 30868 개표</a></td>
        <td><a href="./python/30868.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30957" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 30957 빅데이터 vs 정보보호 vs 인공지능</a></td>
        <td><a href="./python/30957.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30958" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 30958 서울사이버대학을 다니고</a></td>
        <td><a href="./python/30958.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/30999" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 30999 민주주의</a></td>
        <td><a href="./cpp/30999.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31000" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 31000 교환 분배법칙</a></td>
        <td><a href="./cpp/31000.wa.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31001" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/10.svg" height="13" /> 31001 주식 시뮬레이션</a></td>
        <td><a href="./python/31001.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31002" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/14.svg" height="13" /> 31002 그래프 변환</a></td>
        <td><a href="./python/31002.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31009" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 31009 진주로 가자! (Easy)</a></td>
        <td><a href="./python/31009.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31090" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31090 2023은 무엇이 특별할까?</a></td>
        <td><a href="./python/31090.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31403" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31403 $A + B - C$</a></td>
        <td><a href="./python/31403.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31408" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/5.svg" height="13" /> 31408 당직 근무표</a></td>
        <td><a href="./python/31408.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31410" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 31410 제독 작전</a></td>
        <td><a href="./cpp/31410.wa.cpp"><img src="https://img.shields.io/badge/-%20-f34b7d?style=flat-square"/> C++</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31413" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/13.svg" height="13" /> 31413 입대</a></td>
        <td><a href="./python/31413.wa.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31428" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31428 엘리스 트랙 매칭</a></td>
        <td><a href="./python/31428.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31429" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 31429 SUAPC 2023 Summer</a></td>
        <td><a href="./python/31429.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31450" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 31450 Everyone is a winner</a></td>
        <td><a href="./python/31450.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31495" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31495 그게 무슨 코드니..</a></td>
        <td><a href="./python/31495.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31518" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31518 Triple Sevens</a></td>
        <td><a href="./python/31518.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31606" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 31606 果物 (Fruit)</a></td>
        <td><a href="./python/31606.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31609" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31609 現れている数字 (Appearing Numbers)</a></td>
        <td><a href="./python/31609.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31610" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 31610 飴の袋詰め (Drops Packing)</a></td>
        <td><a href="./python/31610.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31611" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 31611 火曜日 (Tuesday)</a></td>
        <td><a href="./python/31611.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31612" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31612 画数数え (Stroke Count)</a></td>
        <td><a href="./python/31612.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31614" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 31614 分 (Minutes)</a></td>
        <td><a href="./python/31614.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31615" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31615 桁 (Digit)</a></td>
        <td><a href="./python/31615.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31636" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31636 三連続 (Three Consecutive)</a></td>
        <td><a href="./python/31636.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31654" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/1.svg" height="13" /> 31654 Adding Trouble</a></td>
        <td><a href="./python/31654.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31656" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31656 Sticky Keys</a></td>
        <td><a href="./python/31656.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31668" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31668 특별한 가지</a></td>
        <td><a href="./python/31668.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31712" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/3.svg" height="13" /> 31712 핑크빈 레이드</a></td>
        <td><a href="./python/31712.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
<tr>
        <td><a href="https://www.acmicpc.net/problem/31746" target="_blank" rel="noreferrer noopener"><img src="https://static.solved.ac/tier_small/2.svg" height="13" /> 31746 SciComLove (2024)</a></td>
        <td><a href="./python/31746.py"><img src="https://img.shields.io/badge/-%20-3572A5?style=flat-square"/> Python</a></td>
    </tr>
</table>

