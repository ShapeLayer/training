#include <stdio.h>
#define swap(a, b) {int tmp = a; a = b; b = tmp;}

void quick_sort(int arr[], int init, int fin) {
  if (init >= fin) return;
  printf("init %d fin %d\n", init, fin);
  int pivot = (init+fin)/2, left = init, right = fin;
  while (left <= right) {
    while (arr[left] < arr[pivot]) left++;
    while (arr[pivot] < arr[right]) right--;
    if (left <= right) {
      if (left != right) {
        swap(arr[left], arr[right]);
      }
      left++; right--;
    }
  }
  quick_sort(arr, init, right);
  quick_sort(arr, left, fin);
}

int main() {
  int n = 10, arr[] = {10, 6, 3, 2, 5, 6, 9, 1, 3 ,10};
  for (int i = 0; i < n; i++) printf("%d ", arr[i]);
  printf("\n");
  quick_sort(arr, 0, 9);
  for (int i = 0; i < n; i++) printf("%d ", arr[i]);
  printf("\n");
  return 0;
}
