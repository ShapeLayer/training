#include <stdio.h>

int main() {
  int arr[5] = { 10, 20, 30, 40, 50 };
  int* p = &arr[0];

  for (int i = 0; i < 5; i++, p++) {
    printf("%d\n", *p);
  }
}