-- https://school.programmers.co.kr/learn/courses/30/lessons/62284

/*
데이터 분석 팀에서는 우유(Milk)와 요거트(Yogurt)를 동시에 구입한 장바구니가 있는지 알아보려 합니다. 우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요. 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.
*/

SELECT CART_ID
FROM (
    SELECT CART_ID, BIT_OR(CODE) AS BIT
    FROM (
        SELECT CART_ID,
            CASE NAME
                WHEN 'Milk' THEN 1
                WHEN 'Yogurt' THEN 2
            ELSE 0
            END AS CODE
        FROM CART_PRODUCTS
    ) BIT_QUERIED
    GROUP BY CART_ID
) BITSUM_QUERIED
WHERE BIT = 3
ORDER BY CART_ID ASC;
