#include <stdio.h>

int main() {
  int n, sums = 0, gets;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &gets);
    sums += gets - 1 >= 0 ? gets - 1 : 0;
  }
  printf("%d\n", sums+1);
}