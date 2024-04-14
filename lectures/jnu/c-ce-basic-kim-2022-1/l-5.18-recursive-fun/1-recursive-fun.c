#include <stdio.h>

int GetGCD(int m, int n);

int main() {
  int x, y;

  printf("두 정수를 입력하세요 : ");
  scanf("%d %d", &x, &y);
  printf("%d, %d의 최대공약수는 %d입니다.\n", x, y, GetGCD(x, y));

  return 0;
}

int GetGCD(int m, int n) {
  if (m % n == 0) return n;
  return GetGCD(n, m % n);
}