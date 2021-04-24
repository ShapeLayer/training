# sql
## 조건식
```SQL
SELECT (COLUMN) FROM (TABLE) WHERE (~~CONDITION~~) GROUP BY (COLUMN) HAVING (~~CONDITION~~);
```

### GROUP BY
일정한 조건에 맞춰 그룹화한다.

```SQL
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

```SQL
SELECT NAME FROM TEST GROUP BY TYPE;
```

결과:
| NAME |
| === |
| 박종현 |
| 이건우 |
| 박인후 |

### CASE WHEN
CASE WHEN은 조건문이다.  
WHEN 뒤에 조건문을 입력하고 THEN 뒤에 처리, ELSE 뒤에는 예외 처리를 입력한다.  

```SQL
CASE ~ WHEN ~ THEN ~ ELSE ~ END;
CASE WHEN NAME IS NULL THEN 'No Name' ELSE 'Name Exists' END;
```

[CASE WHEN ~ THEN ~ ELSE END](https://joke00.tistory.com/103)

### LIKE
LIKE는 Python의 str.startswith()과 비슷한 역할을 한다.  

```SQL
WHERE TABLE_A.COLUMN_1 LIKE 'Foo%'
OR TABLE_B.COLUMN_2 LIKE '%Var'
OR TABLE_A.COLUMN_2 LIKE '%oo Va%'
```

% 와일드카드가 붙은쪽으로는 다른 내용이 있어도 찾는다.  

### IN 연산자
IN 연산자는 Python의 in과 비슷한 역할을 한다.
```SQL
WHERE COLUMN IN (VALUE1, VALUE2, ...);
```

## DISTINCT
DISTINCT는 SELECT 문의 조회 대상 COLUMN 이름 앞에 붙인다.  
DISTINCT를 사용하면 중복되는 값은 제거한다.  

조회 대상이 여러개이고 하나의 COLUMN에 중복이 있을 때, 같은 ROW의 다른 COLUMN이 중복된 내용이 아니라면 그대로 조회한다.

```SQL
SELECT DISTINCT
```

## ORDER BY
ORDER BY 는 SELECT 문 뒤편에 위치한다.

```SQL
SELECT ~ ORDER BY (COLUMN_NAME) (ASC, DESC);
SELECT USERNAME FROM USERS ORDER BY USERID ASC;
```

## 함수
### DATETIME
DATETIME 자료형은 SQL 함수들을 통해 일부 데이터만 추출할 수 있다.

```
YEAR    MONTH   DAY
HOUR    MINUTE  SECOND
```

예시
```SQL
YEAR(DATETIME)
```

#### (MYSQL) DATE_FORMAT
DATE_FORMAT은 MYSQL에서 사용하는 문자열 변환 함수이다.  

```SQL
DATE_FORMAT(DATETIME, "%Y-%m-%d")
```

### IFNULL
IFNULL 함수는 대상 값이 NULL일때, 다른 값을 출력한다.  

```SQL
SELECT IFNULL((COLUMN), 'FOO_VAR') FROM TABLE_NAME;
SELECT IFNULL(NAME, 'No name') FROM NAME_LISTS;
```

### LOWER, UPPER, INITCAP
LOWER(), UPPER(), INITCAP() 함수는 영문 데이터 대소문자를 변환하는데 사용한다.  
```
LOWER('ABCD') -- abcd
UPPER('xyz')  -- XYZ
INITCAP('SHAPELAYER') -- ShapeLayer
```

### 정규식 함수
SQL에는 정규식을 사용하는 함수가 있다.  

#### REGEXP_LIKE
REGEXP_LIKE()는 변수에서 조건식에 맞는 결과를 반환한다.  
```SQL
SELECT COLUMN_1 FROM TABLE_A 
WHERE REGEXP_LIKE(COLUMN1, 'REGEX');
```

#### REGEXP_REPLACE()
REGEXP_REPLACE()는 변수에서 조건식에 맞는 결과를 변경한다.  
```SQL
SELECT COLUMN_2 FROM TABLE_B 
WHERE REGEXP_REPLACE(COLUMN2, 'REGEX', 'TO CHANGE') -- 'TO CHANGE'로 변경
```

#### REGEXP_INSTR(), REGEXP_SUBSTR()
REGEXP_INSTR()과 REGEXP_SUBSTR()은 변수에서 조건식에 맞는 단어의 위치를 반환한다.  

**REGEXP_INSTR()**: INSTR() 함수의 확장 버전이다.  
```SQL
REGEXP_INSTR(VARIABLE(COLUMN), 'REGEX'[, NUM1, NUM2])
```
변수의 NUM1번째 글자에서부터 조건식을 사용해 검색한 결과 중 NUM2번째 결과의 위치를 반환한다.  

**REGEXP_SUBSTR()**: SUBSTR() 함수의 확장 버전이다.
```SQL
REGEXP_SUBSTR(VARIABLE(COLUMN), 'REGEX'[, NUM1, NUM2])
```
변수의 NUM1번째 글자에서부터 조건식을 사용해 검색한 결과를 반환한다.

[[Oracle] 오라클 SQL에서 정규식 사용하여 문자열 잘라내기(10g 이상)](https://steemit.com/kr-dev/@capslock/oracle-sql-10g)

#### REGEXP_COUNT()
REGEXP_COUNT()는 조건식에 맞는 단어가 확인된 횟수를 반환한다.  

```SQL
REGEXP_COUNT(VARIABLE(COLUMN), 'REGEX')
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
```SQL
DECLARE @VAR_NAME (DATATYPE);   -- 변수 선언
SET @VAR_NAME = VALUE;          -- 변수 설정
SELECT @VAR_NAME;               -- 변수 출력
```

## JOIN
[[NS SQL Server #12 조인]](https://doorbw.tistory.com/223)  

### ON을 사용한 JOIN
#### INNER JOIN
두 대상 테이블 상에 공통적으로 존재하는 데이터만 병합한다. (교집합)

#### OUTER JOIN
두 대상 테이블 상에 공통적으로 존재하지 않는 데이터도 병합한다. (합집합)

(LEFT / RIGHT / FULL) OUTER JOIN 사용 가능  
LEFT: 드라이빙 테이블을 기준으로 삼음(보존함)  
RIGHT: JOIN하는 테이블을 기준으로 삼음(보존함)  

### ON을 사용하지 않는 JOIN
#### NATURAL JOIN
동일한 타입과 이름을 가진 컬럼을 그대로 조인 조건으로 사용한다.  
```SQL
SELECT ~ 
FROM TABLE_A 
NATURAL JOIN TABLE_B
NATURAL JOIN TABLE_C
...
```

#### USING 절을 사용한 JOIN
동일한 타입과 이름을 가진 컬럼이 둘 이상이면 자연 조인을 사용할 수 없다.  
이때 JOIN에 사용할 컬럼을 지정할 수 있다.

```SQL
SELECT ~
FROM TABLE_A
JOIN TABLE_B USING(COLUMN_1)
JOIN TABLE_C USING(COLUMN_2)
...
```

## 반복문 (RECURSIVE)
```SQL
WITH RECURSIVE
```
## 키
### 기본키
[기본키 이해하기](https://brunch.co.kr/@dan-kim/17)
### 외래키
[외래키 이해하기](https://brunch.co.kr/@dan-kim/26)