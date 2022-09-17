#include <stdio.h>

int main() {
  float pi_f = 123.123456789;
  double pi_d = 123.123456789;

  printf("float 형의 pi 값 (부동소수점) : %.9f\n", pi_f);
  printf("double 형의 pi 값 (부동소수점) : %.9lf\n", pi_d);
  printf("\n");

  printf("float 형의 pi 값 (지수표기) : %e\n", pi_f);
  printf("double 형의 pi 값 (지수표기) : %le\n", pi_d);
  printf("\n");

  printf("float 형 메모리 크기 : %d\n", sizeof(pi_f));
  printf("double 형 메모리 크기 : %d\n", sizeof(pi_d));
}