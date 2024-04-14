#include <stdio.h>

int main() {
  double a, b;
  printf("두 수를 입력하세요 : ");
  scanf("%Lf %Lf", &a, &b);
  double res = a / b;
  int res_int = a / b;
  if (res != (double)(res_int)) printf("딥: %f", res);
  else printf("답: %d", res_int);
}
