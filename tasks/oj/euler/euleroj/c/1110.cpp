#include <cstdio>

int main(void) {
  int n, r1, r2;

  scanf("%d", &n);
  r1 = n / 2;
  r2 = n - r1;
  printf("%d", (r1+1) * (r2+1));

  return 0;
}
