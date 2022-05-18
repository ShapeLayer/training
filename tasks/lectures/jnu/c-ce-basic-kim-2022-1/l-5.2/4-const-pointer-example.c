#include <stdio.h>

int main() {
    char str1[20] = "Hello World";
    char str2[20] = "Good Bye";

    char* const p1 = str1;
    const char* p2 = str1;
    const char* const p3 = str1;
    str1[3] = 'B';
    
    /*
        정리:
            char* const p1 = str1;
                p1 변경 불가
            const char* p2 = str1;
                p2의 주소 변경 불가, 값 변경 가능
            const char* const p3 = str1;
                둘 다 변경 불가
    */
    return 0;
}