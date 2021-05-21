#include <cstdio>
#include <cmath>

int main(void) {
  double n;
  int sum = 0;
  for (int i = 0; i < 5; i++) {
    if (i == 0) n = pow(10, i);
    else n += pow(10, i);
    sum = sum + (int)n;
    printf("%10.f\n", n);
  }
  printf("----------\n");
  printf("%10d", sum);

  return 0;
}