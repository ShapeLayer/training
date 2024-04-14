// Chap8 Sec3 포인터와 문자열 (p.326)

#include <stdio.h>
#include <string.h>

int main() {
    /*
     리터럴 => 레지스터 - 처리되고 사라지기 때문에 책에서는 임시값으로 표현
     변수 => 메모리
     * 거의 모든 리터럴은 휘발성을 띄고 있음. 단, 예외: 리터럴 문자열
       컴퓨터는 문자열을 레지스터에 넣을 수 없음.. 문자열 자체가 특정한 길이를 갖는 배열이기 때문
       = 문자열은 메모리에 저장 
    */
    // int* pi = {1, 2, 3, 4, 5}; // 오류 발생
    char* p = "abcde";
    printf("p = %s\n", p);
    printf("p = %p\n", p);
    printf("p = %p\n", "abcde");

    p = "hello";
    printf("p = %s\n", p);
    printf("p = %p\n", p);
    printf("p = %p\n", "hello");

    /*
     char str[20];
     str = "Hello, World!";
     를 하면 안되는 이유:
        1. str은 배열의 시작 주소임
        2. "Hello, World!"는 이 문자 배열(문자열 리터럴)의 시작 주소임
        3. 배열의 시작 주소는 변경할 수 없으므로 오류
     strcpy(str, "Hello World");
    */
    return 0;
}