# sql
## 조건식
```
SELECT (COLUMN) FROM (TABLE) WHERE (~~CONDITION~~) GROUP BY (COLUMN) HAVING (~~CONDITION~~);
```

### GROUP BY
일정한 조건에 맞춰 그룹화한다.

```
SELECT (COLUMN) FROM (TABLE) GROUP BY (COLUMN);
```

| ID (INT) | TYPE (INT) | NAME (TEXT) |
| === | === | === |
| 1 | 0 | 박종현 |
| 2 | 0 | 이창현 |
| 3 | 0 | 왕은재 |
| 4 | 1 | 이건우 |
| 5 | 1 | 박영준 |
| 6 | 2 | 박영준 |

상태에서 GROUP BY로 데이터를 그냥 조회했더니 각 그룹의 가장 위쪽 값이 나온다. ([SQL Fiddle](http://sqlfiddle.com/#!9/351095/1/0))

```
SELECT NAME FROM TEST GROUP BY TYPE;
```

결과:
| NAME |
| === |
| 박종현 |
| 이건우 |
| 박인후 |

## DISTINCT
DISTINCT는 SELECT 문의 조회 대상 COLUMN 이름 앞에 붙인다.  
DISTINCT를 사용하면 중복되는 값은 제거한다.  

조회 대상이 여러개이고 하나의 COLUMN에 중복이 있을 때, 같은 ROW의 다른 COLUMN이 중복된 내용이 아니라면 그대로 조회한다.

```
SELECT DISTINCT
```

## ORDER BY
ORDER BY 는 SELECT 문 뒤편에 위치한다.

```
SELECT ~ ORDER BY (COLUMN_NAME) (ASC, DESC);
SELECT USERNAME FROM USERS ORDER BY USERID ASC;
```

## DATETIME
DATETIME 자료형은 SQL 함수들을 통해 일부 데이터만 추출할 수 있다.

```
YEAR    MONTH   DAY
HOUR    MINUTE  SECOND
```

예시
```
YEAR(DATETIME)
```

## SELECT INTO
`SELECT COLUMN INTO (TABLE1) FROM (TABLE2)` 를 통해 이미 있던 테이블, TABLE2의 값을 임시로 테이블을 만들어(TABLE1) 값을 복사할 수 있다.

```
테이블 이름에 따라 임시 테이블이 작동하는 방식

#TABLENAME 연결중인 세션에서만 임시로 사용 가능, 세션 종료 시 삭제
##TABLENAME 다른 세션에서도 사용 가능, 세션 종료 시 삭제
```

## DECLARE
변수를 선언할 수 있다.
```
DECLARE @VAR_NAME (DATATYPE);   -- 변수 선언
SET @VAR_NAME = VALUE;          -- 변수 설정
SELECT @VAR_NAME;               -- 변수 출력
```

## JOIN
[[NS SQL Server #12 조인]](https://doorbw.tistory.com/223)  
### INNER JOIN
두 대상 테이블 상에 공통적으로 존재하는 데이터만 병합 (교집합)

### OUTER JOIN
두 대상 테이블 상에 공통적으로 존재하지 않는 데이터도 병합 (합집합)