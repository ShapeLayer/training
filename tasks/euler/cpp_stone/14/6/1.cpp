#include <cstdio>

int main(void) {
  int a;

  scanf("%d", &a);
  if (a > 0 && a <= 10) printf("1 or more and 10 or less");
  else printf("less than 1 or greater then 10");

  return 0;
}
