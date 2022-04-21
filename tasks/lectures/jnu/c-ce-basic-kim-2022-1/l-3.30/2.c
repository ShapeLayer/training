#include <stdio.h>

void printSumAndAverage(int a, int b) {
  printf("합계 : %d\n", a + b);
  printf("평균 : %f\n", (double)(a+b)/2);
}

int main() {
  int x, y;
  printSumAndAverage(10, 20);
  printf("두 정수를 입력하세요 : ");
  scanf("%d %d", &x, &y);
  printSumAndAverage(x, y);
  return 0;
}
