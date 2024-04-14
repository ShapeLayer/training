#include <stdio.h>

int main() {
  int sum = 0;
  register int i;
  for (i = 0; i < 10000; i++) {
    sum += 1;
  }
}