#include <stdio.h>

int main() {
  int a = 5;
  int b1 = 3;
  float b2 = 3.0;

  printf("%f\n", a / b1);
  printf("%f\n", (float)a / b1);
  printf("%f\n", (float)(a / b1));
  printf("%f\n", a / b2);
  
  return 0;
}