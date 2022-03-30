#include <stdio.h>

void Swap(int x, int y) {
  int temp;
  temp = x;
  x = y;
  y = temp;
}

int main() {
  int a = 10;
  int b = 20;

  printf("Swap 전의 a = %d, b = %d\n", a, b);
  Swap(a, b);
  printf("Swap 후의 a = %d, b = %d\n", a, b); 
  // printf 호출 위치가 Swap 함수 스코프에 해당하지 않으므로 변경되지 않음
  // (related) Pointer

  return 0;
}
