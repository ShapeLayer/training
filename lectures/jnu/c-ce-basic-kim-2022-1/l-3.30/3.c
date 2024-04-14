#include <stdio.h>

int GetFactorial(int num) {
  int fact = 1;
  for (int i = 01; i <= num; i++) fact *= i;
  return fact;
}

int GetSum(int num) {
  int sum = 0;
  for (int i = 1; i <= num; i++) sum += i;
  return sum;
}

int main() {
  int result1, result2, gets;
  printf("num? ");
  scanf("%d", &gets);
  result1 = GetFactorial(gets);
  result2 = GetSum(gets);
  printf("num! = %d, sum = %d\n", result1, result2);
  return 0;
}
