// Theme: for문
#include <stdio.h>

int main() {
  int i;
  int sum = 0;
  int factorial = 1;

  for (i = 1; i <= 10; i++) {
    sum += i;
    factorial *= i;
  }

  printf("1~10의 합 : %d\n", sum);
  printf("1~10의 곱 : %d\n", factorial);
}