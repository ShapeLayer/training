#include <stdio.h>
#define SIZE 5

int main() {
  int arr[SIZE];
  int* parr[SIZE];
  for (int i = 0; i < SIZE; i++) (parr[i]) = arr+i;
  printf("입력 : ");
  for (int i = 0; i < SIZE; i++) scanf("%d", &arr[i]);
  for (int i = 0; i < SIZE; i++) {
    printf("%d번째 원소 값 : %d, 주소 : %d\n", i, arr[i], parr[i]);
  }
  return 0;
}