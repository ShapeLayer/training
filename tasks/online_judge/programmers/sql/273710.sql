-- https://school.programmers.co.kr/learn/courses/30/lessons/273710

-- ROOT 아이템을 찾아 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME)을 출력하는 SQL문을 작성해 주세요. 이때, 결과는 아이템 ID를 기준으로 오름차순 정렬해 주세요.

SELECT ITEM_ID, ITEM_NAME
FROM ITEM_INFO
WHERE ITEM_ID
IN (
    SELECT ITEM_ID
    FROM ITEM_TREE
    WHERE PARENT_ITEM_ID IS NULL
)
ORDER BY ITEM_ID ASC;
