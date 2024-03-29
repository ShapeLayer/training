#include <stdio.h>

void GetSumProduct(int x, int y, int* sum, int* product);

int main() {
  int a = 5, b = 8;
  int res1, res2;

  GetSumProduct(a, b, &res1, &res2);

  printf("%d + %d = %d\n", a, b, res1);
  printf("%d * %d = %d\n", a, b, res2);
  
  return 0;
}

void GetSumProduct(int x, int y, int* sum, int* product) {
  *sum = x + y;
  *product = x * y;
}