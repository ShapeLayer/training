#include <stdio.h>

int main() {
  int a, b, c, d, p;
  scanf("%d %d %d %d %d", &a, &b, &c, &d, &p);
  int price_x = a * p;
  int price_y = b + ((p - c) >= 0 ? (p - c) : 0) * d;
  if (price_x < price_y) {
    printf("%d\n", price_x);
  } else {
    printf("%d\n", price_y);
  }
  return 0;
}