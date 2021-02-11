# sql
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

## GROUP BY