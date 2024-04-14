// Chap8 Sec3 포인터와 문자열 (p.326)

#include <stdio.h>
#include <string.h>

int main() {
   char* p;
   char name[20];
   char* p1 = name;
   char* p2 = "abc";

   p1[0] = 'A';
   p2[0] = 'B'; // 컴파일 오류는 발생하지 않음. 하지만 런타임 오류
   // 그래서 char* p2를 const char* p2로 바꾸자
   // const char* p2 = "abc";
   // p2는 const 포인터라고 명칭
   return 0;
}