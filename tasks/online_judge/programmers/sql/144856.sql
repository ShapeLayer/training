-- https://school.programmers.co.kr/learn/courses/30/lessons/144856

/*
2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여, 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력하는 SQL문을 작성해주세요.
결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬해주세요.
*/

SELECT Q.AUTHOR_ID, A.AUTHOR_NAME, Q.CATEGORY, SUM(Q.SALES) AS TOTAL_SALES
FROM (
    SELECT S.BOOK_ID, B.AUTHOR_ID, B.CATEGORY, S.SALES * B.PRICE AS SALES
    FROM BOOK_SALES AS S
    JOIN BOOK AS B ON S.BOOK_ID = B.BOOK_ID
    WHERE S.SALES_DATE LIKE '2022-01%'
) Q
JOIN AUTHOR AS A ON A.AUTHOR_ID = Q.AUTHOR_ID
GROUP BY Q.AUTHOR_ID, Q.CATEGORY
ORDER BY Q.AUTHOR_ID ASC, Q.CATEGORY DESC;
