#include <cstdio>

int main(void) {
  int a, b;

  scanf("%d", &a);
  scanf("%d", &b);

  printf("%d + %d = %d\n", a, b, a + b);
  printf("%d - %d = %d\n", a, b, a - b);
  printf("%d * %d = %d\n", a, b, a * b);
  printf("%d / %d = %d\n", a, b, a / b);
  printf("%d %% %d = %d\n", a, b, a % b);

  return 0;
}