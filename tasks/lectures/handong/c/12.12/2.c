#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void input_array(int arr[], int n) {
  printf("Array: \n");
  for (int i = 0; i < n; i++) printf("%4d ", arr[i]);
  printf("\n");
}
void output_array(int arr[], int n) {
  printf("===============sorted array===============\n");
  printf("Array: \n");
  for (int i = 0; i < n; i++) printf("%4d ", arr[i]);
  printf("\n");
}
void swap(int* a, int* b) {
  int tmp = *a;
  *a = *b;
  *b = tmp;
}
bool sort(int arr[], int n) {
  int tmp, trigger = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        swap(&arr[j], &arr[j+1]);
        trigger = 1;
      }
    }
  }
  return trigger;
}

int main(void) {
  int n;
  printf("input number of data: ");
  scanf("%d", &n);
  int arr[n];
  for (int i = 0; i < n; i++) {
    int r = rand() % 100;
    r = r >=10 ? r : r+10;
    arr[i] = r;
  }
  input_array(arr, n);

  if (sort(arr, n)) printf("Called swap function\n");
  output_array(arr, n);
  printf("min: %d, max: %d", arr[0], arr[n-1]);
  return 0;
}