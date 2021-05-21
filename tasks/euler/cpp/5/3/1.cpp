#include <cstdio>

int main(void) {
  printf("%10.3lf\n", 12.345);
  printf("%10.3lf\n", 34.567);
  printf("%10.3lf\n", 56.789);
  printf("%10.3lf\n", 456.78);
  printf("----------\n");
  printf("%10.3lf\n", 12.345 + 34.567 + 56.789 + 456.78);

  return 0;
}