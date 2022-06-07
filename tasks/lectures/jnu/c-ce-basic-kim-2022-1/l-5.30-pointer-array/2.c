#include <stdio.h>

int main() {
  int arr[5] = {10, 20, 30, 40, 50};
  int(*p)[5] = &arr;

  for (int i = 0; i < 5; i++) {
    printf("%d ", (*p)[i]);
    // p[0][i]
    // *((*p)+i)
  }
  printf("\n");
  return 0;
}