#include <stdio.h>

int main() {
  int arr1[5] = {1, 2, 3, 4, 5};
  for (int i = 0; i < 5; i++) printf("%d ", arr1[i]);
  printf("\n");
  int arr2[5] = {1, 2, 3};
  for (int i = 0; i < 5; i++) printf("%d ", arr2[i]);
  printf("\n");

  // 0번 인덱스 초기화, 나머지는 0으로 초기화
  int arr3[5] = { 0 };
  for (int i = 0; i < 5; i++) printf("%d ", arr3[i]);
  printf("\n");
  return 0;
}
