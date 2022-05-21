#include <stdio.h>

int main(void) {
  char ch;

  while(1) {
    printf("영문자를 입력하세요 : ");
    scanf(" %c", &ch);
    if (ch == '.') break;
    printf("'%c'는 ", ch);
    if ((int)ch >= 65 && (int)ch <= 9) printf("대문자입니다.\n");
    else if ((int)ch >= 97 && (int)ch <= 122) printf("소문자입니다.\n");
    else printf("영문자가 아닙니다.\n");
  }
  return 0;
}