#include <stdio.h>
#define endl "\n"

int main() {
  int arr[][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  int* p1[] = {arr, arr+1, arr+2};
  int* p2 = arr;
  printf("포인터 배열 : ");
  printf(endl);
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      printf("%d ", p1[i][j]);
    }
    printf(endl);
  }
  printf(endl);
  printf("배열에 대한 포인터 : ");
  printf(endl);
  for (int i = 0; i < 9; i++) {
    printf("%d ", *(p2+i));
    if (i % 3 == 2) printf(endl);
  }
  return 0;
}