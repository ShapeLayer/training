-- https://school.programmers.co.kr/learn/courses/30/lessons/131117

/*
FOOD_PRODUCT와 FOOD_ORDER 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성해주세요. 이때 결과는 총매출을 기준으로 내림차순 정렬해주시고 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬해주세요.
*/

SELECT Q.PRODUCT_ID, P.PRODUCT_NAME, (Q.AMOUNT * P.PRICE) AS TOTAL_SALES
FROM (
    SELECT PRODUCT_ID, SUM(AMOUNT) AS AMOUNT
    FROM FOOD_ORDER
    WHERE PRODUCE_DATE LIKE '2022-05%'
    GROUP BY PRODUCT_ID
) Q
JOIN FOOD_PRODUCT P
WHERE Q.PRODUCT_ID = P.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, P.PRODUCT_ID ASC;
