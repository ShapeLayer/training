#include <stdio.h>

int main() {
  int n = 0;
  int is_even = 0; // 짝수 여부 기록

  printf("input number: ");
  scanf("%d", &n);

  if (n % 2 == 0) {
    is_even = 1; // 짝수 여부 기록
    n++;
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j ++) {
      if (j == i || j == n-i-1) {
        if (is_even == 1) printf("+");
        else printf("*");
      }
      else printf(" ");
    }
    printf("\n");
  }
  
  return 0;
}