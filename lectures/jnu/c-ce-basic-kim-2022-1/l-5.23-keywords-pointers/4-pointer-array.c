#include <stdio.h>

int main(void) {
  int a = 10, b = 20, c = 30, d = 40, e = 50;
  int* arr[5] = {&a, &b, &c, &d, &e};

  int i;

  for (i = 0; i < 5; i++) {
    printf("%d ", *arr[i]);
  }

  printf("\n");
  return 0;
}