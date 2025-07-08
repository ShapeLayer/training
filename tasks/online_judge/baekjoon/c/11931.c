#include <stdio.h>
#define swap(a, b) {int tmp = a; a = b; b = tmp;}

void heapify(int *arr, int index, int size) {
  int max = index, left = 2 * index + 1, right = 2 * index + 2;
  if (left < size && arr[left] > arr[max]) {
    max = left;
  }
  if (right < size && arr[right] > arr[max]) {
    max = right;
  }
  if (max != index) {
    swap(arr[max], arr[index]);
    heapify(arr, max, size);
  }
}

void compute(int *arr, int size) {
  for (int i = size / 2 - 1; i >= 0; i--) {
    heapify(arr, i, size);
  }
  for (int i = size - 1; i > 0; i--) {
    swap(arr[0], arr[i]);
    heapify(arr, 0, i);
  }
}

int main() {
  setbuf(stdout, NULL);
  int n, i, arr[1000000];
  scanf("%d", &n);
  for (i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }
  compute(arr, n - 1);
  
  for (i = n - 1; i >= 0; i--) {
    printf("%d\n", arr[i]);
  }
  return 0;
}
