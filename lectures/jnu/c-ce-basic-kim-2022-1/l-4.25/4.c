/*
  포인터형은 어차피 다 똑같은 포인터인데 int* double* 이런식으로 하지 않아도 되지 않나?
  => 포인터 연산
  int *p = &num;
  p = 1000;
  p + 1 => 1008;
  p 범위: 1000 ~ 1007
  p +1: 1008 ~
*/

#include <stdio.h>

int main(void) {
  char ch;
  char* pc = &ch;

  int n;
  int* pn = &n;

  double d;
  double* pd = &d;

  int arr[3];
  int i;

  for (i = 0; i < 3; i++) {
    printf("pc+%d = %p\n", i, pc + i);
  }
  for (i = 0; i < 3; i++) {
    printf("pc+%d = %p\n", i, pn + i);
  }
  for (i = 0; i < 3; i++) {
    printf("pd+%d = %p\n", i, pd + i);
  }
  for (i = 0; i < 3; i++) {
    printf("&arr[%d]-arr[0] = %d\n", i, &arr[i] - &arr[0]);
  }
}