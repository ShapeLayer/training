#include <cstdio>

int main(void) {
  int a, b, n;

  scanf("%d %d", &a, &b);
  n = a + b;
  if (n > 0) printf("Natural Number");
  else if (n < 0) printf("Negative Number");
  else printf("0");

  return 0;
}
