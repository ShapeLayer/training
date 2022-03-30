#include <stdio.h>

void printCount() {
  int count = 100;
  printf("printCount: count = %d\n", count);
}

int main() {
  int count = 0;
  printf("main: count = %d\n", count);
  printCount();

  // 두 함수 상의 같은 이름의 변수는
  // 서로 다른 변수임
  // (= 스코프가 다름)
  return 0;
}
