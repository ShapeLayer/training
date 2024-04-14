#include <stdio.h>

int main() {
  int count;

  count = 10;
  printf("count = %d\n", count + 10);
  printf("count = %d\n", count++);
  printf("count = %d\n", ++count);

  return 0;
}