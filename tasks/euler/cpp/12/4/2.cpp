#include <cstdio>

int main(void) {
  int a, b;
  
  scanf("%d %d", &a, &b);
  if ((a+b) % 2 == 1) printf("odd");
  else printf("even");

  return 0;
}
