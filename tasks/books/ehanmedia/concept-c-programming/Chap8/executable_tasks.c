/*
  P.78, Chapter 8.
*/

/* Lab08.c */
#include <stdio.h>

int main() {
  char str[256];
  char* pstr = str;
  int len;

  printf("문자열을 입력하세요 : ");
  gets(str);

  len = 0;
  while(*pstr != '\0') {
    len++;
    pstr++;
  }

  printf("문자열의 길이 : %d\n", len);

  return 0;
}
