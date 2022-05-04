#include <stdio.h>

int main() {
  int arr[10];
  int* parr = &arr;
  for (int i = 0; i < 10; i++) {
    scanf("%d", parr+i);
  }
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      if (*(parr+i) > *(parr+j)) {
        int tmp = *(parr+i);
        *(parr+i) = *(parr+j);
        *(parr+j) = tmp;
      }
    }
  }
  for (int i = 0; i < 10; i++) printf("%d ", *(parr+i));
  printf("\n");
  return 0;
}