#include <stdio.h>

int main() {
  int gets;
  printf("정수를 입력하세요 : ");
  scanf("%d", &gets);
  printf("10진수          : %d\n", gets);
  printf("8진수           : %o\n", gets);
  printf("16진수(소문자)  : %x\n", gets);
  printf("16진수(대문자)  : %X\n", gets);
  return 0;
}