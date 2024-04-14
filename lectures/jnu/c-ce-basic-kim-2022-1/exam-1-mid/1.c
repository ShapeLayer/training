#include <stdio.h>
#define PI 3.14

int main() {
  double r1, r2, h;
  printf("반지름 2개와 높이를 이력하세요 : ");
  scanf("%lf %lf %lf", &r1, &r2, &h);
  double res = (1.0 / 3)*PI*h*(r1*r1 + r1*r2 + r2*r2);
  printf("부피는 %lf입니다.\n", res);
  return 0;
}