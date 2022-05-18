#include <stdio.h>

void PrintArray(const int* arr, int size);
void SortArray(int* arr, int size);

int main() {
  int x[5] = { 43, 6, 24, 88, 34};
  int y[10] = { 12, 35, 7, 54, 23, 10, 65, 10, 11, 87 };

  printf("정렬 이전\n");
  PrintArray(x, 5);
  SortArray(x, 5);
  printf("정렬 이후\n");
  PrintArray(x, 5);
  
  printf("정렬 이전\n");
  PrintArray(y, 10);
  SortArray(y, 10);
  printf("정렬 이후\n");
  PrintArray(y, 10);

  return 0;
}

void PrintArray(const int* arr, int size) {
  for (int i = 0 ; i < size; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

void SortArray(int* arr, int size) {
  int temp, index;

  for (int i = 0; i < size - 1; i ++) {
    index = i;
    for (int j = i + 1; j < size; j++) {
      if (arr[index] > arr[j]) {
        index = j;
      }
    }
    temp = arr[i];
    arr[i] = arr[index];
    arr[index] = temp;
  }
}