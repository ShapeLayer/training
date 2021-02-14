-- 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;

-- 동명 동물 수 찾기
SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME;

/*
SELECT NAME, COUNT(NAME) FROM ANIMAL_INS WHERE COUNT(NAME) > 1 GROUP BY NAME ORDER BY NAME;
를 실행하면 "Invalid use of group function"이 발생한다.
COUNT(NAME)이 GROUP BY의 결과를 보여주고 있어서 GROUP BY 이전에 WHERE COUNT() 조건을 사용할 수 없는 것으로 보인다.
*/

-- 입양 시각 구하기(1)
-- https://programmers.co.kr/questions/15813

SELECT HOUR(DATETIME) AS H, COUNT(DATETIME) 
FROM ANIMAL_OUTS 
GROUP BY H 
HAVING H >= 9 AND H <= 19 
ORDER BY H;

-- 입양 시각 구하기(2)
-- https://chanhuiseok.github.io/posts/db-6/

SET @H := -1; -- 변수 선언
SELECT (@H := @H + 1) AS 'HOUR', -- 0시부터 23시까지 'HOUR' 항목으로 추가
    (SELECT COUNT(DATETIME) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @H) AS 'COUNT'
    -- @H 와 같은 값의 HOUR(DATETIME)을 찾아서 COUNT함
FROM ANIMAL_OUTS
WHERE @H < 23; -- @H의 범위를 23까지 설정하여 0부터 23까지 반환함