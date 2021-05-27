#include <cstdio>

int main(void) {
  int l, r;

  scanf("%d %d", &l, &r);
  if (l > r) printf(">");
  else if (l < r) printf("<");
  else printf("=");

  return 0;
}
