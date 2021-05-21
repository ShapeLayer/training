#include <cstdio>

int main(void) {
  int lock1, lock2;

  scanf("%d %d", &lock1, &lock2);
  if (lock1 % 2 == 1 && lock2 % 2 == 0) printf("0");
  else printf("1");

  return 0;
}
