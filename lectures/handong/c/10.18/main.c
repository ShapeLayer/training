#include <stdio.h>

int main(void) {
  int loop, puts[2];
  double res;
  char calcs[5] = {'+', '-', '*', '/', '%'};
  scanf("%d %d %d", &loop, &puts[0], &puts[1]);
  for (int i = 1; i < loop+1; i++) {
    if (i % 5 == 1) res = puts[0] + puts[1];
    else if (i % 5 == 2) res = puts[0] - puts[1];
    else if (i % 5 == 3) res = puts[0] * puts[1];
    else if (i % 5 == 4) res = (double)puts[0] / puts[1];
    else if (i % 5 == 0) res = puts[0] % puts[1];
    printf("%d %c %d = %g\n", puts[0], calcs[i%5 == 0 ? 4 : i%5 - 1], puts[1], res);
  }
  return 0;
}