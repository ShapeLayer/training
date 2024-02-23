-- https://school.programmers.co.kr/learn/courses/30/lessons/131532

/*
USER_INFO 테이블과 ONLINE_SALE 테이블에서 년, 월, 성별 별로 상품을 구매한 회원수를 집계하는 SQL문을 작성해주세요. 결과는 년, 월, 성별을 기준으로 오름차순 정렬해주세요. 이때, 성별 정보가 없는 경우 결과에서 제외해주세요.
*/

-- SELECT YEAR, MONTH, GENDER, USERS

SELECT YEAR, MONTH, GENDER, COUNT(DISTINCT USER_ID) AS USERS
FROM (
    SELECT
        USER_ID,
        SUBSTRING(SALES_DATE, 1, 4) AS YEAR,
        CONVERT(SUBSTRING(SALES_DATE, 6, 2), UNSIGNED) AS MONTH,
        GENDER 
    FROM ONLINE_SALE
    JOIN USER_INFO USING(USER_ID)
    WHERE GENDER IS NOT NULL
) AS QUERIED
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR ASC, MONTH ASC, GENDER ASC;
