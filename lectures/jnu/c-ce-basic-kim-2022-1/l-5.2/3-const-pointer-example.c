#include <stdio.h>
#include <string.h>
#define MAX_STR 40

int main() {
    // const char*는 보통 이렇게 쓰임
    const char* filename = "test.txt";

    char str[MAX_STR] = "Hello World";
    char* ps1 = NULL; // 메모리 주소 변경 가능함
    const char* ps2 = NULL; // 메모리 주소 변경 안됨
    ps1 = str;
    // ps1 = "Good-bye"; // 작동하지 않음
    ps2 = str;
    ps2 = "Good-bye"; // 작동함

    /*
        다른 언어와는 다른, 큰 차이점임: 헷갈리기 쉬우니 유의할 것
        배열의 시작 메모리 주소는 변경하면 안되니 const char로 사용해야함
    */

    return 0;
}