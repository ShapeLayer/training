#include <stdio.h>
#define swap(a, b) {int tmp = a; a = b; b = tmp;}

void compute(int *arr, int start, int end) {
  if (start >= end) return;
  int p1 = arr[start], p2 = arr[end];
  int low = start + 1;
  int high = end - 1;
  int now = low + 1;

  while (now <= high) {
    if (arr[now] < p1) {
      swap(arr[now], arr[low]);
      now++;
      low++;
    } else if (arr[now] > p2) {
      swap(arr[now], arr[high]);
      high--;
    } else {
      now++;
    }
  }

  low--;
  high++;
  swap(arr[start], arr[low]);
  swap(arr[end], arr[high]);

  compute(arr, start, low - 1);
  compute(arr, low + 1, high - 1);
  compute(arr, high + 1, end);
}

int main() {
  setbuf(stdout, NULL);
  int n, i, arr[1000000];
  scanf("%d", &n);
  for (i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }
  compute(arr, 0, n - 1);
  
  for (i = n - 1; i >= 0; i--) {
    printf("%d\n", arr[i]);
  }
  return 0;
}
