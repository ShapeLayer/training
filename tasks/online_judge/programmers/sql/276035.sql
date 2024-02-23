-- https://school.programmers.co.kr/learn/courses/30/lessons/276035

/*
DEVELOPERS 테이블에서 Front End 스킬을 가진 개발자의 정보를 조회하려 합니다. 조건에 맞는 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성해 주세요.

결과는 ID를 기준으로 오름차순 정렬해 주세요.
*/

SELECT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS AS D
JOIN (
    SELECT BIT_OR(CODE) AS BITSUM
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
) AS J
WHERE J.BITSUM & D.SKILL_CODE > 0
ORDER BY ID ASC;
