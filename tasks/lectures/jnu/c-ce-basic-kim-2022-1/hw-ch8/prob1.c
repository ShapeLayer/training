#include <stdio.h>

int main() {
  const int pi = 3.141592;
  int* ppi = &pi;

  printf("pi의 주소 \t: %d\n", ppi);
  printf("pi의 값 \t: %d\n", *ppi);
  return 0;
}