#include <stdio.h>

int main() {
  int arr[3];
  for (int i = 0; i < 3; i++) {
    int gets;
    scanf("%d", &gets);
    arr[i] = gets;
  }
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 2; j++) {
      if (arr[j] > arr[j+1]) {
        int tmp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = tmp;
      }
    }
  }
  printf("%d %d %d\n", arr[0], arr[1], arr[2]);
}