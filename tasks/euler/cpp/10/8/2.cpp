#include <cstdio>

int main(void) {
  int a, b, c;

  scanf("%d %d %d", &a, &b, &c);
  printf("%d\n%.2lf", a+b+c, (double)(a+b+c)/3);

  return 0;
}
