#include <cstdio>

int main(void) {
  int a, b, c;

  scanf("%d %d\n", &a, &b);
  scanf("%d", &c);
  printf("%d %d", (a+(b+c)/60)%24, (b+c)%60);

  return 0;
}
