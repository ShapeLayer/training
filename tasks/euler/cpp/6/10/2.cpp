#include <cstdio>

int main(void) {
  double a = 12.34, b = 23.12;

  printf("%.2lf + %.2lf = %.2lf\n", a, b, a + b);
  printf("%.2lf - %.2lf = %.2lf\n", a, b, a - b);
  printf("%.2lf * %.2lf = %.2lf\n", a, b, a * b);
  printf("%.2lf / %.2lf = %.2lf\n", a, b, a / b);

  return 0;
}