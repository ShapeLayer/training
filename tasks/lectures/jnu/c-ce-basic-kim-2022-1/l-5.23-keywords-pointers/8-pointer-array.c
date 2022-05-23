#include <stdio.h>

int main() {
  int arr[3][5] ={
    {1, 2, 3, 4, 5},
    {6, 7, 8, 9, 10},
    {11, 12, 13, 14, 15}
  };

  int (*p)[5] = arr;
  // p   = &arr[0]
  // p+1 = &arr[1]
  // p+2 = &arr[2]
  // *p     = arr[0]
  // *(p+1) = arr[1]
  // *(p+2) = arr[2]
  // p[2][1] = arr[2][1]
  // printf("%d\n", (*(p+2))[1]); // (=arr[2][1])

  int i, j;

  for (i = 0; i < 3; i++) {
    for (j = 0; j < 5; j++) {
      printf("%2d ", p[i][j]);
    }
    printf("\n");
  }

  return 0;
}