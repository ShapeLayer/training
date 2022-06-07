#include <stdio.h>
#include <stdlib.h>

int main() {
  int size;
  int* arr = NULL;
  int sum = 0;
  double average = 0.0;
  
  printf("몇 개의 정수를 입력하시겠습니까? : ");
  scanf("%d", &size);
  arr = malloc(sizeof(int) * size);
  if (arr = NULL) { return -1; }

  printf("정수를 입력하세요: ");
  for (int i = 0; i < size; i++) {
    scanf("%d", arr+i);
    sum += arr[i];
  }

  average = (double)sum / (double)size;
  printf("합계 = %d, 평균 = %d", sum, average);
}